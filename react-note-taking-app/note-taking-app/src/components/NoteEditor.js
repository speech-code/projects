
import React, { useState, useEffect, useRef } from 'react';

const NoteEditor = ({ note, onSaveNote }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const contentRef = useRef(null);

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setContent(note.content);
    } else {
      setTitle('');
      setContent('');
    }
  }, [note]);

  const handleSave = () => {
    onSaveNote({ ...note, title, content });
  };

  const formatText = (command, value = null) => {
    document.execCommand(command, false, value);
    setContent(contentRef.current.innerHTML);
  };

  return (
    <div className="note-editor">
      <input
        type="text"
        placeholder="Note Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <div className="toolbar">
        <button onClick={() => formatText('bold')}>Bold</button>
        <button onClick={() => formatText('italic')}>Italic</button>
        <button onClick={() => formatText('insertUnorderedList')}>List</button>
      </div>
      <div
        className="content-editable"
        contentEditable={true}
        // dangerouslySetInnerHTML={{ __html: content }}
        onInput={(e) => setContent(e.target.innerHTML)}
        ref={contentRef}
      ></div>
      <button onClick={handleSave}>Save Note</button>
    </div>
  );
};

export default NoteEditor;
