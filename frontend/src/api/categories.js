const API_URL = "http://127.0.0.1:8000/categories";

export const fetchCategories = async (userId) => {
  const res = await fetch(`${API_URL}?user_id=${userId}`);
  if (!res.ok) throw new Error("Failed to fetch categories");
  return await res.json();
};