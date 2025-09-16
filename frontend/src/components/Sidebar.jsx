import { NavLink } from "react-router-dom";

const sections = [
  { name: "All Notes", path: "/" },
  { name: "Categories", path: "/categories" },
  { name: "Favorites", path: "/favorites" },
  { name: "IA Assistant", path: "/assistant" },
  { name: "Archived", path: "/archived" },
  { name: "Deleted", path: "/deleted" },
];

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Notes With Python</h2>
      <ul>
        {sections.map((s) => (
          <li key={s.name}>
            <NavLink
              to={s.path}
              className={({ isActive }) => (isActive ? "active" : "")}
              end={s.path === "/"} // para que '/' seja casado apenas exatamente
            >
              {s.name}
            </NavLink>
          </li>
        ))}
      </ul>

      <div className="upgrade">
        <p>Upgrade To Pro</p>
        <button>Upgrade</button>
      </div>

      <div className="settings">
        <p>Settings</p>
        <p>Contact Us</p>
      </div>
    </div>
  );
};

export default Sidebar;
