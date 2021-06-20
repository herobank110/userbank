from flask import Response, jsonify, request
from userbank import app, db_connection
from userbank.validation import make_post_user


@app.route('/api/user')
def get_api_user():
    try:
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("Select id from users;")
            rows = cur.fetchall()
    except:
        return Response(None, 500)
    res: Response = jsonify(users=[r[0] for r in rows])
    res.status_code = 200
    return res


@app.route('/api/user', methods=["POST"])
def post_api_user():
    if not (user := make_post_user(request)):
        return Response("validation failure", 400)
    try:
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute(
                "Insert into users (first_name, last_name, email, phone_num) "
                "values (%s, %s, %s, %s);",
                (user.first_name, user.last_name, user.email, user.phone_num))
    except:
        return Response("database error", 500)
    return Response(None, 200)
