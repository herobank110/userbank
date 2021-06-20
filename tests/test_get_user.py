from flask.testing import FlaskClient
from flask.wrappers import Response


def test_get_user(client: FlaskClient):
    res: Response = client.get('/api/user')
    assert res.status_code == 200
    assert res.is_json
    assert len(res.json) == 1
    assert type(res.json['users']) == list
