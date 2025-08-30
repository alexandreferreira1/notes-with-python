import React from "react";
import SearchBar from "./SearchBar.tsx";

const Header: React.FC = () => {
  return (
    <div className="header">
      <h1>All Notes</h1>
      <SearchBar />
      <div className="icons">
        <span>🔔</span>
        <span>👤</span>
      </div>
    </div>
  );
};

export default Header;
