import React, { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import NoteCard from "../components/NoteCard";
import type { Note } from "../../types";

const AllNotes: React.FC = () => {
  const [selectedSection, setSelectedSection] = useState("All Notes");
  const [notes, setNotes] = useState<Note[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadNotes = async () => {
      try {
        const userId = "347cc90f-c9c0-46dc-b9d0-aeb041827a1d";
        const res = await fetch(`http://127.0.0.1:8000/notes/user/${userId}`);

        if (!res.ok) {
          throw new Error(`Erro ao buscar notas: ${res.status} ${res.statusText}`);
        }

        const data: Note[] = await res.json();
        setNotes(data);
      } catch (err: unknown) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("Erro desconhecido");
        }
      } finally {
        setLoading(false);
      }
    };

    loadNotes();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="app-container">
      <Sidebar selected={selectedSection} onSelect={setSelectedSection} />
      <div className="main-content">
        <Header />
        <div className="notes-grid">
          {notes.map(note => (
            <NoteCard key={note.id} note={note} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default AllNotes;
