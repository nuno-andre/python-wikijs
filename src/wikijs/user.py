from typing import TYPE_CHECKING, Any
from .typing import WikiJsProtocol


if TYPE_CHECKING:
    from typing import Dict, List, Optional


class UserMixin(WikiJsProtocol):
    # region USER QUERY
    def list_users(
        self,
        filter:   'Optional[str]' = None,
        order_by: 'Optional[str]' = None,
    ) -> 'List[Dict[str, Any]]':
        query = '''
            query User(
                $filter: String,
                $orderBy: String
            ) {
                users {
                    list (
                        filter: $filter,
                        orderBy: $orderBy
                    ) {
                        id, name, email, providerKey, isSystem, isActive, createdAt, lastLoginAt
                    }
                }
            }
        '''

        params = dict(filter=filter, orderBy=order_by)

        return self.execute(query, params)['users']['list']

    def search_users(self, **kwargs) -> Any:
        raise NotImplementedError

    def get_user(self, id: int) -> Any:
        raise NotImplementedError
    # endregion

    # region USER MUTATION
    # endregion
