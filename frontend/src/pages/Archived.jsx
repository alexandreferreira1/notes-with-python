import React from "react";
import NotesPage from "./NotesPage";

const Favorites = () => {
  return <NotesPage section="Favorites" filterFn={(note) => note.favorite} />;
};

export default Favorites;