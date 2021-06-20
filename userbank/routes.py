from flask import Response, jsonify, request
from psycopg2.extras import DictCursor
from userbank import app
from userbank.db_connection import db_connection


@app.route('/hi')
def get_hi():

    print('hi')
    conn = db_connection()
    with conn.cursor() as cur:
        cur.execute("select * from users;")
        rows = cur.fetchone()
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
