"""
    test_app.py: contains tests for pages
"""
from unittest import mock


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
    with mock.patch("src.bps.pages.github_content", return_value=[]):
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
