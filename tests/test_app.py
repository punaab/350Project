import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_creation():
    """Test that the Flask app can be created successfully"""
    assert app is not None
    assert app.name == 'app'

def test_home_endpoint(client):
    """Test that the home endpoint returns correct content"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Welcome to 350FinalProject! v1.0'

def test_integration_home(client):
    """Integration test for the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Welcome to 350FinalProject!' in response.data.decode('utf-8')

def test_home_route_exists():
    """Test that the home route exists and returns correct content"""
    with app.test_request_context('/'):
        # Test that the route exists
        assert app.url_map.bind('localhost').match('/') == ('home', {})
        
        # Test the view function directly
        from app import home
        response = home()
        assert response == 'Welcome to 350FinalProject! v1.0'