from flask import Response, jsonify, request
from userbank import app


@app.route('/hi')
def get_hi():
    res: Response = jsonify(a=3)
    res.status_code = 200
    return res


@app.route('/hi/<id>')
def get_hi_id(id):
    res: Response = jsonify(a=3, echo=id)
    res.status_code = 200
    return res


@app.route('/hi', methods=["POST"])
def post_hi():
    print('json', request.json)
    res = Response()
    res.status_code = 69
    return res
