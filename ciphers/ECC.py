from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_ECC_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


# ----- testing function

private_key, public_key = generate_ECC_key_pair()

# Serializing and printing private key
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serializing and printing public key
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

def return_decoded_ECC_key_pair():
    return private_key_pem.decode(), public_key_pem.decode()

private_key_dec, public_key_dec = return_decoded_ECC_key_pair()
# print("Private Key:", private_key_pem.decode())
# print("\nPublic Key:", public_key_pem.decode())
