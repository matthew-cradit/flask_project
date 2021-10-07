import os 
import pytest

from web_app import app

def test_connection():

    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World!</p>'
