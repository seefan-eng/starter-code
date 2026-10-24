# Project 2

Notes Functionality

## Description

Now that we've created a simple authentication system for our notes application, we'll begin adding the actual notes functionality into our project.

Upon logging in, a dictionary will store all of the notes for the user. The key for the dictionary is the title of the note. The collection of notes look like the following:

```python
{
    "First Note": {
        "title": "First Note",
        "description": "My first note",
        "author": "John Doe",
        "labels": [
            "note",
            "general"
        ]
    }
}
```

Each note will contain a title, description, author, and a list of labels.

Using the menu created in *Project 1*, the user will update the dictionary of notes.

Additionally, functions will be used for each aspect of the actual functionalities. The functions are defined for you already, you must add the implementation for the functions, calling the functions in your menu.

## New Features

- Dictionary keeping track of notes
- Functionality to Create Notes
- Functionality to Read Notes
- Functionality to Update Notes
- Functionality to Delete Notes
- Functions to simplify code basis

## Functionality

- When the user chooses to `add` a new note, multiple inputs will be asked to the user. The user will be asked to enter the title, description, and any labels. These labels will be entered as comma-separated values. These will be parsed and read into the list of labels using string functions. After creating all of the necessary values, a new note is added to the dictionary of notes. If a note with the same name exists, do not add it.
- When the user chooses to `remove` a note, the user will be asked which note they want to remove. A list of the title will be shown and the user must enter in the title of the note that they want to remove. If the title is spelled incorrectly, the program will inform the user that no such note exists. If the title exists, the note will be removed from the dictionary of notes.
- When the user chooses to `view` a note, the user will be asked to enter which note they want to view the details of. A list of the title will be shown to the user to choose from. Once they enter the title, the program will check if the title is a valid title of a note. If it is, the program will show the details of the note in a formatted-string. If the title is invalid, meaning spelled incorrectly or simply doesn't exist in the list of titles, the program informs the user that no note with that title exists.
- When the user chooses to `list` the notes, a list of all of the possible titles are shown to the user. If no notes exist, print out a message informing the user that no notes exist yet.
- When the user chooses to `exit` the program, the program ends, ending the loop.

## Topics

- Data Types
- Variables
- Conditional Statements
- Loops
- Functions
- Lists
- Strings
- Dictionaries

## Example Output

```bash
Enter your username: john
Enter your password: password

Logged in!

Options:
1. Add a new note
2. Remove a note
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 1
Enter the title of the note: Run
Enter the description of the note: Go for a run
Enter the labels; separated by commas: exercise,health 

Options:
1. Add a new note
2. Remove a note
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 1 
Enter the title of the note: Sleep early
Enter the description of the note: Sleep before midnight
Enter the labels; separated by commas: health,rest

Options:
1. Add a new note
2. Remove a note
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 3
List of notes to view: 
- Run
- Sleep early
Enter the title of the note to view: Run
Title: Run
Description: Go for a run
Author: john
Labels: ['exercise', 'health']

Options:
1. Add a new note
2. Remove a note
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
- Run
- Sleep early

Options:
1. Add a new note
2. Remove a note
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 5
Exiting...
```

## Specification

| Grade | Tasks |
| ------ | -------- |
| A+ | <ul><li>Everything from A</li><li>Code runs without errors</li><li>At least 3 additional fields for a note have been added (you decide and add to the reflection if you choose to add additional fields)</li></ul>|
| A | <ul><li>Everything from B</li><li>All functions implemented</li><li>Main implemented fully</li></ul>|
| B |<ul><li>Everything from C</li><li>3 Note functions implemented</li></ul>|
| C |<ul><li>Reflection answered fully</li><li>2 Note functions implemented</li></ul> |
| D | <ul><li>Attempt made</li><li>Reflection approached</li></ul> |
| F | No attempt made. |
