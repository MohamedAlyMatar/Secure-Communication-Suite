from Authentication_Methods import *

# Main code for user login
if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = calculate_md5(password)

    if not email_exists(email):
        print("Email not found")
    elif login(email, hashed_password):
        print("Login successful")
    else:
        print("Login failed")
