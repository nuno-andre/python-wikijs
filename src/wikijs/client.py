from typing import Any, TYPE_CHECKING
from functools import cached_property

from gql import gql, Client

from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
from graphql.error.graphql_error import GraphQLError

from .exceptions import ClientError, raise_exc

from .asset import AssetMixin
from .page import PageMixin
from .system import SystemMixin
from .user import UserMixin

if TYPE_CHECKING:
    from typing import Dict, Optional


class WikiJs(AssetMixin, PageMixin, SystemMixin, UserMixin):
    def __init__(self, endpoint, api_key) -> None:
        self.endpoint = endpoint
        self.api_key = api_key

    @cached_property
    def client(self) -> Client:
        headers = {'Authorization': f'Bearer {self.api_key}'}
        transport = AIOHTTPTransport(url=self.endpoint, headers=headers)
        return Client(transport=transport, fetch_schema_from_transport=True)

    def execute(self, query: str, params: 'Optional[Dict[str, Any]]' = None) -> Any:
        try:
            return self.client.execute(gql(query), variable_values=params)
        except GraphQLError as e:
            raise ClientError(e.message) from None
        except TransportQueryError as e:
            raise ClientError(e.errors) from None

    def check_response_result(self, result: 'Dict[str, Any]') -> bool:
        if not result['succeeded']:
            raise_exc(result['errorCode'], result['message'])
        return True
