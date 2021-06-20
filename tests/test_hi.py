from flask.testing import FlaskClient
from flask.wrappers import Response


def test_add():
    assert 2 + 2 == 4


def test_get_hi(client: FlaskClient):
    res: Response = client.get('/hi')
    assert res.json == {'a': 3}
    assert res.status_code == 200
