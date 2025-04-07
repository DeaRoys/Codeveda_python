# Intermediate Task1 
# Initialize an empty list for tasks
tasks = []


def list_tasks():
    if not tasks:
        print("\nYour to-do list is empty!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['name']} [{status}]")
        print()


def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "done": False})
    print(f"Task '{task_name}' added!\n")


def delete_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' deleted!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def mark_task_done():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True
            print(f"Task '{tasks[task_number - 1]['name']}' marked as done!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    while True:
        print("To-Do List Application")
        print("1. List tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as done")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_done()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!\n")


if __name__ == "__main__":
    main()