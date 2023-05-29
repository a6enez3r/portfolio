"""
    conftest.py: contains all pytest configurations & fixtures for testing
"""
import pytest

from portfolio.factory import create_app


@pytest.fixture(scope="session", autouse=True)
def test_client():
    """
    test app fixture
    """
    app = create_app(environment="testing")
    yield app.test_client()
