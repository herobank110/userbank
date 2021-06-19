from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/hi')
def hi():
    return jsonify({'a': 2, 'b': 'hello'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)