from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload, MediaIoBaseUpload
import io
from models.google_drive_file import GoogleDriveFile

# This is the controller to manage teh operations on Google Drive.
class DriveController:
    def __init__(self):
        self.service = None # init the service

    # init with credentials
    def initialize(self, credentials_json):
        from google.oauth2.credentials import Credentials
        credentials = Credentials.from_authorized_user_info(eval(credentials_json))
        self.service = build("drive", "v3", credentials=credentials)

    # Get all files in the drive
    def list_files(self):
        response = self.service.files().list(
            q="mimeType != 'application/vnd.google-apps.folder'", # dont get folders
            pageSize=100,
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)"
        ).execute()
        return [ # Convert these responses to a list
            GoogleDriveFile(
                file["id"],
                file["name"],
                file["mimeType"],
                file["modifiedTime"]
            )
            for file in response.get("files", [])
        ]

    # To upload a file
    def upload_file(self, file):
        file_metadata = {"name": file.filename}
        media = MediaIoBaseUpload(file, mimetype=file.content_type, resumable=True)
        self.service.files().create(body=file_metadata, media_body=media, fields="id").execute()

    # To upload a file
    def download_file(self, file_id):
        file_metadata = self.service.files().get(fileId=file_id, fields="name").execute() # Get teh metadata
        file_name = file_metadata["name"]

        # Initiate the download
        request = self.service.files().get_media(fileId=file_id)
        file_stream = io.BytesIO()
        downloader = MediaIoBaseDownload(file_stream, request)

        done = False
        while not done:
            _, done = downloader.next_chunk() # Get the file in chunks

        file_stream.seek(0)
        return file_name, file_stream

    # To delete a file
    def delete_file(self, file_id):
        self.service.files().delete(fileId=file_id).execute()
