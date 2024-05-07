from Authentication_Methods import *

if __name__ == "__main__":
    print("-------------------------------------")
    print("Secure Communication Suite")
    print("by NRM\n")

    print("Choose the operation:")
    print("1. Sign-up (new)")
    print("2. Sign-in (already registered)")
    print("3. Forgot/Recover password")
    print("4. Exit")
    print("-------------------------------------")

    choice = input("Enter your choice (1/2/3/4): ")
    while choice != '4':
        # --------- 1. sign-up (new) ---------
        if choice == '1':
            print("\n---> Sign-up (new)")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            hashed_password = calculate_md5(password)

            private_key_rsa, public_key_rsa = generate_RSA_key_pair()
            private_key_ecc, public_key_ecc = generate_ECC_key_pair()

            if save_user_data(email, hashed_password, private_key_rsa, public_key_rsa, private_key_ecc, public_key_ecc):
                print("User registration successful")
            else:
                print("User registration failed. Email already exists.")
        
        # --------- 2. sign-up (already registered) ---------
        elif choice == '2':  # Sign-in (already registered)
            print("\n---> Sign-in (already registered)")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            hashed_password = calculate_md5(password)

            if not email_exists(email):
                print("Email not found")
            elif login(email, hashed_password):
                print("Login successful")
            else:
                print("Login failed")
        
        # --------- 3. Forgot/Recover password ---------
        elif choice == '3':  # Forgot/Recover password
            print("\n---> Forgot/Recover password")
            email = input("Enter your email: ")
            new_password = input("Enter your new password: ")
            hashed_new_password = calculate_md5(new_password)

            if email_exists(email):
                # check if new password is different from old password
                if not check_password_match(email, hashed_new_password):
                    # Update password if new password is different from old password
                    update_password(email, hashed_new_password)
                    print("Password updated successfully")
                else:
                    print("New password cannot be the same as the old password")
            else:
                print("Email not found. Please enter a registered email.")

        # Invalid choice
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

        choice = input("Enter your choice (1/2/3/4): ")  # Ask for choice again at the end of each iteration

    print("\n!Thank you for using our Secure Communication Suite. Goodbye <3 !")
