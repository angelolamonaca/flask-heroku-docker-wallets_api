from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import walletsSQL

app = Flask(__name__)
api = Api(app)


class Wallet:
    def __init__(self, publicKey, privateKey):
        self.publicKey = publicKey
        self.privateKey = privateKey


class Wallets(Resource):
    def get(self):
        return walletsSQL.select_all()

    def put(self):
        print(request.form['public_key'] + request.form['private_key'])
        return walletsSQL.insert(request.form['public_key'], request.form['private_key'])


api.add_resource(Wallets, '/wallets')

if __name__ == '__main__':
    app.run(debug=True)
