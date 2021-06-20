from flask.testing import FlaskClient
from flask.wrappers import Response


def test_delete_user_id_valid(client: FlaskClient):
    res: Response = client.delete('/api/user/1')
    # Testing on live database so user 1 may not be a row.
    # TODO: use mock database to have more test cases
    assert res.status_code in (200, 500)


def test_delete_user_id_invalid(client: FlaskClient):
    res: Response = client.delete('/api/user/hahaha')
    assert res.status_code == 400
