import pytest
from controllers.auth_controller import get_auth_url, handle_auth_callback
from unittest.mock import patch

@pytest.fixture
def mock_flow(): # Mock the flow class
    with patch("controllers.auth_controller.Flow") as mock:
        yield mock

# Test to see if the corrent auth url is generated
def test_get_auth_url(mock_flow):
    mock_instance = mock_flow.from_client_secrets_file.return_value
    mock_instance.authorization_url.return_value = ("http://mock-auth-url", None)
    auth_url = get_auth_url()
    assert auth_url == "http://mock-auth-url" # verify if mock url is returned
    mock_instance.authorization_url.assert_called_once() # check if method was called

# Test to see if callback handles the auth response correctly
def test_handle_auth_callback(mock_flow):
    mock_instance = mock_flow.from_client_secrets_file.return_value
    mock_instance.fetch_token.return_value = None # mock token fetch
    auth_response = "http://mock-auth-response"
    credentials = handle_auth_callback(auth_response)
    mock_instance.fetch_token.assert_called_once_with(authorization_response=auth_response)
    assert credentials is not None # make sure credentials is returned
