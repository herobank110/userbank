import psycopg2


def db_connection():
    if 'conn' not in globals():
        global conn
        conn = psycopg2.connect(
            user="docker",
            password="hahaha123",
            database="Users",
            host="172.10.10.2")
    return conn
