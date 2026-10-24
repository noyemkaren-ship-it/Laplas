import { useAuth } from "../context/AuthContext";

export default function Navbar({ onNavigate }) {
  const { user, logout } = useAuth();
  return (
    <nav className="navbar">
      <div className="logo" onClick={() => onNavigate({ name: "home" })}>
          🧠 Laplas
        </div>
      <div className="nav-right">
        <span className="user-chip">
          👤 {user?.email || user?.name || "User"}
        </span>
        <button className="btn-ghost" onClick={logout}>
          Выйти
        </button>
      </div>
    </nav>
  );
}