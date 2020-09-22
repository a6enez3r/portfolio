import pytest


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_resume(client):
    response = client.get("/resume")
    assert response.status_code == 200
