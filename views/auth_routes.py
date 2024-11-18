from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.auth_controller import get_auth_url, handle_auth_callback

# Define teh blueprint for the routes
auth_routes = Blueprint("auth_routes", __name__)

# Render the homepage
@auth_routes.route("/")
def index():
    return render_template("index.html")

# Redirect the user to googels OAuth 2.0 auth url
@auth_routes.route("/login")
def login():
    auth_url = get_auth_url()
    return redirect(auth_url)

# Handle the Oauth2.0 callback
@auth_routes.route("/oauth2callback")
def oauth2callback():
    credentials = handle_auth_callback(request.url)
    session["credentials"] = credentials.to_json() # save the credentials
    return redirect(url_for("drive_routes.dashboard")) # Go to the dashboard
