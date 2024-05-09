import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Function for generating the private and public keys
def generate_RSA_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Export private key to a file in the private folder
def export_private_key(private_key, username):
    private_folder = os.path.join("private", f"{username}_private_key.pem")
    with open(private_folder, "wb") as key_file:
        key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

# Export public key to a file in the public folder
def export_public_key(public_key, username):
    public_folder = os.path.join("public", f"{username}_public_key.pem")
    with open(public_folder, "wb") as key_file:
        key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Import private key from a file
def import_private_key(username):
    private_folder = os.path.join("private", f"{username}_private_key.pem")
    with open(private_folder, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    return private_key

# Import public key from a file
def import_public_key(username):
    public_folder = os.path.join("public", f"{username}_public_key.pem")
    with open(public_folder, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return public_key

# Generate key pair
# private_key, public_key = generate_RSA_key_pair()

# Export keys to files in folders
# export_private_key(private_key, "user1")
# export_public_key(public_key, "user1")

# Import keys from files in folders
imported_private_key = import_private_key("omar")
imported_public_key = import_public_key("omar")

# Test the import/export
print("\nImported private key:", imported_private_key)
print("\nImported public key:", imported_public_key)

# Sample message to encrypt
message = "Hello, this is a sample message."
message_bytes = message.encode('utf-8')

def rsa_encrypt(message, imported_public_key):
    ciphertext = imported_public_key.encrypt(message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\nCiper text:  ", ciphertext)
    return ciphertext

# Decrypts ciphertext using RSA decryption with OAEP padding.
def rsa_decrypt(ciphertext, imported_private_key):
    print("\nCiper text:  ", ciphertext)
    print(imported_private_key)
    plaintext = imported_private_key.decrypt(ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext


ciphertext = rsa_encrypt(message_bytes, imported_public_key)
print("\n\nEncrypted message:", ciphertext)

# Decrypt the message using the private key
print(imported_private_key)

decrypted_message = rsa_decrypt(ciphertext, imported_private_key)
print("\n\nDecrypted message:", decrypted_message.decode())
