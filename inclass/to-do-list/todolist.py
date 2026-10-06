def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit() == True:
            return int(user)
        else:
            print("Not a number, try again!")

def print_list(list):
    for item in list:
        print(item)

def add(list, item):
    list.append(item)


def remove(list, item):
    if item_found_in_list(list,item):
        list.remove
    else:
        print("item is not in the list")
    

def item_found_in_list(list, item):
    if item in list:
        return true
    else:
        return false
    

def index_of_item(list, item):
    if item_found_in_list(list,item):
        return list.index(item)
    else:
        return -1
    

def update_item(list, item, new_item):
    index = index_of_item(list,item)
    if index!= -1:
        list[index] = new_item
    else:
        print("item is not in the list")
     

def menu():
    print("Options: [1] View your todos\n[2] Add a todo item\n[3] Remove a todo\n[4] Update a todo\n[5] Quit")

def main():
    todo_list = []
    menu()
    """
    TODO After viewing the menu, ask the user to enter what they want to do. 
    If they choose 1, print the todo list using the print_list function
    If they choose 2, ask the user to enter the item they want to add, then add the item to the todo list using the add function
    If they choose 3, ask the user which item they want to remove, then remove that item from the todo list using the remove function
    If they choose 4, ask the user which item they want to update, ask the user what they want to change the item into, then update the item using the update_item function.


    """



if __name__ == "__main__":
    main()

