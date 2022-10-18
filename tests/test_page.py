import pytest


PAGE = dict(
    title='Test Title',
    content='# Test Content',
    description='Test Description',
    editor='markdown',
    is_published=True,
    is_private=False,
    locale='en',
    path='test-folder/test',
    tags=['testag'],
)


@pytest.fixture(scope='session')
def page(client):
    from wikijs.exceptions import PageDuplicateCreate

    try:
        return client.create_page(**PAGE)
    except PageDuplicateCreate:
        raise  # TODO: delete it and create it again


def test_fetch_page(client, page, camel):
    page = client.fetch_page(page['id'])

    for field, value in PAGE.items():
        assert page[camel(field)] == value
