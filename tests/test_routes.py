"""
All tests will be done in an isolated flask test client but the live
database will be used.
"""

from flask.testing import FlaskClient
from flask.wrappers import Response


def test_get_api_user(client: FlaskClient):
    res: Response = client.get('/api/user')
    assert res.status_code == 200
    assert res.is_json
    assert len(res.json) == 1
    assert type(res.json['users']) == list


def test_post_api_user_valid(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 200


def test_post_api_user_missing_field(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "lastName": "Smith",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_api_user_wrong_type(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": 23,
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_api_user_first_name_empty(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_api_user_last_name_empty(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_api_user_email_wrong_pattern(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmithgmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_api_user_phone_too_long(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "012345678901234"
    })
    assert res.status_code == 400


def test_post_api_user_phone_too_short(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "012345"
    })
    assert res.status_code == 400
