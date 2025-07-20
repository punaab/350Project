import pytest
from app import app

def test_app_creation():
    """Test that the Flask app can be created successfully"""
    assert app is not None
    assert app.name == 'app'

def test_home_route_exists():
    """Test that the home route exists and returns correct content"""
    with app.test_request_context('/'):
        # Test that the route exists
        assert app.url_map.bind('localhost').match('/') == ('home', {})
        
        # Test the view function directly
        from app import home
        response = home()
        assert response == 'Welcome to 350FinalProject! v1.0'