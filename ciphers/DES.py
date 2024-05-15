import os
from colorama import init, Fore, Back, Style
init()

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from supports.files import *

# DES function
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size).decode('utf-8')
    return plaintext

# Define a function to set a DES key for a user
def set_DES_key(user):
    DES_keys_folder = os.path.join("DES_keys", f"{user}_des_key.pem")
    key = get_random_bytes(8)  # 8 bytes for DES key
    try:
        with open(DES_keys_folder, "wb+") as key_file:
            key_file.write(key)
        print(Fore.GREEN + f"DES key for {user} exported successfully." + Fore.RESET)
        return key
    except Exception as e:
        print(Fore.RED + f"Error exporting DES key for {user}: {e}" + Fore.RESET)
        return None

# Define a function to get a DES key for a user
def get_DES_key(user):
    DES_keys_folder = os.path.join("DES_keys", f"{user}_des_key.pem")
    try:
        with open(DES_keys_folder, "rb") as key_file:
            key = key_file.read()
        print(Fore.GREEN + f"DES key for {user} imported successfully." + Fore.RESET)
        return key
    except Exception as e:
        print(Fore.RED + f"Error importing DES key for {user}: {e}" + Fore.RESET)
        return None

# # Read plaintext from a file and encrypt it
# file_path = 'plaintext.txt'
# plaintext = read_from_file(file_path)
# encrypted = des_encrypt(key, plaintext)
# print("Encrypted:", encrypted.hex())

# # Write and save the encrypted text
# encrypted_file_path = 'encrypted.txt'
# write_to_file(encrypted_file_path, encrypted.hex())

# # Read the decrypted text and encrypt it
# encrypted_data = read_from_file(encrypted_file_path)
# decrypted = des_decrypt(key, bytes.fromhex(encrypted_data))
# print("Decrypted:", decrypted)
