# Flask Instagram Clone

This is a simplified Instagram clone application built with Flask, Python, and vanilla HTML, CSS, and JavaScript.

## Features

- User Authentication: Sign up, Login, Logout
- Content Posting: Upload photos with captions
- Content Viewing: Main feed displaying posts from followed users, individual user profiles
- Post Interactions: Like and comment on posts
- Follow System: Follow and unfollow other users
- User Search: Search for other users

## Setup and Run

Follow these steps to get the application up and running on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1.  **Clone the repository (or download the project files):**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install Flask
    ```

### Running the Application

1.  **Navigate to the project directory:**

    ```bash
    cd <project_directory>
    ```

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    You should see output similar to this, indicating the development server is running:

    ```
     * Serving Flask app 'app'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```

3.  **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

```
.
├── app.py
├── templates/
│   ├── feed.html
│   ├── signup.html
│   ├── login.html
│   ├── create_post.html
│   ├── profile.html
│   ├── search.html
│   └── search_results.html
└── static/
    └── style.css
```

-   `app.py`: The main Flask application file containing all routes and backend logic.
-   `templates/`: Contains all HTML template files rendered by Flask.
-   `static/`: Contains static files like CSS, JavaScript, and images.

## Note on Data Storage

This application uses in-memory dictionaries for user data, posts, likes, and comments. This means all data will be lost when the server restarts. For a production application, a proper database (e.g., SQLite, PostgreSQL, MySQL) would be required.

## Future Enhancements

- Integrate a real database (SQLAlchemy with SQLite/PostgreSQL).
- Implement secure password hashing.
- Enhance file upload functionality (store images on disk/cloud).
- Add more robust error handling and validation.
- Improve UI/UX.
- Implement pagination for feeds and profiles.
