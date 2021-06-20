from flask.testing import FlaskClient
from flask.wrappers import Response


def test_post_user_valid(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 200


def test_post_user_no_body(client: FlaskClient):
    res: Response = client.post('/api/user')
    assert res.status_code == 400


def test_post_user_missing_field(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "lastName": "Smith",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_user_wrong_type(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": 23,
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_user_first_name_empty(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_user_last_name_empty(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_user_email_wrong_pattern(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmithgmail.com",
        "phoneNum": "01234567890"
    })
    assert res.status_code == 400


def test_post_user_phone_too_long(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "012345678901234"
    })
    assert res.status_code == 400


def test_post_user_phone_too_short(client: FlaskClient):
    res: Response = client.post('/api/user', json={
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "012345"
    })
    assert res.status_code == 400
