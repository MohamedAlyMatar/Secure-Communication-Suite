from supports.authentication import *
from supports.messages import *
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


def main():
    current_user_email = None
    status = welcome()
    while status != 6:
        if status == 1:
            signup()
        elif status == 2:
            current_user_email = login()
        elif status == 3:
            active(current_user_email)
        elif status == 4:
            sendmessage(current_user_email)
        elif status == 5:
            readmessage(current_user_email)
        status = welcome()
        if status == 6:
            print("Goodbye!")
            current_user_email = None

if __name__ == "__main__":
    main()
