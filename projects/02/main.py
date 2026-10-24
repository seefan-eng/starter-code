def strong_password(password):
    if len(password) < 8:
        return False
    hasUpper = False
    hasLower = False
    hasDigit = False
    for char in password:
        if char.isupper():
            hasUpper = True
        elif char.islower():
            hasLower = True
        elif char.isdigit():
            hasDigit = True
    return hasUpper and hasLower and hasDigit

def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit():
            return int(user)
        print("Not a number")

def encrypt(password, shift):
    encrypted = ""
    for char in password:
        encrypted += chr(ord(char) + shift)
    return encrypted 

def login(username, password):
    stored_username = "john"
    stored_password = encrypt("super secure password", 2)
    if(stored_username == username):
        if(stored_password == encrypt(password, 2)):
            return True 
    return False 

def add_note(notes, title, description, author, label):
    # TODO Add the note to your notes
    # TODO The key is the title of the note. 
    # TODO If the note with the same title already exists, do not add it.
    pass 

def remove_note(notes, title):
    # TODO check if the title is in the notes. If it is, remove the note from notes with that title, then return True. If it isn't, return False
    pass

def view_note(notes, title):
    """
    TODO 
        check if a note with the given title is in the notes
            If it isn't, return None
        if the note contains that title, return the contents for that note as a string. It should go as follows:

        Title: {title of note}
        Description: {note description}
        Author: {author of note, this is the username for the user that created the note}
        Labels: {a list of the labels attached to the note}


    """
    pass 

def list_notes(notes):
    """
    TODO 
        print out all of the titles of the notes stored; if no notes are stored, print out a message informing the user that no notes exist yet.
    """

def menu():
    print("""
Options: 
1. Add a new note 
2. Remove a note 
3. View a note 
4. List all notes 
5. Exit the program
    """)


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    logged_in = login(username, password)
    notes = {}

    if logged_in == False:
        print("Authentication failed. Try again!")
        return

    while True:
        menu()
        choice = num_input("Enter your choice: ")
        # TODO add your checks and process the user's choice here
        # TODO This can come from Project 1
    


if __name__ == "__main__":
    main()
    # Leave this as is

