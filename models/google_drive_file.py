# Model for a googel drive file
class GoogleDriveFile:
    # init the file with its id, name, time, etc
    def __init__(self, file_id, name, mime_type=None, modified_time=None): 
        self.file_id = file_id
        self.name = name
        self.mime_type = mime_type or "Unknown"
        self.modified_time = modified_time or "Unknown"

    # Serailize the object
    def to_dict(self):
        return {
            "file_id": self.file_id,
            "name": self.name,
            "mime_type": self.mime_type,
            "modified_time": self.modified_time,
        }

    # Check if the file is an image
    def is_image(self):
        return self.mime_type.startswith("image/")

    # get the extension of the file
    def get_extension(self):
        return self.name.split(".")[-1] if "." in self.name else None
