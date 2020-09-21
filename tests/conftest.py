import pytest


@pytest.fixture(scope="module")
def client():
    from app import app

    app.config["TESTING"] = True
    return app.test_client()