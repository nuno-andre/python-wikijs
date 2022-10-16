from typing import TYPE_CHECKING, Any
from .typing import WikiJsProtocol


if TYPE_CHECKING:
    from typing import Dict, List


class UserMixin(WikiJsProtocol):
    # region USER QUERY
    def list_users(self, filter: str, order_by: str) -> Any:
        params = dict(filter=filter, orderBy=order_by)
        raise NotImplementedError

    def search_users(self, **kwargs) -> Any:
        raise NotImplementedError
    # endregion

    # region USER MUTATION
    # endregion
