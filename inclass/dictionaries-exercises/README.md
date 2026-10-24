# Dictionaries Exercises

Today we are going to practice working with dictionaries to create three simple programs.

## Programs

- `dice_count`: We are revisiting the dice count program from our for loops problem in Lab 3. Instead of creating all of the separate variables, we will store the values in a dictionary!
- `char_occur`: We will create a dictionary to count the number of occurrences for each letter in a given string. The dictionary will contain a letter as the key and the occurrence as the value. 
- `users`: We will create a simple dictionary to keep track of users. The key will be the username and the value will be the encrypted password.

## Dice count

Roll 100 dice but keep track of the number of occurrences for each dice face in a dictionary.

## Char Occur

Create a dictionary that counts how many times each character occurs in a given string. The string will be given into the function. We will also take the string from the user input in the `main` function.

## Users

We will create a simple program that includes multiple functions to process users. We will use one dictionary throughout the program and update this dictionary of users.

### Add User

The function takes in the credentials dictionary, the username, and a password. The function should add a new username and password to the credentials dictionary.

### View Users

The function should view all of the users in the credentials dictionary. This should only give you the usernames and not the passwords.

### Delete User

This should delete the user with the given username. If the username is not in the dictionary, it should tell the user the username is invalid.

### Replace Password

This function should find the user with the specified username in the credentials dictionary. If the user exists, replace their password with the new password provided into the function. If the user does not exist, do not create a new user, instead, print out to the user that that user does not exist.

### Lookup User

This function should return the user with the specified username in the credentials dictionary, if the user exists. If a user with that username does not exist, it should return `None` instead. This function should return both the username and password.

### Main

Implement the main to run the function requested by the user from the menu. For each function, if there are parameters, ask the user to enter the necessary parameters.

## Example Output

### Dice Count

```bash
{1: 13, 2: 15, 3: 21, 4: 15, 5: 17, 6: 19}
```

### Char Occurrence

```bash
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### Users

```bash
Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 1
no users

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 2

Enter your username: Ed
Enter your password: password

User added

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 2

Enter your username: John
Enter your password: password2

User added

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 1
- Ed
- John

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 2

Enter your username: Anna
Enter your password: password3

User added

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 3

Enter the username of the user to remove: John

User deleted 

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 1
- Ed
- Anna

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 4

Enter the username to update: Anna
Enter the new password: password9

User updated

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 5
Enter the username to look up: Anna

The user is: {'Anna', 'rcuuyqtf;'}

Options:
[1] View Users
[2] Add User
[3] Remove User
[4] Update User
[5] Lookup User
[6] Exit
Choice: 6
Exiting...
```
