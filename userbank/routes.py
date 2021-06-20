from flask import Response, jsonify, request
from userbank import app
from userbank.db_connection import db_connection


@app.route('/api/user')
def get_api_user():
    try:
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("select id from users;")
            rows = cur.fetchall()
    except:
        return Response(None, 500)
    res: Response = jsonify(users=[r[0] for r in rows])
    res.status_code = 200
    return res

# @app.route('/api/user/<id>')
# def get_hi_id(id):
#     print('hi')
#     res: Response = jsonify(a=3, echo=id)
#     res.status_code = 200
#     return res


# @app.route('/hi', methods=["POST"])
# def post_hi():
#     print('json', request.json)
#     res = Response()
#     res.status_code = 69
#     return res
