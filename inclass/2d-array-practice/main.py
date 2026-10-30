import random

def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit():
            return int(user)
        print("Not a number")

def str_to_num_list(string):
    numbers = string.split(",")
    result = [] 

    for num in numbers:
        result.append(int(num))

    return result
    

def generate_grid(n):
    grid = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append("_")
        grid.append(row)

    return grid
    

def print_grid(grid):
    for row in grind:
        for item in row:
            print(item, end="")
        print()
    
def split_parity(n):
    even = []
    odd = []

    for i in range(n):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return (even,odd)
   


def print_sequence(split_n):
    even = split_n[0]
    odd = split_n[1]

    for i in range(len(even)):
        print(even[i]), end=""

        if i < len(odd):
            print(odd[i], end="")
    

    

def sum_grid(n):
    grid = []
    rows = []
    cols = []
    total = 0

    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1,100))
        grid.append(row)

    for row in grid:
        row_sum = sum(row)
        rows.append(row_sum)

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += grid[i][j]
        cols.append(col_sum)

    for row in grid:
        for num in row:
            total += num

    return (grid,rows,cols,total)


   

def find_dupes(l):
    count = {}
    duplicates = []

    for num in l:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in counts:
        if counts[num] > 1:
            duplicates.append(num)

    return duplicates
    


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
