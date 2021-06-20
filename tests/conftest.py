"""
All tests will be done in an isolated flask test client but the live
database will be used.
"""

import pytest
from userbank import app as my_app


@pytest.fixture
def app():
    return my_app
