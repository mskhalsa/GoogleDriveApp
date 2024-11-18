import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "abc123")
    CLIENT_SECRETS_FILE = str(BASE_DIR / "client_secret.json")  # secrets
    SCOPES = ["https://www.googleapis.com/auth/drive"]

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    CLIENT_SECRETS_FILE = str(BASE_DIR / "tests" / "mock_client_secret.json")
    WTF_CSRF_ENABLED = False  # disable CSRF for testing
