import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import NoteCard from "../components/NoteCard";
import { fetchFavoriteNotes } from "../api/notes";

const Favorites = () => {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadNotes = async () => {
      try {
        const userId = "347cc90f-c9c0-46dc-b9d0-aeb041827a1d"; // mockado por enquanto
        const data = await fetchFavoriteNotes(userId);
        setNotes(data);
      } catch (err) {
        setError(err.message);
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
      <Sidebar selected="Favorites" onSelect={() => {}} />
      <div className="main-content">
        <Header />
        <div className="notes-grid">
          {notes.length > 0 ? (
            notes.map((note) => <NoteCard key={note.id} note={note} />)
          ) : (
            <p>No favorite notes found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Favorites;
