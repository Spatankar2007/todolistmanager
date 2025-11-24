# Python Command-Line To-Do List Manager

## Project Description
A simple, functional To-Do List application built purely in **Python**. This command-line utility allows users to manage their daily tasks, offering a basic interface to add, view, and exit the program.

---

##  Features

This application includes the following core functionalities:

* **Add Task (1):** Allows the user to input a new task description.
* **View Tasks (2):** Displays a numbered list of all tasks currently added.
* **Exit Program (3):** Ends the application's runtime.
* **Persistent Storage (Future Goal):** Currently, tasks are lost when the program closes. The next step is to add functionality to save and load tasks from a file (e.g., JSON).

---

## How to Run the Application

Follow these steps to get a local copy of the program running on your Windows desktop:

### Prerequisites
* You must have **Python 3** installed on your system.

### Running from Terminal

1.  **Navigate:** Open your command prompt or terminal (like the one in VS Code).
2.  **Go to the Folder:** Use the `cd` (change directory) command to navigate to your project folder (e.g., `cd todo_list_manager`).
3.  **Execute the Script:** Run the following command:

    ```bash
    python todo.py
    ```

4.  The To-Do List menu will appear, and you can start managing your tasks!

---

##  Technology Used

* **Language:** Python 3
* **Environment:** Visual Studio Code (VS Code)

---

##  Next Steps (Future Enhancements)

* Add a feature to mark tasks as **completed**.
* Implement a **save/load** feature using a file (like `tasks.json`) so tasks persist after the program is closed.
* Add a feature to **delete** tasks by number.
