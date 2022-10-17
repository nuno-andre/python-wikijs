from .typing import WikiJsProtocol, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .typing import AssetKind


class AssetMixin(WikiJsProtocol):

# region ASSET QUERY
    def list_assets(self, folder_id: int, kind: AssetKind) -> Any:
        query = '''
        '''

        params = dict(folderId=folder_id, kind=kind)

        raise NotImplementedError
# endregion

# region ASSET MUTATION
# endregion
