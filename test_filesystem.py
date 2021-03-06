import pytest
import api
import os

HOME = os.environ['HOME']
path = os.path.join(HOME, 'filesystem/foo')

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    client = api.app.test_client()
    yield client

def test_get_all(client):
    response = client.get('/',
            data=dict(path=path))
    assert b'bar' in response.data

def test_get_bar(client):
    response = client.get('/bar',
            data=dict(path=path))
    assert b'bar1' in response.data

def test_get_foo1(client):
    response = client.get('/foo1',
            data=dict(path=path))
    assert b'Hello foo' in response.data

def test_get_bar1(client):
    response = client.get('/bar/bar1',
            data=dict(path=path))
    assert b'Hello bar' in response.data
