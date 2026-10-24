import { createContext, useContext, useState } from "react";
import { api } from "../api";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const raw = localStorage.getItem("user");
    return raw ? JSON.parse(raw) : null;
  });
  const [error, setError] = useState(null);

  const save = (u) => {
    setUser(u);
    localStorage.setItem("user", JSON.stringify(u));
  };

  const login = async (email, password) => {
    setError(null);
    try { const u = await api.login({ email, password }); save(u); return u; }
    catch (e) { setError(e.message); throw e; }
  };

  const register = async (data) => {
    setError(null);
    try { const u = await api.register(data); save(u); return u; }
    catch (e) { setError(e.message); throw e; }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
    // ⚠️ Если на бэке появится /user/logout — вызови api.logout()
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, error }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);