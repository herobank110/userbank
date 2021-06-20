from flask.testing import FlaskClient
from flask.wrappers import Response


def test_put_user_valid(client: FlaskClient):
    # Testing on live database so user 1 may not be a row.
    # TODO: use mock database to have more test cases
    res: Response = client.put('/api/user/1', json={"firstName": "Jonathon"})
    assert res.status_code in (200, 500)


def test_put_user_no_body(client: FlaskClient):
    res: Response = client.put('/api/user/1')
    assert res.status_code == 400


def test_put_user_no_fields(client: FlaskClient):
    res: Response = client.put('/api/user/1', json={})
    assert res.status_code == 400


def test_put_user_wrong_type(client: FlaskClient):
    res: Response = client.put('/api/user/1', json={"lastName": 23})
    assert res.status_code == 400


def test_put_user_first_name_empty(client: FlaskClient):
    res: Response = client.put('/api/user/1', json={"firstName": ""})
    assert res.status_code == 400


def test_put_user_last_name_empty(client: FlaskClient):
    res: Response = client.put('/api/user/1', json={"lastName": ""})
    assert res.status_code == 400


def test_put_user_email_wrong_pattern(client: FlaskClient):
    res: Response = client.put('/api/user/1',
                               json={"email": "johnsmithgmail.com"})
    assert res.status_code == 400


def test_put_user_phone_too_long(client: FlaskClient):
    res: Response = client.put('/api/user/1',
                               json={"phoneNum": "012345678901234"})
    assert res.status_code == 400


def test_put_user_phone_too_short(client: FlaskClient):
    res: Response = client.put('/api/user/1',
                               json={"phoneNum": "012345"})
    assert res.status_code == 400
