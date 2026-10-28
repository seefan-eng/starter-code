def format_contact(contact):
    name = contact["name"]
    phone = contact["phone"]
    email = contact["email"]
    address = contact["address"]
    return f"{name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}"

def menu():
    print("Options:\n[1] View all contacts\n[2] Add new contact\n[3] View a single contact\n[4] Remove a contact\n[5] Update a contact\n[6] Exit")

def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit():
            return int(user)
        print("Invalid input, try again!")


def add_contact(contacts, name, phone, email, address):
    pass 

def view_contact(contacts, name):
    pass

def remove_contact(contacts, name):
    pass 

def update_contact(contacts, name, value_name, new_value):
    pass 

def list_contacts(contacts):
    pass


def main():
    contacts = {}
    while True:
        menu()
        choice = num_input(">> ")
        # TODO Your code goes here
    pass 

if __name__ == "__main__":
    main()
