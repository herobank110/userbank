from flask import Response, jsonify, request
from userbank import app
from userbank.db_connection import db_connection


@app.route('/hi')
def get_hi():
    try:
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("select * from users;")
            rows = cur.fetchone()
    except:
        return Response(None, 500)
    res: Response = jsonify(id=rows[0])
    res.status_code = 200
    return res


@app.route('/hi/<id>')
def get_hi_id(id):
    print('hi')
    res: Response = jsonify(a=3, echo=id)
    res.status_code = 200
    return res


@app.route('/hi', methods=["POST"])
def post_hi():
    print('json', request.json)
    res = Response()
    res.status_code = 69
    return res
