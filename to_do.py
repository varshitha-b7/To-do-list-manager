# To-Do List Application

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['title']}")

    elif choice == "2":
        title = input("Enter task: ")
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['title']}")

            try:
                task_num = int(input("Enter task number to mark completed: "))
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['title']}")

            try:
                task_num = int(input("Enter task number to delete: "))
                deleted = tasks.pop(task_num - 1)
                print(f"Deleted task: {deleted['title']}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")