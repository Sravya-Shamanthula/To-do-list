# TO-DO LIST APP

todo = []


def show_menu():
    print("\n========== TO-DO MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")


def add_task():
    task = input("Enter task: ").strip()

    if task:
        todo.append(task)
        print("✅ Task added successfully!")
    else:
        print("⚠ Task cannot be empty.")


def view_tasks():
    if not todo:
        print("📭 No tasks available.")
        return

    print("\n📋 Your Tasks:")
    for index, task in enumerate(todo, start=1):
        print(f"{index}. {task}")


def delete_task():
    if not todo:
        print("❌ No tasks to delete.")
        return

    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(todo):
            removed = todo.pop(num - 1)
            print(f"🗑 Deleted: {removed}")
        else:
            print("⚠ Invalid task number.")

    except ValueError:
        print("⚠ Please enter a valid number.")


# Main Program
while True:
    show_menu()

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("👋 Exiting TO-DO App. Goodbye!")
        break

    else:
        print("⚠ Invalid option. Please choose between 1 and 4.")