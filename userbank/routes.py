from userbank.db_access import add_user, get_all_user_ids, get_user_by_id
from flask import Response, jsonify, request
from userbank import app
from userbank.validation import make_post_user, make_user_id


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
    if not (id_int := make_user_id(id_)):
        return Response('validation failure', 400)
    if not (user := get_user_by_id(id_int)):
        return Response('database error', 500)
    res: Response = jsonify({
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
        "phoneNum": user.phone_num
    })
    res.status_code = 200
    return res
