# To-Do List Application

This module provides a simple command-line to-do list application that allows users to manage their tasks efficiently. The application supports adding, viewing, marking tasks as completed, and deleting tasks. All tasks are stored in a file for persistence.

## Functions

### `load_tasks()`

Loads tasks from the file specified by `TASKS_FILE`. If the file does not exist, it returns an empty list.

**Returns:**

- `list`: A list of tasks.

### `save_tasks(tasks)`

Saves the provided list of tasks to the file specified by `TASKS_FILE`.

**Parameters:**

- `tasks (list)`: A list of tasks to be saved.

### `add_task(tasks)`

Prompts the user to enter a new task and adds it to the provided list of tasks.

**Parameters:**

- `tasks (list)`: A list of tasks to which the new task will be added.

### `view_tasks(tasks)`

Displays all tasks in the provided list. If there are no tasks, it informs the user that no tasks are found.

**Parameters:**

- `tasks (list)`: A list of tasks to be displayed.

### `mark_task_completed(tasks)`

Prompts the user to enter the number of the task to mark as completed. It appends "(completed)" to the selected task.

**Parameters:**

- `tasks (list)`: A list of tasks from which a task will be marked as completed.

### `delete_task(tasks)`

Prompts the user to enter the number of the task to delete. It removes the selected task from the list.

**Parameters:**

- `tasks (list)`: A list of tasks from which a task will be deleted.

### `main()`

The main function that runs the to-do list application. It provides a menu for the user to choose actions such as adding, viewing, marking tasks as completed, deleting tasks, and exiting the application. It also ensures that tasks are loaded at the start and saved before exiting.

## Usage

To run the application, execute the script. The user will be presented with a menu to manage their tasks.

```sh
python todo_app.py
```

## Example

```sh
To-Do List Application
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Enter your choice: 
```

This application is a simple yet effective tool to keep track of your tasks and ensure you stay organized.
