"""
    test_app.py: contains tests for pages
"""


def test_home(test_client):
    """
    test home page
    """
    # get page
    response = test_client.get("/")
    # assert response is valid
    assert response.status_code == 200


def test_about(test_client):
    """
    test about page
    """
    # get page
    response = test_client.get("/about")
    # assert response is valid
    assert response.status_code == 200


def test_resume(test_client):
    """
    test resume page
    """
    # get page
    response = test_client.get("/resume")
    # assert response is valid
    assert response.status_code == 200
