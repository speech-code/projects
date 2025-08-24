# React Note-Taking App

This is a simple note-taking application built with React, as specified by an HLC file.

## Features

- Create, view, edit, and delete notes.
- Search notes by title or content.
- Rich text editing (bold, italics, lists).
- Responsive two-panel layout.
- Optional dark mode theme.
- Data persistence using browser local storage.

## How to Run

1.  **Ensure you have Node.js and npm installed.** You can download them from [nodejs.org](https://nodejs.org/).

2.  **Navigate to the project directory** in your terminal:
    ```bash
    cd note-taking-app
    ```

3.  **Install dependencies**:
    ```bash
    npm install
    ```

4.  **Start the development server**:
    ```bash
    npm start
    ```

    This will open the application in your browser at `http://localhost:3000` (or another available port).

## Project Structure

- `public/`: Contains the public assets and `index.html`.
- `src/`:
    - `App.js`: Main application component, handling state management and overall layout.
    - `App.css`: Styling for the application.
    - `components/`:
        - `NoteList.js`: Component for displaying the list of notes.
        - `NoteEditor.js`: Component for creating and editing notes with rich text functionalities.

## Local Storage

Notes are stored locally in your browser's local storage. This means your notes will persist even if you close and reopen the browser, but they will not be synchronized across different browsers or devices.
