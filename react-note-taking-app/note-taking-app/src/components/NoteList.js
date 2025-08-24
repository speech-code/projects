
import React from 'react';

const NoteList = ({ notes, onSelectNote, onDeleteNote }) => {
  return (
    <div className="note-list">
      <h2>Notes</h2>
      <ul>
        {notes.map(note => (
          <li key={note.id}>
            <span onClick={() => onSelectNote(note)}>{note.title}</span>
            <button onClick={() => onDeleteNote(note.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NoteList;
