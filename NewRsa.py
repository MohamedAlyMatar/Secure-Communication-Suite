# Importing necessary modules
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa,ec

## Function for generating the private and public keys 
def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

#Encrypts a message using RSA encryption with OAEP padding
def rsa_encrypt(message_path, public_key):
    with open(message_path, "rb") as f:
        message = f.read()
    ciphertext = public_key.encrypt(message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Decrypts ciphertext using RSA decryption with OAEP padding.
def rsa_decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode("utf-8")
    return plaintext

#Testing algorithm

# Generating RSA key pair
private_key, public_key = generate_key_pair()

# Serializing and printing private key
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print("Private Key:")
print(private_key_pem.decode())

# Serializing and printing public key
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("\nPublic Key:")
print(public_key_pem.decode())

mesaage_path = r"message.txt"

encryption = rsa_encrypt(mesaage_path, public_key)
print("Encrypted message is :", encryption)

decryption = rsa_decrypt(encryption, private_key)
print("Decrypted message is :", decryption)
