import os

from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB', '')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'localhost')
app.config['MYSQL_DATABASE_PORT'] = os.getenv('MYSQL_DATABASE_PORT', 3306)

mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()


def insert_bitcoin_wallet(private_key, public_key, address):
    try:
        query = 'INSERT INTO satoshiphyton.bitcoin (public_key, private_key, address) VALUES (%s,%s,%s)'
        t = (private_key, public_key, address)
        cursor.execute(query, t)
        connection.commit()
        return True
    except Exception as e:
        print("Problem inserting bitcoin wallet into db: " + str(e))
        return False


def insert_ethereum_wallet(mnemonic, private_key, public_key, address):
    try:
        query = 'INSERT INTO satoshiphyton.ethereum (mnemonic, private_key, public_key, address) ' \
                'VALUES (%s,%s,%s,%s)'
        t = (mnemonic, private_key, public_key, address)
        cursor.execute(query, t)
        connection.commit()
        return True
    except Exception as e:
        print("Problem inserting ethereum wallet into db: " + str(e))
        return False
