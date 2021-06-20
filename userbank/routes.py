from userbank.db_access import add_user, get_all_user_ids
from flask import Response, jsonify, request
from userbank import app, db_connection
from userbank.validation import make_post_user


@app.route('/api/user')
def get_api_user():
    if not (user_ids := get_all_user_ids()):
        return Response(None, 500)
    res: Response = jsonify(users=user_ids)
    res.status_code = 200
    return res


@app.route('/api/user', methods=["POST"])
def post_api_user():
    if not (user := make_post_user(request)):
        return Response("validation failure", 400)
    if not add_user(user):
        return Response("database error", 500)
    return Response(None, 200)
