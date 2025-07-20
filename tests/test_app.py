import pytest
from src.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to 350FinalProject! v1.0' in response.data

def test_integration_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Welcome to 350FinalProject! v1.0'