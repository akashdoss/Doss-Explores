todo_list = []
def show_menu():
    print("\n-- To Do List Menu")
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Remove tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task")
    todo_list.append(task)
    print(f'"{task}"has been added to the list')

def view_tasks():
    if len(todo_list) == 0:
        print("your to do list is empty")
    else:
        print("\n-- To Do List --")
        for idx,task in enumerate(todo_list,1):
            print(f"{idx}.{task}")
def remove_tasks():
    view_tasks()
    if len(todo_list) > 0:
        task_num = int(input("Enter the task number to remove"))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f'"{removed_task}"has been removed from the list')
        else:
            print("Invalid task number")
while True:
    show_menu()
    choice = input("choose the option (1-4):")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_tasks()
    elif choice == '4':
        print("Exiting the to do list. Goodbye!")
    else:
        print("invalid choice! please try again")
