# Address Book Lab

Today, for our lab, we are going to create a simple Address Book. This address book will store the information for various users. The key of the address book will be the name of the user. The value will consist of a nested Dictionary. This nested dictionary will contain the name of the user again, the phone number, the email, and address.

## Functions to write

- `add_contact`: This will take the original contacts dictionary and add a new contact with the given name, phone number, email, and address. The new contact will be its own dictionary instance.
- `view_contact`: This will view the information of a given contact with the given name. It may be useful to call the `format_contact` function to format the contact in a more readable form.
- `remove_contact`: This will remove the contact with a given name from the original dictionary of contacts.
- `update_contact`: This will look for the contact with a given name and update the specific field. For example, if the user wants to update the `address` of that contact, the `value_name` would be `"address"` and the `new_value` would be the new address.
- `list_contacts`: This will list out all of the contacts to view.

## Contact example

```python
contacts = {
    "john": {
        "name": "john",
        "phone": "415 123 4567",
        "email": "jdoe@gmail.com",
        "address": "1 Main Street"
    }
}
```

## Instructions

1. Start by implementing the `add_contact` function. This should take the dictionary of contacts and create a new contact. The initial key of the contact is the name of the contact. The corresponding value is a new dictionary with the name, phone, email, and address stored. See the *contact example* above.
2. Next implement the `view_contact` function. This should view the entire contact of a given contact, given the name is a valid name.
3. Implement `remove_contact` next. This will take the contacts dictionary and the name of the contact to remove. Use the `pop` function to remove a contact from the dictionary of contacts.
4. Implement the `update_contact` function next. This should take the contacts dictionary and the name of the contact. The `value_name` provided can be the `address`, `email`, or `phone` as these are the keys we want to replace the value of within the internal dictionary. Lastly, change the value at this key for the contact.
5. Lastly, implement the `list_contacts` function. This should simply list out all of the contacts

## Extra Credit Functions

- [ ] Store at least 3 other fields in the address book. Additional fields can be: secondary address, secondary email, secondary phone number, birthday, and important dates. Feel free to add other fields if you can think of any. (+10)
- [ ] Add a way of storing notes attached to the user (+5)

## Example Output

```bash

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 2
Enter a name: John Doe
Enter a phone number: 415 123-4567
Enter an email address: jdoe@email.com
Enter an address: 1 Main Street
Added contact John Doe

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 1
- John Doe

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 3
Enter the name of the user to view: John Doe
John Doe
Phone: 415 123-4567
Email: jdoe@email.com
Address: 1 Main Street

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 3
Enter the name of the user to view: jane
Invalid contact

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 2
Enter a name: Jane    
Enter a phone number: 415 987-6543
Enter an email address: jadoe@email.com
Enter an address: 2 Main Street
Added contact Jane

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 1
- John Doe
- Jane

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 4
Enter the name of the user to remove: Jane
Removed contact Jane

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 4
Enter the name of the user to remove: Jane
Invalid contact

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 5
Enter the name of the user to update: John Doe
Enter the field to update: email
Enter the new value to store: jdoe@gmail.com
Updated contact John Doe

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 3
Enter the name of the user to view: John Doe
John Doe
Phone: 415 123-4567
Email: jdoe@gmail.com
Address: 1 Main Street

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 5
Enter the name of the user to update: John Doe
Enter the field to update: none
Enter the new value to store: none

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 3
Enter the name of the user to view: John Doe
John Doe
Phone: 415 123-4567
Email: jdoe@gmail.com
Address: 1 Main Street

Options:
[1] View all contacts
[2] Add new contact
[3] View a single contact
[4] Remove a contact
[5] Update a contact
[6] Exit
>> 6
```
