import os
import ecdsa
import hashlib
import base58

def generate_private_key():
    """
    Generate a random private key.

    Returns:
    bytes: 32-byte private key
    """
    return os.urandom(32)

def private_key_to_wif(private_key):
    """
    Convert a private key to Wallet Import Format (WIF).

    Parameters:
    private_key (bytes): 32-byte private key

    Returns:
    str: WIF-encoded private key
    """
    prefix = b"\x80"
    extended_key = prefix + private_key
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def private_key_to_public_key(private_key):
    """
    Generate a public key from a private key.

    Parameters:
    private_key (bytes): 32-byte private key

    Returns:
    bytes: 33-byte compressed public key
    """
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b"\x02" + vk.to_string()[:32] if vk.to_string()[31] < 128 else b"\x03" + vk.to_string()[:32]
    return public_key

def public_key_to_address(public_key):
    """
    Generate a Bitcoin address from a public key.

    Parameters:
    public_key (bytes): 33-byte compressed public key

    Returns:
    str: Bitcoin address
    """
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new("ripemd160", sha256_hash).digest()
    extended_key = b"\x00" + ripemd160
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    address = base58.b58encode(extended_key + checksum)
    return address.decode()

if __name__ == "__main__":
    print("=== Bitcoin Address Generator ===")
    private_key = generate_private_key()
    wif = private_key_to_wif(private_key)
    public_key = private_key_to_public_key(private_key)
    address = public_key_to_address(public_key)

    print(f"\nPrivate Key (WIF): {wif}")
    print(f"Public Key: {public_key.hex()}")
    print(f"Bitcoin Address: {address}")