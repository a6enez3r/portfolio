"""
    conftest.py: contains all pytest configurations & fixtures for testing
"""
# testing framework
import pytest

# api factory (function to create & configure api)
from src.factory import create_app


@pytest.fixture(scope="session", autouse=True)
def test_client():
    """
    test app fixture
    """
    # create app
    app = create_app(environment="testing")
    # yield test app client
    yield app.test_client()
