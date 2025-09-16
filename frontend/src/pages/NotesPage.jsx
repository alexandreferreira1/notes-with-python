import React, { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import NoteCard from "../components/NoteCard";
import { fetchNotes } from "../api/notes";

const NotesPage = ({ section = "All Notes", filterFn = null }) => {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadNotes = async () => {
      setLoading(true);
      try {
        const userId = "347cc90f-c9c0-46dc-b9d0-aeb041827a1d";
        const data = await fetchNotes(userId);
        setNotes(filterFn ? data.filter(filterFn) : data);
      } catch (err) {
        console.warn("Não foi possível buscar notas:", err);
        setNotes([]); // se não conseguir buscar, mostra vazio
      } finally {
        setLoading(false);
      }
    };

    loadNotes();
  }, [filterFn, section]);

  if (loading) return <p>Loading...</p>;

  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <Header />
        <div className="notes-grid">
          {notes.length > 0 ? (
            notes.map((note) => <NoteCard key={note.id} note={note} />)
          ) : (
            <p>No notes found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default NotesPage;
