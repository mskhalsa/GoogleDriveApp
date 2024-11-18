import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))  # add project directory to path
from app import create_app

@pytest.fixture
def app():
    # ensure testing config is used
    app = create_app("config.TestingConfig")
    yield app

@pytest.fixture
def client(app):
    # create a test client from the app
    return app.test_client()

@pytest.fixture
def session(client):
    # session fixture for testing
    with client.session_transaction() as session:
        yield session
