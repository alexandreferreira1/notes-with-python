import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import { fetchCategories } from "../api/categories";

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadCategories = async () => {
      try {
        const userId = "347cc90f-c9c0-46dc-b9d0-aeb041827a1d";
        const data = await fetchCategories(userId);
        setCategories(data);
      } catch (err) {
        if (err instanceof Error) setError(err.message);
        else setError("Erro desconhecido");
      } finally {
        setLoading(false);
      }
    };

    loadCategories();
  }, []);

  if (loading) return <p>Loading categories...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="app-container">
      <Sidebar selected="Categories" />
      <div className="main-content">
        <Header />
        <div className="notes-grid">
          {categories.length > 0 ? (
            categories.map((cat) => (
              <div key={cat.id} className="note-card">
                <h3>{cat.name}</h3>
              </div>
            ))
          ) : (
            <p>No categories found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Categories;
