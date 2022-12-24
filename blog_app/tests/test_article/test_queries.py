from blog.models import Article
from blog.queries import ListArticlesQuery


def test_list_articles():
    """
    GIVEN 2 articles stored in the databases
    WHEN the execute method is called
    THEN it should return 2 articles
    """

    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article"
    ).save()

    Article(
        author="jane@doe.com",
        title="Another Article",
        content="Super awesome article"
    ).save()

    query = ListArticlesQuery()

    assert len(query.execute()) == 2