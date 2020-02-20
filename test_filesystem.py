import pytest
import api
import os

BASE_PATH = os.environ['HOME']

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    client = api.app.test_client()
    yield client

def test_get_all(client):
    response = client.get('/',
            data=dict(path='workspace/projects/python/weave-grid/foo',
                base_path=BASE_PATH))
    assert b'bar' in response.data

def test_get_bar(client):
    response = client.get('/bar',
            data=dict(path='workspace/projects/python/weave-grid/foo',
                base_path=BASE_PATH))
    assert b'bar1' in response.data

def test_get_foo1(client):
    response = client.get('/foo1',
            data=dict(path='workspace/projects/python/weave-grid/foo',
                base_path=BASE_PATH))
    assert b'Hello foo' in response.data

def test_get_bar1(client):
    response = client.get('/bar/bar1',
            data=dict(path='workspace/projects/python/weave-grid/foo',
                base_path=BASE_PATH))
    assert b'Hello bar' in response.data
