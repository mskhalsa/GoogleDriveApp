import os
from google_auth_oauthlib.flow import Flow
from pathlib import Path

# allow insecure transport to aviod https
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Get secrets and define the scope.
BASE_DIR = Path(__file__).parent.parent
CLIENT_SECRETS_FILE = BASE_DIR / "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Generate the OAuth 2.0 URL
def get_auth_url():
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow.redirect_uri = "http://localhost:5002/oauth2callback"
    auth_url, _ = flow.authorization_url(
        access_type="offline",  # refresh_token is included
        prompt="consent",
    )
    return auth_url

# Handle the OAuth 2.0 callback and fetch credentials.
def handle_auth_callback(auth_response):
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow.redirect_uri = "http://localhost:5002/oauth2callback"
    flow.fetch_token(authorization_response=auth_response)
    return flow.credentials