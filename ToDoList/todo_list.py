import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """"Load tasks from a file"""
    if not os.path.exists(TASKS_FILE):
        return[]

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    
def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("\n✅ No tasks available!")
        return
    
    print("\n📋 Your To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n📌 To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task Added!")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            task_num = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num] = f"✔️ {tasks[task_num]}"
                save_tasks(tasks)
                print("✅ Task marked as done!")
            else:
                print("⚠️ Invalid Task number.")

        elif choice == "4":
            display_tasks(tasks)
            task_num = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                deleted_task = tasks.pop(task_num)
                save_tasks(tasks)
                print(f"🗑️Deleted: {deleted_task}")
            else:
                print("⚠️ Invalid task number.")

        elif choice == "5":
            print("👋 Exiting... Your tasks are saved.")
            break

        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
        


