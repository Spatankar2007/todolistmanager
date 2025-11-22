# Intializing the main list
todo_list = []

def show_menu():
    """Display the options to the user."""
    print("\n------------------------------")
    print("    TO-DO LIST MANAGER")
    print("------------------------------")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Exit the program")
    print("------------------------------")

def add_task():
    """Prompts the user for a task and add it to the list"""
    tasks = input("Enter the task you want to add:")
    
    todo_list.append(tasks)
    print(f"Task '{tasks}' has been added !")

def view_tasks():
    """Displays all the tasks in the list. """
    if not todo_list:
        # check if the list is empty
        print("\nYour To Do list is currently empty. Add tasks!")
    else:
        print("\n===== YOUR TASKS =====")
        
        for index, tasks in enumerate(todo_list):
            print(f"{index + 1}.{tasks}")
print("======================\n")

def run_app():
    while True:
        show_menu()
        choice = input("Enter your choice (1, 2, or 3)")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("\nThanks you for using to do list manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3")

if __name__ == "__main__":
    run_app()




    
   
