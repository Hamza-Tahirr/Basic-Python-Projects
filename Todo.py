tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def edit_task(task_number, new_task):
    tasks[task_number] = new_task
    print("Task edited!")

def delete_task(task_number):
    del tasks[task_number]
    print("Task deleted!")

def show_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    if not tasks:
        print("Your list is empty!")

while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Show your to-do list")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)

    elif choice == "2":
        task_number = int(input("Enter the number of the task to edit: ")) - 1
        new_task = input("Enter the new task: ")
        edit_task(task_number, new_task)

    elif choice == "3":
        task_number = int(input("Enter the number of the task to delete: ")) - 1
        delete_task(task_number)

    elif choice == "4":
        show_tasks()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-5.")
