import pytest

# test to see if the index route renders correctly
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

# Test to see if the login route redirects to googles OAUth 2.0 url
def test_login_redirect(client):
    response = client.get("/login")
    assert response.status_code == 302  
    assert "Location" in response.headers # Verify if headers exists
    assert "https://accounts.google.com/o/oauth2/auth" in response.headers["Location"] # chcek url




