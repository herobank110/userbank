import pytest
from userbank import app as my_app

@pytest.fixture
def app():
    return my_app
