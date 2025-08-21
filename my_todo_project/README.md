# Django Todo App

This is a simple web-based todo application built with Django, as specified by an HLC file.
It allows users to create, read, update, and delete tasks.

## Setup and Run Instructions

1. **Ensure Python and Pip are installed.**

    - You can download Python from [python.org](https://www.python.org/downloads/). Pip is usually included with Python installations.

2. **Clone the repository or navigate to the project directory.**

3. **Install Django:**

    ```bash
    pip install django
    ```

4. **Navigate into the project directory:**

    ```bash
    cd my_todo_project
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py makemigrations todo_app
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create your superuser.

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:8000/todo/` to view the todo list.
    - If you created a superuser, you can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## Features

- **Create Task:** Add new tasks to your todo list.
- **Read Tasks:** View all your tasks.
- **Update Task:** Mark tasks as completed or edit their titles.
- **Delete Task:** Remove tasks from your list.
