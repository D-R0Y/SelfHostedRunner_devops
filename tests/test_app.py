import pytest
import requests

def test_health_endpoint():
    """Test the health endpoint of the Flask application"""
    response = requests.get('http://localhost:5000/health')
    assert response.status_code == 200
    
    data = response.json()
    assert 'status' in data
    assert data['status'] == 'healthy'

def test_home_endpoint():
    """Test the home endpoint of the Flask application"""
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    
    data = response.json()
    assert 'message' in data
    assert 'Database connected successfully!' in data['message']
