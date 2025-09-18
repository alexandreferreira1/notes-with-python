// src/pages/Archived.jsx
import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import NoteCard from "../components/NoteCard";
import { fetchArchivedNotes } from "../api/notes";

const Archived = () => {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadArchived = async () => {
      try {
        const userId = "347cc90f-c9c0-46dc-b9d0-aeb041827a1d"; // depois puxamos dinâmico
        const data = await fetchArchivedNotes(userId);
        setNotes(data);
      } catch (err) {
        if (err instanceof Error) setError(err.message);
        else setError("Erro desconhecido");
      } finally {
        setLoading(false);
      }
    };

    loadArchived();
  }, []);

  if (loading) return <p>Loading archived notes...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="app-container">
      <Sidebar selected="Archived" />
      <div className="main-content">
        <Header />
        <div className="notes-grid">
          {notes.length > 0 ? (
            notes.map((note) => <NoteCard key={note.id} note={note} />)
          ) : (
            <p>No archived notes found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Archived;
