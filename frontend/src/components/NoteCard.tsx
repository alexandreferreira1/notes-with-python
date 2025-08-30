import React from "react";
import type { Note } from "../../types";

interface NoteCardProps {
  note: Note;
}

const NoteCard: React.FC<NoteCardProps> = ({ note }) => {
  return (
    <div className="note-card">
      <h3>{note.title}</h3>
      <p>{note.content}</p>
    </div>
  );
};

export default NoteCard;
