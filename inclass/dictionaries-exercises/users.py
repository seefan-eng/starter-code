"""
Create a dictionary that stores the credentials of users. The key of the dictionary is the username and the value is the encrypted password.
"""

def encrypt(password, shift):
    updated = ""
    for char in password:
        updated += chr(ord(char) + shift)
    return updated

def menu():
    print(f"Options:\n[1] View Users\n[2] Add User\n[3] Remove User\n[4] Update User\n[5] Lookup User\n[6] Exit")

def num_input(prompt):
    while True: 
        user = input(prompt)
        if user.isdigit():
            return int(user)
        print("Not a number!")


def add_user(creds, username, password):
    # TODO: Add the user to the credentials; make sure the password is encrypted
    pass

def view_users(creds):
    # TODO: View all of the users in the credentials dictionary
    pass 

def delete_user(creds, username):
    # TODO: Delete a user from the credentials given the username
    pass 

def replace_password(creds, username, new_password):
    # TODO: Given the username and new password, update the user in the credentials dictionary
    pass

def lookup_user(creds, username):
    # TODO : Given the username, lookup the user in the credentials dictionary. If no user with that username exists, return None
    pass

def main():
    users = {}
    while True:
        menu()
        choice = num_input("Choice: ")
    # TODO 

if __name__ == "__main__":
    main()
