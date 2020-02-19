import pytest
import filesystem
import json

BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture
def client():
    filesystem.app.config['TESTING'] = True
    client = filesystem.app.test_client()
    yield client

def test_get_all(client):
    response = client.get('/')
    assert b'world' in response.data
