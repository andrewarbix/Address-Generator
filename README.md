# Address-Generator

Bitcoin Address Generator

Description:
> This Python script generates a Bitcoin private key, converts it to Wallet Import Format (WIF), derives the public key, and calculates the corresponding Bitcoin address. It uses the ECDSA library for key generation and Base58 encoding for the address.

Features
> Generates a random private key.
> Converts the private key to Wallet Import Format (WIF).
> Derives the compressed public key.
> Generates a Bitcoin address using SHA-256, RIPEMD-160, and Base58 encoding.

Requirements:
> Python 3.x
> ecdsa library
> base58 library

Installation:
> Clone the repository or copy the script.
> Install the required libraries: ``pip install ecdsa base58``
> Run the script: ``python bitcoin_address_generator.py``

Usage:
1. Run the script to generate a new Bitcoin private key, public key, and address.
2. The script will output:
* Private Key (WIF)
* Public Key (hexadecimal)
* Bitcoin Address (Base58)

Notes:
> This script is for educational purposes only. Do not use the generated keys for storing actual cryptocurrency.
