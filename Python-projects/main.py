# to-do app

def display_menu():
    print("------- To-Do List Application --------")
    print("1. Add your task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print(".........................................\n")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(task_list):
    print("------- To-Do List Application --------")
    for index, task in enumerate(task_list, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def mark_complete(task_list):
    index = int(input("Enter the index of the task to mark as complete: ")) - 1
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid index!")

def delete_task(task_list):
    index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= index < len(task_list):
        del task_list[index]
        print("Task deleted successfully!")
    else:
        print("Invalid index!")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print("\n")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
if __name__ == "__main__":
    main()
