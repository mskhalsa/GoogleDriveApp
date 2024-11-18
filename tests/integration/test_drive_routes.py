import io
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_drive_controller(): # mock the drive controller for testing
    with patch("controllers.drive_controller.DriveController") as mock:
        yield mock

def test_dashboard_no_session(client): # Test to see if the route redirects to login, if no sessions
    response = client.get("/drive/dashboard")
    assert response.status_code == 302  # Redirect to login

# Test dashboard with session but no files
def test_dashboard_with_session(client, session, mock_drive_controller):
    session["credentials"] = "{}" # mock credentials
    mock_instance = mock_drive_controller.return_value
    mock_instance.list_files.return_value = [] # empty file list
    response = client.get("/drive/dashboard")
    assert response.status_code == 302

# Test file uploading functionality
def test_upload_file(client, session, mock_drive_controller):
    session["credentials"] = "{}" # mock credentials
    data = {"file": (io.BytesIO(b"test data"), "test.txt")} # mock file upload data

    response = client.post("/drive/upload", data=data, content_type="multipart/form-data")
    assert response.status_code == 302  # Redirect to dashboard after successful upload
