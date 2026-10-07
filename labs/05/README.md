# Lab 5: Hangman

In today's lab, we will create a simple game of Hangman. We have now covered all of the necessary concepts to create this game! Let's begin.

In this lab, we will implement the following functions, along with implementing the main function itself.

## Instructions

1. Start by implementing the get_word function. Add a number of strings into the list of words. This function should return a random word from this list of words.
2. After you have the `get_word` function done, implement the `hide_word` function. This should append an underscore as a string "_" into the list called hidden. It should then return this list at the end.
3. Now that the setup is done, we can start working on the game logic. In your main, after we print the hidden word, ask the user to input their guess.
4. Check if the user's guess is in the word using the `check_char` function. To make sure this works, implement the `check_char` function. This should simply return True if the character is in the word and return False if it is not. 
5. If the character is in the word, loop through the word using the indexes and see where the character is found in the word. Wherever it is found, pass the hidden list, guessed character, and index into the `update_hidden` function. In order for this to work, implement the `update_hidden` function next. This should take a character and replace the underscore at that index with the guessed character.
6. If the letter was not there, have the game continue without updating the hidden list.
7. When the game ends, print out what the final word was, whether the user guessed it or not.
8. Once the core functionality of the game is done, feel free to start implementing the Extra Credit portions.

## Functions written for you

As you've noticed, there are already some functions written for you. These functions are:

- word_found: This function takes in the hidden list and the original word. It will convert the hidden list into a string using the join function.
- print_hidden: This function prints out the hidden list as a string using the join function.

## Task

Implement the following functions:

- `get_word`: This function contains a list of words. Add your own words into the list. Make sure the words you're adding in contain at least 4 letters to make the game more entertaining. Once you have the list of words, return a random word from the list of words 
- `hide_word`: Given a word, you should create a list of underscore characters "_" in place of each letter. We will show the user this list as a string when they guess the word.
    - For example: "hello" should become ["_", "_", "_", "_", "_"]
- `check_char`: Given the original word and a character, return True if the character is in the original word, False if the given character is not. 
- `update_hidden`: Given the hidden list, the character, and a single index, update the hidden list at that index with the character. This should replace an "_" with the specified character.
- `main`: The main function has been setup for you but you need to finish the implementation. The user should be prompted to enter a guess. 

## Extra Credit

- [ ] Store incorrect letters: Add a way to track incorrect letters (+10)
- [ ] Play again: Allow the user to play the game again (+5)
    - [ ] Rerandomize: Playing again should rerandomize the word and reset all necessary variables (+5)
- [ ] Limit guesses: Keep a count of how many incorrect guesses the user makes, stop the game once the user runs out of guesses (+5)


