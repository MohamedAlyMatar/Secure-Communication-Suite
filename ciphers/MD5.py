import hashlib
from supports.files import *

def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

# ----- testing algorithm
# file_path = 'text.txt'
# plaintext = read_from_file(file_path)
# print("Before hashing:", plaintext)
# md5_hash = calculate_md5(plaintext)

# hashed_file_path = 'hashedtext.txt'
# write_to_file(hashed_file_path, md5_hash)
# print("After hashing:", md5_hash)