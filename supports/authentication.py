import csv  # For CSV file operations
from ciphers.RSA import *
# from ciphers.ECC import generate_ECC_key_pair
from ciphers.MD5 import calculate_md5  # Importing the calculate_md5 function from MD5.py

def signup():
    print("\n---> Sign-up (new)")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = calculate_md5(password)

    private_key_rsa, public_key_rsa = generate_RSA_key_pair()
    
    export_private_key(private_key_rsa, email)
    export_public_key(public_key_rsa, email)
    print("exported private key:", private_key_rsa)
    print("exported public key:", public_key_rsa)
    
    imported_private_key = import_private_key(email)
    imported_public_key = import_public_key(email)
    print("Imported private key:", imported_private_key)
    print("fucccccccccccck")
    print("Imported public key:", imported_public_key)
    
    print("fucccccccccccck")
    imported_private_key = import_private_key(email)
    imported_public_key = import_public_key(email)
    print("Imported private key:", imported_private_key)
    print("Imported public key:", imported_public_key)

    if save_user_data(email, hashed_password, private_key_rsa, public_key_rsa):
        print("User registration successful")
    else:
        print("User registration failed. Email already exists.")

def signin():
    print("\n---> Sign-in")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = calculate_md5(password)

    if not email_exists(email):
        print("Email not found")
        return None
    elif login(email, hashed_password):
        print("Login successful")
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email:
                    rsa_private_key_str = row[2]
                    rsa_public_key_str = row[3]
                    return email, rsa_private_key_str, rsa_public_key_str 
    else:
        print("Login failed")

def logincheck(current_user_email):
    if not current_user_email:
        print("You need to sign in first.")
        return False
    return True


# Function to check if email exists in users.csv
def email_exists(email):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                return True
        return False

# Function to save user data to CSV file
def save_user_data(email, encrypted_password, private_key_rsa, public_key_rsa):
    if email_exists(email):
        print("Email already exists. Please use a different email.")
        return False

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, encrypted_password, private_key_rsa, public_key_rsa])
    return True


# Function to check if email exists in users.csv
def email_exists(email):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                return True
        return False

# Function to check user credentials during login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    password_hash = calculate_md5(password)
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                if row[1] == password_hash:
                    return email
                else:
                    return False
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