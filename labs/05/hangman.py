import random 

def word_found(hidden, word):
    return "".join(hidden) == word # Turns the hidden list into a string to compare

def print_hidden(hidden):
    print("".join(hidden)) # Prints the hidden list as a string

def get_word():
    words = []
    # TODO Add your own words into this list, each word should be at least 4 letters
    # TODO Get a random word from words 
    # TODO return the random word 


def hide_word(word):
    hidden = []
    
    # TODO Convert the word into a hidden version of the word 

    return hidden 

def check_char(word, char):

    # TODO return True if the character is in the original word 

    pass 


def update_hidden(hidden, char, index):

    # TODO should replace the underscore in the hidden list with the character at that given index 

    pass 

def main():
    word = get_word()
    hidden = hide_word(word)
    
    while word_found(hidden, word) == False:
        print_hidden(hidden)

        # TODO Implement the rest of the game

        # TODO Delete the pass once you finish implementing the game
        pass


if __name__ == "__main__":
    main()

