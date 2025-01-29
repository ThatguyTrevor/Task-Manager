tasks = []


# Function to display the menu
def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


# Function to add a task
def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added!")


# Function to view all tasks
def view_tasks():
    if tasks:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")


# Function to delete a task
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        task_index = int(input(f"Enter the task number to delete (1 to {len(tasks)}): ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main program loop
def main():
    print("Welcome to the Task Manager!")

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()