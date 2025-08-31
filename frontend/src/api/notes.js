export const fetchNotes = async () => {
  const res = await fetch("http://127.0.0.1:8000/notes/user/347cc90f-c9c0-46dc-b9d0-aeb041827a1d");
  if (!res.ok) {
    throw new Error("Failed to fetch notes");
  }
  const data = await res.json();
  return data;
};
