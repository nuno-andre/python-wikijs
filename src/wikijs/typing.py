from typing import Any, Union, Protocol, TypeVar, TYPE_CHECKING
from enum import Enum


class StrEnum(str, Enum):
    __str__ = str.__str__


class AssetKind(StrEnum):
    IMAGE  = 'IMAGE'
    BINARY = 'BINARY'
    ALL    = 'ALL'


class CacheControlScope(StrEnum):
    PUBLIC  = 'PUBLIC'
    PRIVATE = 'PRIVATE'


class NavigationMode(StrEnum):
    NONE   = 'NONE'
    TREE   = 'TREE'
    MIXED  = 'MIXED'
    STATIC = 'STATIC'


class PageOrderBy(StrEnum):
    CREATED = 'CREATED'
    ID      = 'ID'
    PATH    = 'PATH'
    TITLE   = 'TITLE'
    UPDATED = 'UPDATED'


class PageOrderByDirection(StrEnum):
    ASC  = 'ASC'
    DESC = 'DESC'


class PageRuleMatch(StrEnum):
    START = 'START'
    EXACT = 'EXACT'
    END   = 'END'
    REGEX = 'REGEX'
    TAG   = 'TAG'


class PageTreeMode(StrEnum):
    FOLDERS = 'FOLDERS'
    PAGES   = 'PAGES'
    ALL     = 'ALL'


class SystemImportUsersGroupMode(StrEnum):
    MULTI  = 'MULTI'
    SINGLE = 'SINGLE'
    NONE   = 'NONE'


if TYPE_CHECKING:
    from typing import Any, Dict, Optional
    from gql import Client

    class WikiJsProtocol(Protocol):
        @property
        def client(self) -> Client: ...
        def execute(self, query: str, params: 'Optional[Dict[str, Any]]' = None) -> Any: ...
        def check_response_result(self, result: 'Dict[str, Any]') -> bool: ...

else:
    class WikiJsProtocol(): ...


T = TypeVar('T')

class Unset: ...

Unforced = Union[Unset, T]
Nullable = Union[Unset, None, T]

unset = Unset()
