import csv

def add_todo(file_name):
    print("Add todo")
    todo_title = input("Enter your todo item as the title: ")
    with open(file_name, "a") as todo_file: #whenever this block finishes executing, it will close the file automatically
        writer = csv.writer(todo_file)
        writer.writerow([todo_title, "False"]) # will write this as a new row in list.csv
 
def remove_todo(file_name):
    print("Remove todo")
    view_todo(file_name)
    todo_title = input("Enter the todo item that you want to remove: ")
    todo_lists = []
    # we will read and save all the data in a list except the one that we want to remove
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader:
            if todo_title != row[0]:
                todo_lists.append(row)
    print(todo_lists)
    # we will write that down in the file again, and this will overwrite the previous list.csv
    with open(file_name, "w") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    print("Mark todo")
    view_todo(file_name)
    todo_title_done = input("Enter the todo item that you want to mark as done: ")
    todo_lists = []

    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        for row in reader:
            if todo_title_done == row[0]:
                todo_lists.append([todo_title_done,"True"])
            else:
                todo_lists.append(row)
    print(todo_lists)
    with open(file_name, "w") as todo_file:
        writer = csv.writer(todo_file)
        writer.writerows(todo_lists)


def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as todo_file:
        reader = csv.reader(todo_file)
        reader.__next__() # this function skips to the next line, can be used repeatedly
        for row in reader:
            if (row[1] == "True"):
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not completed")

