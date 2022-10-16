# Wiki.Js Python client ( &#9888; WIP &#9888; )

## Examples

- Move all pages in a folder to a new folder

  ```python
  from wikijs import WikiJs

  client = WikiJs(<endpoint>, <api_key>)

  OLD_FOLDER = 'OldFolder/'
  NEW_FOLDER = 'NewFolder/'

  for page in client.search_pages('', OLD_FOLDER):
      new_path = page['path'].replace(OLD_FOLDER, NEW_FOLDER, 1)
      client.move_page(page['id'], new_path, page['locale'])
  ```
