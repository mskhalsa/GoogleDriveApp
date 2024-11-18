import pytest
from unittest.mock import patch, MagicMock
from controllers.drive_controller import DriveController

@pytest.fixture
def mock_service(): # Mock the drive api service builder
    with patch("controllers.drive_controller.build") as mock:
        yield mock

# test the list files method of drive controller
def test_list_files(mock_service):
    mock_drive_service = MagicMock()
    mock_service.return_value = mock_drive_service # mock the service returned by build
    mock_drive_service.files.return_value.list.return_value.execute.return_value = {
        "files": [ # this is a mock file returned by the drive api
            {"id": "file1", "name": "test1.txt", "mimeType": "text/plain", "modifiedTime": "2024-11-17T00:00:00Z"}
        ]
    }

    drive_controller = DriveController()
    drive_controller.service = mock_drive_service 
    files = drive_controller.list_files() # call teh list files method
    assert len(files) == 1 # make sure files are returned
    assert files[0].name == "test1.txt" # verifying the file name
