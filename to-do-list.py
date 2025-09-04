#To-Do List Application
#    Create a simple text-based to-do list app where users can add, view, and remove tasks.
# Skills learned: Lists, file I/O (for saving tasks), loops.
def display_menu():
    print("To-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")    
    print()
    choice = input("Choose an option (1-4): ")
    return choice
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(filename, tasks):        
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
def view_tasks(tasks):