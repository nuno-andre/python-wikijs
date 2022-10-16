from typing import TYPE_CHECKING, Any
from .typing import WikiJsProtocol


if TYPE_CHECKING:
    from typing import List, Dict, Optional
    from .typing import PageOrderBy, PageOrderByDirection



class PageMixin(WikiJsProtocol):

# region PAGE QUERY
    def get_all_pages(self, order_by='TITLE') -> 'List[Dict[str, Any]]':
        query = '{ pages { list (orderBy: %s) { id path title } } }' % order_by

        return self.execute(query)['pages']['list']

    def search_pages(
        self,
        query:  str,
        path:   'Optional[str]' = None,
        locale: 'Optional[str]' = None,
    ) -> 'List[Dict[str, Any]]':

        _query = '''
            query Page(
                $query: String!,
                $path: String,
                $locale: String
            ) {
                pages {
                    search (
                        query: $query,
                        path: $path,
                        locale: $locale
                    ) {
                        results { id, title, description, path, locale },
                        suggestions,
                        totalHits
                    }
                }
            }
        '''
        params = dict(query=query, path=path, locale=locale)

        return self.execute(_query, params)['pages']['search']['results']

    def search_tags(self, query: str) -> Any:
        _query = '''
        '''
        params = dict(query=query)
        raise NotImplementedError

    def list_pages(
        self,
        limit:      'Optional[int]' = None,
        order_by:   'Optional[PageOrderBy]' = None,
        direction:  'Optional[PageOrderByDirection]' = None,
        tags:       'Optional[List[str]]' = None,
        locale:     'Optional[str]' = None,
        creator_id: 'Optional[int]' = None,
        author_id:  'Optional[int]' = None,
    ) -> Any:
        query = '''
        '''
        params = dict(limit=limit, orderBy=order_by, orderByDirection=direction,
                      tags=tags, locale=locale, creatorId=creator_id, authorId=author_id)
        raise NotImplementedError
# endregion

# region PAGE MUTATION
    # TODO: publishEndDate, publishStartDate, scriptCss, scriptJs
    def create_page(
        self,
        title:        str,
        content:      str,
        description:  str,
        editor:       str,
        is_published: bool,
        is_private:   bool,
        locale:       str,
        path:         str,
        tags:         'List[str]' = [],
    ) -> 'Dict[str, Any]':
        mutation = '''
            mutation Page(
                $content: String!,
                $description: String!,
                $editor: String!,
                $isPublished: Boolean!,
                $isPrivate: Boolean!,
                $locale: String!,
                $path: String!,
                $tags: [String]!,
                $title: String!
            ) {
                pages {
                    create (
                        content: $content,
                        description: $description,
                        editor: $editor,
                        isPublished: $isPublished,
                        isPrivate: $isPrivate,
                        locale: $locale,
                        path: $path,
                        tags: $tags,
                        title: $title
                    ) {
                        responseResult {
                            succeeded,
                            errorCode,
                            slug,
                            message
                        },
                        page {
                            id,
                            path,
                            title
                        }
                    }
                }
            }
        '''

        params = dict(
            title=title, content=content, description=description,
            editor=editor, isPublished=is_published, isPrivate=is_private,
            locale=locale, path=path, tags=tags
        )

        resp = self.execute(mutation, params)['pages']['create']
        self.check_response_result(resp['responseResult'])
        return resp['page']

    # TODO: publishEndDate, publishStartDate, scriptCss, scriptJs
    def update_page(
        self,
        title:        str,
        content:      str,
        description:  str,
        editor:       str,
        is_published: bool,
        is_private:   bool,
        locale:       str,
        path:         str,
        tags:         'List[str]' = [],
    ) -> 'Dict[str, Any]':
        mutation = '''
        '''

        params = dict(
            title=title, content=content, description=description,
            editor=editor, isPublished=is_published, isPrivate=is_private,
            locale=locale, path=path, tags=tags
        )
        raise NotImplementedError

    def convert_page(self, id: int, editor: str) -> Any:
        mutation = '''
        '''

        params = dict(id=int(id), editor=editor)
        raise NotImplementedError

    def move_page(self, id: int, dest_path: str, dest_locale: str) -> Any:
        mutation = '''
            mutation Page(
                $id: Int!,
                $destinationPath: String!,
                $destinationLocale: String!
            ) {
                pages {
                    move (
                        id: $id,
                        destinationPath: $destinationPath,
                        destinationLocale: $destinationLocale
                    ) {
                        responseResult {
                            succeeded,
                            errorCode,
                            slug,
                            message
                        }
                    }
                }
            }
        '''

        params = dict(id=int(id), destinationPath=dest_path, destinationLocale=dest_locale)

        resp = self.execute(mutation, params)['pages']['move']
        return self.check_response_result(resp['responseResult'])

    def delete_page(Self, id: int) -> Any:
        mutation = '''
        '''

        params = dict(id=id)
        raise NotImplementedError

    def delete_tag(self, id: int) -> Any:
        mutation = '''
        '''

        params = dict(id=id)
        raise NotImplementedError

    def update_tag(self, id: int, tag: 'List[str]', title: str) -> Any:
        mutation = '''
        '''

        params = dict(id=id, tag=tag, title=title)
        raise NotImplementedError

    def flush_cache(self) -> Any:
        mutation = '''
        '''

        raise NotImplementedError

    def migrate_to_locale(self, source: str, target: str) -> Any:
        mutation = '''
        '''

        params = dict(sourceLocale=source, targetLocale=target)
        raise NotImplementedError

    def rebuild_tree(self) -> Any:
        mutation = '''
        '''

        raise NotImplementedError

    def render(self, id: int) -> Any:
        mutation = '''
        '''

        params = dict(id=id)
        raise NotImplementedError

    def restore(self, page_id: int, version_id: int) -> Any:
        mutation = '''
        '''

        params = dict(pageId=page_id, versionId=version_id)
        raise NotImplementedError

    def purge_history(self, older_than: str) -> Any:
        mutation = '''
        '''

        params = dict(olderThan=older_than)
        raise NotImplementedError
# endregion
