from Authentication_Methods import *

# Main code for user registration
if __name__ == "__main__":
    

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = calculate_md5(password)

    private_key_rsa, public_key_rsa = generate_RSA_key_pair()
    private_key_ecc, public_key_ecc = generate_ECC_key_pair()
    
    if save_user_data(email, hashed_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc):
        print("User registration successful")
    else:
        print("User registration failed. Email already exists.")
