import pytest
from fastapi import status


def test_get_root(client):
    """Test GET / redirects to /static/index.html"""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities(client, mock_activities):
    """Test GET /activities returns all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert data == mock_activities
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data


def test_signup_success(client):
    """Test POST /signup adds a participant"""
    response = client.post(
        "/activities/Programming%20Class/signup?email=newstudent@mergington.edu"
    )
    assert response.status_code == 200
    result = response.json()
    assert "Signed up newstudent@mergington.edu" in result["message"]


def test_unregister_success(client):
    """Test DELETE /unregister removes a participant"""
    response = client.delete(
        "/activities/Chess%20Club/unregister?email=michael@mergington.edu"
    )
    assert response.status_code == 200
    result = response.json()
    assert "Unregistered michael@mergington.edu" in result["message"]
