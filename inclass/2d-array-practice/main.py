import random

def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit():
            return int(user)
        print("Not a number")

def str_to_num_list(string):
    nums = []
    vals = string.split(",")
    for val in vals:
        if val.isdigit():
            nums.append(int(val))
    return nums

def generate_grid(n):
    """
    Generate an n x n grid with "_"s.
    return the grid after
    """
    pass

def print_grid(grid):
    """
    Using the grid from generate_grid, print out the values one row at a time:
    
    for example: grid = [['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_','_', '_']]
    this should print:
    _ _ _ _ _
    _ _ _ _ _
    _ _ _ _ _
    _ _ _ _ _
    _ _ _ _ _

    This should work for any 2D Array
    """
    pass

def split_parity(n):
    """
    Create a 2D list that contains the even numbers and odd numbers in separate inner lists.
    Go up to n (exclude n)

    For example:
    n = 10
    [ [0,2,4,6,8], [1,3,5,7,9] ]

    """
    pass


def print_sequence(split_n):
    """
    Using the split array generated in "split_parity", print out the full sequence of numbers from the alternating lists

    print_sequence([[0,2,4,6,8], [1,3,5,7,9]])
    0,1,2,3,4,5,6,7,8,9
    """
    pass

def sum_grid(n):
    """
    Create a grid of n x n random numbers between 1 and 100
    Calculate the sum of the rows, columns, and all the values.
    Return a tuple containing the grid itself, sum of the rows, cols, and all

    For example:
    sum_grid(3): 
        grid -> [[81, 96, 3], [4, 91, 52], [13, 65, 52]]
        rows = [180, 147, 130]
        cols = [98, 252, 107]
        all = 457
        returns: ([[81, 96, 3], [4, 91, 52], [13, 65, 52]], [180, 147, 130], [98, 252, 107], 457)
    """
    pass

def find_dupes(l):
    """
    Challenge: return a list with the duplicates from the list passed in as an argument.

    Example:
    l = [1,2,3,4,3,3,5,4]
    find_dupes(l) -> [3,4]

    Hint: How can we keep a count of how many times each value appears?
    """
    pass


def main():
    while True:
        print("Menu:\n[1] Generate Grid\n[2] Print Grid\n[3] Split Parity\n[4] Print Sequence from Split Parity\n[5] Sum Grid\n[6] Find Dupes\n[7] Quit")
        choice = num_input(">> ")
        if choice == 1:
            size = num_input("How large should the grid be? ")
            print(generate_grid(size))
        elif choice == 2:
            size = num_input("How large should the grid be? ")
            print_grid(generate_grid(size))
        elif choice == 3:
            n = num_input("What is the value for n? ")
            print(split_parity(n))
        elif choice == 4:
            n = num_input("What is the value for n? ")
            split = split_parity(n)
            print_sequence(split)
        elif choice == 5:
            n = num_input("What is the value for n? ")
            print(sum_grid(n))
        elif choice == 6:
            nums = input("Enter a list of numbers by separating them with commas: e,g.: 3,4,5,6: ")
            nums = str_to_num_list(nums)
            print(find_dupes(nums))
        elif choice == 7:
            break
        else:
            print("Invalid option")
        print()

if __name__ == "__main__":
    main()
