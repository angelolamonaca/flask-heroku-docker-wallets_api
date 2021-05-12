from flask import Flask
from flask_restful import Resource, Api
import bitcoinwallet
import ethereumwallet
import walletsSQL
import json

app = Flask(__name__)
api = Api(app)


class CreateWallet(Resource):
    def put(self, blockchain):
        if blockchain == 'bitcoin':
            # Create Bitcoin Wallet
            new_wallet = bitcoinwallet.create_wallet()
            # Insert the wallet into the DB
            walletsSQL.insert_bitcoin_wallet(new_wallet[0], new_wallet[1], new_wallet[2])
            json_to_return = {'private_key': new_wallet[0], 'public_key': new_wallet[0], 'address': new_wallet[0]}
            print(json_to_return)
            return json_to_return

        if blockchain == 'ethereum':
            # Create Ethereum Wallet
            new_wallet = ethereumwallet.create_wallet()
            # Print all wallet information's
            x = json.dumps(new_wallet.dumps(), indent=4, ensure_ascii=False)
            # Insert the wallet into the DB
            y = json.loads(x)
            walletsSQL.insert_ethereum_wallet(y["mnemonic"], y["public_key"], y["private_key"], y["address"])
            json_to_return = {'mnemonic:': y["mnemonic"], 'public_key': y["public_key"], 'private_key': y["private_key"],'address': y["address"]}
            print(json_to_return)
            return json_to_return


api.add_resource(CreateWallet, '/createwallet/<string:blockchain>')

if __name__ == '__main__':
    app.run(debug=True)
