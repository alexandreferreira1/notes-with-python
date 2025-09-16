const API_URL = "http://127.0.0.1:8000/notes";

export const fetchNotes = async (userId) => {
  const res = await fetch(`${API_URL}/user/${userId}`);
  if (!res.ok) throw new Error("Failed to fetch notes");
  return res.json();
};

export const fetchFavoriteNotes = async (userId) => {
  const res = await fetch(`${API_URL}/user/${userId}/favorites`);
  if (!res.ok) throw new Error("Failed to fetch favorite notes");
  return res.json();
};

export const fetchArchivedNotes = async (userId) => {
  const res = await fetch(`${API_URL}/user/${userId}/archived`);
  if (!res.ok) throw new Error("Failed to fetch archived notes");
  return res.json();
};

export const fetchDeletedNotes = async (userId) => {
  const res = await fetch(`${API_URL}/user/${userId}/deleted`);
  if (!res.ok) throw new Error("Failed to fetch deleted notes");
  return res.json();
};
