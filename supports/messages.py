import base64
from supports.authentication import *
# from main import *

def clean_byte_string(byte_str):
    if byte_str.startswith('b"') or byte_str.startswith("b'"):
        return byte_str[2:-1]
    return byte_str

import csv
import base64

# Define logincheck, import_public_key, rsa_encrypt functions if not already defined
def sendmessage(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Send Message")
        sender = current_user_email
        receiver = input("Enter recipient's email: ")
        imported_public_key = import_public_key(receiver)  # Import recipient's public key

        message = input("Enter your message: ")
        message_bytes = message.encode('utf-8')

        # Encrypt message with recipient's public key
        message_encrypted = rsa_encrypt(message_bytes, imported_public_key)

        # Base64 encode the encrypted message
        encoded_message = base64.b64encode(message_encrypted).decode()

        with open('messages.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sender, receiver, encoded_message])
        print("Message sent successfully to", receiver)

def readmessage(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Read Message")
        with open('messages.csv', mode='r') as file:
            reader = csv.reader(file)
            messages = [(row[0], row[2]) for row in reader if row[1] == current_user_email]
            
        for sender, message in messages:
            print("From:", sender)
            imported_private_key = import_private_key(current_user_email)
            try:
                msg_bytes = base64.b64decode(message)
                plaintext = rsa_decrypt(msg_bytes, imported_private_key)
                print("Message:", plaintext.decode('utf-8'))  # Decode as UTF-8
            except Exception as e:
                print("Error decoding message:", e)

def active(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Active Users")
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            active_users = [row[0] for row in reader if row]
        for user in active_users:
            print("- " + user)