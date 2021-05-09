import json

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import ethereum
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
        new_wallet = ethereum.create_ethereum_wallet()
        # Print all wallet information's
        x = json.dumps(new_wallet.dumps(), indent=4, ensure_ascii=False)
        print(x)
        y = json.loads(x)
        walletsSQL.insert(y["public_key"], y["private_key"])
        return "Hai creato un wallet con indirizzo = " + y["address"]


api.add_resource(Wallets, '/wallets')

if __name__ == '__main__':
    app.run(debug=True)
