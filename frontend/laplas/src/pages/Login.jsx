import { useState } from "react";
import { useAuth } from "../context/AuthContext";

export default function Login({ onSwitch }) {
  const { login, error } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await login(email, password);
    } catch {}
    finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <form className="auth-card" onSubmit={submit}>
        <h1>🦉 С возвращением!</h1>
        <p className="muted">Войди, чтобы продолжить обучение</p>

        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label>Пароль</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {error && <div className="error">{error}</div>}

        <button className="btn-primary" disabled={loading}>
          {loading ? "Вход..." : "Войти"}
        </button>

        <p className="switch">
          Нет аккаунта?{" "}
          <button type="button" className="link" onClick={onSwitch}>
            Регистрация
          </button>
        </p>
      </form>
    </div>
  );
}