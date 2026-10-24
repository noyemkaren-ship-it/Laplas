import { useState } from "react";
import { useAuth } from "../context/AuthContext";

export default function Register({ onSwitch }) {
  const { register, error } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    // ⚠️ поправь поля под свою UserIn (email, password, name?)
    try {
      await register({ email, password });
    } catch {}
    finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <form className="auth-card" onSubmit={submit}>
        <h1>🚀 Создать аккаунт</h1>
        <p className="muted">Начни учиться бесплатно</p>

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
          {loading ? "Создание..." : "Зарегистрироваться"}
        </button>

        <p className="switch">
          Уже есть аккаунт?{" "}
          <button type="button" className="link" onClick={onSwitch}>
            Войти
          </button>
        </p>
      </form>
    </div>
  );
}