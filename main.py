# Terminal App(TO DO list)
from todo_functions import add_todo, remove_todo, mark_todo, view_todo

from colored import fg, bg, attr

print(f"{fg('blue')}{bg('yellow')}Welcome to your TODO list{attr('reset')}")

# CSV Structure
# title,    Completed
# Todo 1,   False
# Todo 2,   True
file_name = "list.csv"

# Check if list.csv exists
try:
    todo_file = open(file_name, "r") # in read mode, if the file does not exist, then it will throw an exception
    #if it exists, then all is good
    todo_file.close()
    print("We are in try block")
    # if it does not exist, then we will create the list.csv
except FileNotFoundError as e:
    todo_file = open(file_name, "w")
    todo_file.write("Title, Completed\n")
    todo_file.close()
    print("We are in except block")

# If it exists, then all fine
# If it does not exist, then we can create it.



def create_menu():
    print("1. Enter 1 to add a new item to your list!")
    print("2. Enter 2 to remove an item from your list!")
    print("3. Enter 3 to mark an item as completed on your list!")
    print("4. Enter 4 to view your TODO list!")
    print("5. Enter 5 to exit!")
    choice = input("Enter your selection: ")
    return choice

# user_choice = create_menu()
# print(user_choice)
# does not cover what happens while user choice is not 5

user_choice = "" # or you can use user_choice = str()

while user_choice != "5":
    user_choice = create_menu()

#match case is better
    if user_choice == "1": # or you can use user_choice == 1 if user_choice == str() was used
        add_todo(file_name)
    elif user_choice == "2":
        remove_todo(file_name)
    elif user_choice == "3":
        mark_todo(file_name)
    elif user_choice == "4":
        view_todo(file_name)
    elif user_choice == "5":
        continue # or you can use break
    else:
        print("Invalid input")

    input("Press Enter to continue....")

print("Thank you for using the TODO list")



