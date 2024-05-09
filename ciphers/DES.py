from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from supports.files import *

# DES function
def encrypt_des(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt_des(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size).decode('utf-8')
    return plaintext

key = get_random_bytes(8)  # 8 bytes for DES key

# Read plaintext from a file and encrypt it
file_path = 'plaintext.txt'
plaintext = read_from_file(file_path)
encrypted = encrypt_des(key, plaintext)
print("Encrypted:", encrypted.hex())

# Write and save the encrypted text
encrypted_file_path = 'encrypted.txt'
write_to_file(encrypted_file_path, encrypted.hex())

# Read the decrypted text and encrypt it
encrypted_data = read_from_file(encrypted_file_path)
decrypted = decrypt_des(key, bytes.fromhex(encrypted_data))
print("Decrypted:", decrypted)
