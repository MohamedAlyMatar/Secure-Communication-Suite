from colorama import init, Fore, Back, Style
init()

from supports.authentication import *
from supports.messages import *
from cryptography.hazmat.primitives import serialization

def welcome():
    print("_____________________________________")
    print(Style.BRIGHT + Fore.CYAN + "Secure Communication Suite" + Fore.RESET)
    print(Style.BRIGHT + Fore.CYAN + "by NRM\n" + Fore.RESET)

    print( Fore.YELLOW + "What you want to do? " + Fore.RESET)
    print("1. Sign-up")
    print("2. Sign-in")
    print("3. List Active Users")
    print("4. Send Message")
    print("5. Read Message")
    print("6. Exit")
    print("_____________________________________")
    choice = int(input(Fore.YELLOW + "Enter your choice (1/2/3/4/5/6): " + Fore.RESET))
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
            current_user_email = None
    print(Fore.CYAN + Style.BRIGHT + "Goodbye!" + Fore.RESET)

if __name__ == "__main__":
    main()
