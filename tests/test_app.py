
def test_home(client):
    """
        test home page
    """
    # get page
    response = client.get("/")
    # assert response is valid
    assert response.status_code == 200


def test_about(client):
    """
        test about page
    """
    # get page
    response = client.get("/about")
    # assert response is valid
    assert response.status_code == 200


def test_resume(client):
    """
        test resume page
    """
    # get page
    response = client.get("/resume")
    # assert response is valid
    assert response.status_code == 200