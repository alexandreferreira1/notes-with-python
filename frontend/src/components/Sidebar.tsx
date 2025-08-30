import React from "react";

interface SidebarProps {
  selected: string;
  onSelect: (section: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ selected, onSelect }) => {
  const sections = ["All Notes", "Categories", "Favorites", "IA Assistant", "Archived", "Deleted"];

  return (
    <div className="sidebar">
      <h2>Notes With Python</h2>
      <ul>
        {sections.map(section => (
          <li
            key={section}
            className={selected === section ? "active" : ""}
            onClick={() => onSelect(section)}
          >
            {section}
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
