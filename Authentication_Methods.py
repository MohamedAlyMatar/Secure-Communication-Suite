import csv  # For CSV file operations
from RSA import generate_RSA_key_pair
from ECC import generate_ECC_key_pair
from MD5 import calculate_md5  # Importing the calculate_md5 function from MD5.py

# Function to check if email exists in users.csv
def email_exists(email):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                return True
        return False

# Function to save user data to CSV file
def save_user_data(email, encrypted_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc):
    if email_exists(email):
        print("Email already exists. Please use a different email.")
        return False

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, encrypted_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc])
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
def save_user_data(email, encrypted_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc):
    if email_exists(email):
        print("Email already exists. Please use a different email.")
        return False

    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, encrypted_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc])
    return True

# Function to check user credentials during login
def login(email, password_hash):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                if row[1] == password_hash:
                    return True
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
