from colorama import init, Fore, Back, Style
init()

import csv  # For CSV file operations
from ciphers.RSA import *
# from ciphers.ECC import generate_ECC_key_pair
from ciphers.MD5 import calculate_md5  # Importing the calculate_md5 function from MD5.py

def signup():
    print(Fore.YELLOW + "\n---> Sign-up (new)" + Fore.RESET)
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = calculate_md5(password)

    if save_user_data(email, hashed_password):
        private_key_rsa, public_key_rsa = generate_RSA_key_pair()
        export_private_key(private_key_rsa, email)
        export_public_key(public_key_rsa, email)
        print(Fore.GREEN + "User registration successful" + Fore.RESET)
    else:
        print(Fore.RED + "User registration failed. Email already exists." + Fore.RESET)

def signin():
    print(Fore.YELLOW + "\n---> Sign-in" + Fore.RESET)
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    hashed_password = calculate_md5(password)

    if not email_exists(email):
        return None
    elif login(email, hashed_password):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email:
                    rsa_private_key_str = row[2]
                    rsa_public_key_str = row[3]
                    return email, rsa_private_key_str, rsa_public_key_str 
    else:
        print(Fore.RED + "Login failed" + Fore.RESET)

def logincheck(current_user_email):
    if not current_user_email:
        print(Fore.RED + "You need to sign in first." + Fore.RESET)
        return False
    return True


# Function to check if email exists in users.csv
def email_exists(email):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                return True
        print(Fore.GREEN + "Unique email" + Fore.RESET)
        return False


# Function to save user data to CSV file
def save_user_data(email, encrypted_password):
    if email_exists(email):
        return False
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, encrypted_password])
    return True

# Function to check user credentials during login
def login():
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    password_hash = calculate_md5(password)
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                if row[1] == password_hash:
                    print(Fore.GREEN + "Login successful" + Fore.RESET)
                    return email
                else:
                    print(Fore.RED + "Incorrect password. Please try again." + Fore.RESET)
                    return False
        print(Fore.RED + "User not found. Please try again." + Fore.RESET)
        return False
    


# Function to check if hashed passwords match
def check_password_match(email, hashed_password):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                if row[1] == hashed_password:
                    return True
                else:
                    print(Fore.RED + "Incorrect password. Please try again!." + Fore.RESET)
                    return False
        return False
    

# Function to update user password in users.csv
def update_password(email, new_password):
    # hashed_new_password = calculate_md5(new_password)

    rows = []
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                row[1] = new_password  # Update the hashed password
            rows.append(row)

    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True