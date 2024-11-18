from models.google_drive_file import GoogleDriveFile

# Test the to_dict method
def test_google_drive_file_to_dict():
    drive_file = GoogleDriveFile("file1", "test.txt", "text/plain", "2024-11-17")
    file_dict = drive_file.to_dict() # to_dict happens here
    # assertions to verify the contents
    assert file_dict["file_id"] == "file1"
    assert file_dict["name"] == "test.txt"
    assert file_dict["mime_type"] == "text/plain"
    assert file_dict["modified_time"] == "2024-11-17"

# Test the is_image method for image files
def test_google_drive_file_is_image():
    drive_file = GoogleDriveFile("file2", "image.jpg", "image/jpeg")
    assert drive_file.is_image() # Verify is true for images

    drive_file = GoogleDriveFile("file3", "document.pdf", "application/pdf")
    assert not drive_file.is_image() # verify false for non images
