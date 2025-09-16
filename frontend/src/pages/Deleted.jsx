import React from "react";
import NotesPage from "./NotesPage";

const Deleted = () => {
  return <NotesPage section="Deleted" filterFn={(note) => note.deleted} />;
};

export default Deleted;
