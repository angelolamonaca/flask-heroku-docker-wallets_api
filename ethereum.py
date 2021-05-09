from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy


def create_ethereum_wallet():
    # 128 strength entropy
    entropy = generate_entropy(strength=128)
    # Secret passphrase
    passphrase = None  # str("meherett")
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese & korean
    language = "italian"  # default is english

    # Initialize wallet
    wallet = Wallet()
    # Get Ethereum wallet from entropy
    wallet.from_entropy(entropy=entropy, passphrase=passphrase, language=language)

    # Derivation from path
    # wallet.from_path("m/44'/60'/0'/0/0'")
    # Or derivation from index
    wallet.from_index(44, harden=True)
    wallet.from_index(60, harden=True)
    wallet.from_index(0, harden=True)
    wallet.from_index(0)
    wallet.from_index(0, harden=True)

    return wallet
