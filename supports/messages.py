from supports.authentication import *
# from main import *

def clean_byte_string(byte_str):
    if byte_str.startswith('b"') or byte_str.startswith("b'"):
        return byte_str[2:-1]
    return byte_str

def sendmessage(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Send Message")
        sender = current_user_email
        receiver = input("Enter recipient's email: ")
        
        message = input("Enter your message: ")
        message_bytes = message.encode('utf-8')
        
        imported_public_key = import_public_key(current_user_email)
        print(current_user_email)
        print(imported_public_key)
        message = rsa_encrypt(message_bytes, imported_public_key)
        print(message)
        with open('messages.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sender, receiver, message])
        print("Message sent successfully to", receiver)

def readmessage(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Read Message")
        with open('messages.csv', mode='r') as file:
            reader = csv.reader(file)
            messages = [(row[0], row[2]) for row in reader if row[1] == current_user_email]

        for sender, message in messages:
            print("From:", sender)
            imported_private_key = import_private_key(sender)
            print("\nSender's private key: ", imported_private_key)
            
            msg = clean_byte_string(message)
            print("Message:", msg)
            message = msg.encode('utf-8')
            print("encoded message: ", message)
            
            plaintext = rsa_decrypt(message, imported_private_key)
            print("Message:", plaintext.decode())

def active(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Active Users")
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            active_users = [row[0] for row in reader if row]
        for user in active_users:
            print("- " + user)