# ------ Importing necessary modules
from colorama import init, Fore, Back, Style
init()

import csv
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from ciphers.DES import *

# Function for generating the private and public keys
def generate_RSA_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# ////////// Functions for exporting and importing keys //////////

# # Export private key to a file in the private folder
# def export_private_key(private_key, username):
#     private_folder = os.path.join("private", f"{username}_private_key.pem")
#     try:
#         with open(private_folder, "wb+") as key_file:
#             key_file.write(private_key.private_bytes(
#                 encoding=serialization.Encoding.PEM,
#                 format=serialization.PrivateFormat.TraditionalOpenSSL,
#                 encryption_algorithm=serialization.NoEncryption()
#             ))
#             print(Fore.GREEN + f"Private key for {username} exported successfully." + Fore.RESET)
#     except Exception as e:
#         print(Fore.RED + f"Error exporting private key: {e}" + Fore.RESET)

# Modify export_private_key to encrypt the private key before export
def export_private_key(des_key, private_key, username):
    private_folder = os.path.join("private", f"{username}_private_key.pem")
    try:
        encrypted_private_key = des_encrypt(des_key, private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8'))  # Convert bytes to string for encryption
        with open(private_folder, "wb+") as key_file:
            key_file.write(encrypted_private_key)
        print(Fore.GREEN + f"Private key for {username} exported and encrypted successfully." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error exporting private key: {e}" + Fore.RESET)

# Export public key to PEM format
def export_public_key(public_key, username):
    public_folder = os.path.join("public", f"{username}_public_key.pem")
    try:
        with open(public_folder, "wb+") as key_file:
            key_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        print(Fore.GREEN + f"Public key for {username} exported successfully." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error exporting public key: {e}" + Fore.RESET)

# # Import private key from a file
# def import_private_key(username):
#     private_folder = os.path.join("private", f"{username}_private_key.pem")
#     try:
#         with open(private_folder, "rb") as key_file:
#             private_key = serialization.load_pem_private_key(
#                 key_file.read(),
#                 password=None
#             )
#         print(Fore.GREEN + f"Private key for {username} imported successfully." + Fore.RESET)
#         return private_key
#     except Exception as e:
#         print(Fore.RED + f"Error importing public key: {e}" + Fore.RESET)
#         return None  # Return None or handle the error as needed
    
# Modify import_private_key to decrypt the private key after import
def import_private_key(des_key, username):
    private_folder = os.path.join("private", f"{username}_private_key.pem")
    try:
        with open(private_folder, "rb") as key_file:
            encrypted_private_key = key_file.read()
        decrypted_private_key = des_decrypt(des_key, encrypted_private_key)
        private_key = serialization.load_pem_private_key(
            decrypted_private_key.encode('utf-8'),  # Convert string back to bytes for loading
            password=None
        )
        print(Fore.GREEN + f"Private key for {username} imported and decrypted successfully." + Fore.RESET)
        return private_key
    except Exception as e:
        print(Fore.RED + f"Error importing private key: {e}" + Fore.RESET)
        return None  # Return None or handle the error as needed

# Import public key from a file
def import_public_key(username):
    public_folder = os.path.join("public", f"{username}_public_key.pem")
    try:
        with open(public_folder, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read()
            )
            print(Fore.GREEN + f"Public key for {username} imported successfully." + Fore.RESET)
        return public_key
    except Exception as e:
        print(Fore.RED + f"Error importing public key: {e}" + Fore.RESET)
        return None

#  ////////// Functions for encrypting and decrypting messages /////////

# Encrypts a message using RSA encryption with OAEP padding
def rsa_encrypt(message, imported_public_key):
    ciphertext = imported_public_key.encrypt(message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # print("\nCiper text:  ", ciphertext)
    # print(len(ciphertext))
    return ciphertext

# Decrypts ciphertext using RSA decryption with OAEP padding.
def rsa_decrypt(ciphertext, imported_private_key):
    # print("\nCiper text:  ", ciphertext)
    # print(len(ciphertext))
    # print(imported_private_key)
    plaintext = imported_private_key.decrypt(ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext