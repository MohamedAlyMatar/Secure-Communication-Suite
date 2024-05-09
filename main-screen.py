import csv
from RSA import generate_RSA_key_pair, rsa_encrypt
from MD5 import calculate_md5
from Methods_Authentication import *
from cryptography.hazmat.primitives import serialization

def welcome():
    print("-------------------------------------")
    print("Secure Communication Suite")
    print("by NRM\n")

    print("Choose the operation:")
    print("1. Sign-up")
    print("2. Sign-in")
    print("3. List Active Users")
    print("4. Send Message")
    print("5. Read Message")
    print("6. Exit")
    print("-------------------------------------")
    choice = int(input("Enter your choice (1/2/3/4/5/6):"))
    return choice


def signup():
            print("\n---> Sign-up (new)")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            hashed_password = calculate_md5(password)

            private_key_rsa, public_key_rsa = generate_RSA_key_pair()

            if save_user_data(email, hashed_password, private_key_rsa, public_key_rsa):
                print("User registration successful")
            else:
                print("User registration failed. Email already exists.")

def signin():
            print("\n---> Sign-in (already registered)")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            hashed_password = calculate_md5(password)

            if not email_exists(email):
                print("Email not found")
            elif login(email, hashed_password):
                print("Login successful")
                current_user = email
                print(current_user)
            else:
                print("Login failed")

def active():
    print("\n---> Active Users")
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        active_users = [row[0] for row in reader if row]
    for user in active_users:
        print("- " +user)

def sendmessage():
    pass

def readmessage():
    pass


def main():
    status =welcome()
    while status != 6:
        if status == 1:
            signup()
        elif status == 2:
            signin()
        elif status == 3:
            active()
        elif status == 4:
            sendmessage()
        elif status == 5:
            readmessage()        
        status = welcome()

        

if __name__ == "__main__":
    main()
