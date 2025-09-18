import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NotesPage from "./pages/NotesPage";
import Favorites from "./pages/Favorites";
import Archived from "./pages/Archived";
import Deleted from "./pages/Deleted";
import Categories from "./pages/Categories";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<NotesPage section="All Notes" />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path="/archived" element={<Archived />} />
        <Route path="/deleted" element={<Deleted />} />
        <Route path="/categories" element={<Categories />} />
      </Routes>
    </Router>
  );
}

export default App;