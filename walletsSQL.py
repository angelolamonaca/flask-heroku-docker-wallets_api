from flaskext.mysql import MySQL
from flask import Flask, jsonify
import os

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD', 'root')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB', 'main_schema')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'localhost')

mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()


def select_all():
    cursor.execute('select * from wallets_mysql_schema.ethereum')
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'wallets': r})


def insert(public_key, private_key):
    try:
        query = 'INSERT INTO wallets_mysql_schema.ethereum (public_key, private_key) VALUES (%s,%s)'
        t = (public_key, private_key)
        cursor.execute(query, t)
        connection.commit()
        return True
    except Exception as e:
        print("Problem inserting into db: " + str(e))
        return False
