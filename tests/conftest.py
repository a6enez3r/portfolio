import pytest


@pytest.fixture(scope="module")
def client():
    """
        pytest fixture that returns test
        flask client
    """
    # import flask app
    from app import app
    # set testing to true
    app.config["TESTING"] = True
    # return test client
    return app.test_client()