from userbank.db_access import add_user, get_all_user_ids
from flask import Response, jsonify, request
from userbank import app
from userbank.validation import make_post_user


@app.route('/api/user')
def get_api_user():
    if not (users := get_all_user_ids()):
        return Response('database error', 500)
    res: Response = jsonify(users=users)
    res.status_code = 200
    return res


@app.route('/api/user', methods=["POST"])
def post_api_user():
    if not (user := make_post_user(request)):
        return Response('validation failure', 400)
    if not add_user(user):
        return Response('database error', 500)
    return Response(None, 200)


@app.route('/api/user/<id_>')
def get_api_user_id(id_: str):
    if not id_.isnumeric():
        return Response('validation failure', 400)
    res: Response = jsonify({
        "firstName": "John",
        "lastName": "Smith",
        "email": "johnsmith@gmail.com",
        "phoneNum": "01234567890"
    })
    res.status_code = 200
    return res
