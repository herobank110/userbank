from flask import Flask, jsonify, Response
import psycopg2

app = Flask(__name__)


@app.route('/hi')
def hi():
    res: Response = jsonify(a=2, b='hello')
    res.status_code = 200
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
