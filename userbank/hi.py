import psycopg2
from flask import Response, jsonify

from .app import app


@app.route('/hi')
def hi():
    res: Response = jsonify(a=2, b='helo')
    res.status_code = 200
    return res
