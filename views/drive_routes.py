from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.drive_controller import DriveController 

# Define the blueprint for the route
drive_routes = Blueprint("drive_routes", __name__)
drive_controller = DriveController() # init the drive controller

@drive_routes.route("/dashboard")
def dashboard():
    if "credentials" not in session: # Redirect if user is not authed
        return redirect(url_for("auth_routes.login"))
    # use the drive controller with stored credentials and fetch file list
    drive_controller.initialize(session["credentials"])
    files = [file.to_dict() for file in drive_controller.list_files()]
    return render_template("dashboard.html", files=files) # Put the files on the dashboard

@drive_routes.route("/upload", methods=["POST"])
def upload():
    if "credentials" not in session: # Redirect if user is not authed
        return redirect(url_for("auth_routes.login"))
    # make sure a file is provided
    file = request.files.get("file")
    if not file or file.filename == "":
        return "No file selected", 400
    # use the drive controller and upload the file
    drive_controller.initialize(session["credentials"])
    drive_controller.upload_file(file)
    return redirect(url_for("drive_routes.dashboard")) # redirect to dashboard after upload

@drive_routes.route("/download/<file_id>")
def download(file_id):
    if "credentials" not in session: # Redirect if user is not authed
        return redirect(url_for("auth_routes.login"))
    # use the drive controller and downlaod the file
    drive_controller.initialize(session["credentials"])
    file_name, file_stream = drive_controller.download_file(file_id)
    return ( # return the download to teh user
        file_stream,
        {
            "Content-Disposition": f"attachment; filename={file_name}",
            "Content-Type": "application/octet-stream",
        },
    )

@drive_routes.route("/delete/<file_id>", methods=["POST"])
def delete(file_id):
    if "credentials" not in session: # Redirect if user is not authed
        return redirect(url_for("auth_routes.login"))
    # use the drive controller to delete file
    drive_controller.initialize(session["credentials"])
    drive_controller.delete_file(file_id)
    return redirect(url_for("drive_routes.dashboard"))

