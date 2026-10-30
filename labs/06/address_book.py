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
    if name in contact:
        print("contact already exist")
    else:
        contacts[name] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address" address
        }
        print("contact added")

def view_contact(contacts, name):
    if name in contacts:
        print(format_contact(contacts[name]))
    else:
        print("contact not found")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("contact removed")
    else:
        print("contact not found")

def update_contact(contacts, name, value_name, new_value):
    if name in contacts:
        if value_name in contacts[name]:
            if value_name == "name":
                if new_value in contacts:
                    print("a contact with that name already exist")
                else:
                    contact = contact[name]
                    contact["name"] = new_value
                    contacts[new_value] = contact
                    del contact[name]
                    print("contact updated")
            else:
                contacts[name][value_name] = new_value
                print("contact updated")
        else:
            print("invalid field")
    else:
        print("contact not found")

def list_contacts(contacts):
    if len(contacts) == 0:
        print("there are no contacts")
    else:
        for name in contacts:
            print(format_contact(contacts[name]))
            print("---------------")


def main():
    contacts = {}
    while True:
        menu()
        choice = num_input(">> ")
        
        if choice == 1:
            list_contacts(contacts)
        elif choice  == 2:
            name = input("Enter name:")
            phone = input("Enter phone number:")
            email = input("Enter email:")
            address = input("Enter adress:")

            add_contact(contacts,name,phone,email,address)
        elif choice == 3:
            name = input("Enter the name of the contact:")
            view_contact(contact,name)

        elif choice == 4:
            name = input("Enter the name of the contact to remove")
            remove_contact(contacts,name)
        elif choice == 5:
            name = input("Enter the name of the contact to update:")
            value_name = input("what would you like to update")
            new_value = input("Enter the new value:")

            update_contact(contacts,name,value_name,new_value)
        elif choice == 6:
            print("Goodbye")
            break

        else:
            print("invalid option")

        print()

if __name__ == "__main__":
    main()
