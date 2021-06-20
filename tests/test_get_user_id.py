from flask.testing import FlaskClient
from flask.wrappers import Response


def test_get_user_id_valid(client: FlaskClient):
    res: Response = client.get('/api/user/1')
    # Testing on live database so user 1 may not be a row.
    # TODO: use mock database to have more test cases
    if res.status_code == 200:
        assert res.is_json
        assert len(res.json) == 4
        assert type(res.json['firstName']) == str
        assert type(res.json['lastName']) == str
        assert type(res.json['email']) == str
        assert type(res.json['phoneNum']) == str


def test_get_user_id_invalid(client: FlaskClient):
    res: Response = client.get('/api/user/hahaha')
    assert res.status_code == 400
