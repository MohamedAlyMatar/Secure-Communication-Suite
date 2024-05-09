from Methods_Authentication import *

def sendmessage(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Send Message")
        sender = current_user_email
        receiver = input("Enter recipient's email: ")
        message = input("Enter your message: ")
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
            print("Message:", message)

def active(current_user_email):
    if logincheck(current_user_email):
        print("\n---> Active Users")
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            active_users = [row[0] for row in reader if row]
        for user in active_users:
            print("- " + user)