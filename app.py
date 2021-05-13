from flask import Flask
from flask_restful import Resource, Api
import bitcoinwallet
import ethereumwallet
import walletsSQL

app = Flask(__name__)
api = Api(app)


class CreateWallet(Resource):
    def get(self):
        return 'Hello World'

    def put(self, blockchain):
        global json_to_return
        if blockchain == 'bitcoin':
            # Create Bitcoin Wallet
            new_wallet = bitcoinwallet.create_wallet()

            # Insert the wallet into the DB
            walletsSQL.insert_bitcoin_wallet(new_wallet[0], new_wallet[1], new_wallet[2])

            json_to_return = {'private_key': new_wallet[0], 'public_key': new_wallet[0], 'address': new_wallet[0]}
            print('Wild BITCOIN WALLET appeared!')

        if blockchain == 'ethereum':
            # Create Ethereum Wallet
            new_wallet = ethereumwallet.create_wallet()

            # Insert the wallet into the DB
            walletsSQL.insert_ethereum_wallet(new_wallet.mnemonic(), new_wallet.public_key(), new_wallet.private_key(), new_wallet.address())

            json_to_return = {'mnemonic:': new_wallet.mnemonic(), 'public_key': new_wallet.public_key(),
                              'private_key': new_wallet.private_key(), 'address': new_wallet.address()}
            print('Wild ETHEREUM WALLET appeared!')

        print(json_to_return)
        return json_to_return


api.add_resource(CreateWallet, '/createwallet/<string:blockchain>')

if __name__ == '__main__':
    app.run(debug=True)
