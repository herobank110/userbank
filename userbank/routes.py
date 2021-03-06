from userbank.db_access import (add_user, delete_user, get_all_user_ids,
                                get_user_by_id, update_user)
from flask import Response, jsonify, request
from userbank import app
from userbank.validation import (make_new_user_record, make_update_user_record,
                                 make_user_id)


@app.route('/api/user')
def get_api_user():
    if not (users := get_all_user_ids()):
        return Response('database error', 500)
    res: Response = jsonify(users=users)
    res.status_code = 200
    return res


@app.route('/api/user', methods=["POST"])
def post_api_user():
    if not (user := make_new_user_record(request)):
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
        "id": user.id_,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
        "phoneNum": user.phone_num
    })
    res.status_code = 200
    return res


@app.route('/api/user/<id_>', methods=['PUT'])
def put_api_user_id(id_: str):
    if not (user := make_update_user_record(id_, request)):
        return Response('validation failure', 400)
    if not update_user(user):
        return Response('database error', 500)
    return Response(None, 200)


@app.route('/api/user/<id_>', methods=['DELETE'])
def delete_api_user_id(id_: str):
    if not (id_int := make_user_id(id_)):
        return Response('validation failure', 400)
    if not delete_user(id_int):
        return Response('database error', 500)
    return Response(None, 200)
