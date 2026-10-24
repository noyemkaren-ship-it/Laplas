import { useEffect, useState } from "react";
import { api } from "../api";

const EMOJI = {
  math: "🧮", математика: "🧮",
  english: "🇬🇧", английский: "🇬🇧",
  physics: "⚛️", физика: "⚛️",
  chemistry: "🧪", химия: "🧪",
  history: "📜", история: "📜",
  biology: "🧬", биология: "🧬",
  programming: "💻", программирование: "💻",
};
const DEFAULT_EMOJI = "📚";

export default function Home({ onOpenSubject }) {
  const [lessons, setLessons] = useState([]);
  const [completed, setCompleted] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    Promise.all([api.getAllLessons(), api.getMyCompleted()])
      .then(([ls, comp]) => {
        setLessons(ls);
        setCompleted(comp);
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="center">Загрузка...</div>;
  if (error) return <div className="center error">Ошибка: {error}</div>;
  if (!lessons.length) return <div className="center">Уроков пока нет 📭</div>;

  const subjects = [...new Set(lessons.map((l) => l.subject))];
  const doneIds = new Set(completed.map((c) => c.lesson_id));

  return (
    <div>
      <h1 className="page-title">Выбери предмет</h1>
      <div className="grid">
        {subjects.map((s) => {
          const subjLessons = lessons.filter((l) => l.subject === s);
          const done = subjLessons.filter((l) => doneIds.has(l.id)).length;
          const pct = subjLessons.length
            ? (done / subjLessons.length) * 100
            : 0;
          return (
            <button
              key={s}
              className="subject-card"
              onClick={() => onOpenSubject(s)}
            >
              <div className="subject-emoji">
                {EMOJI[s.toLowerCase()] || DEFAULT_EMOJI}
              </div>
              <h3>{s}</h3>
              <p className="muted">{subjLessons.length} уроков</p>
              <div className="progress">
                <div
                  className="progress-fill"
                  style={{ width: `${pct}%` }}
                />
              </div>
              <p className="small">
                {done}/{subjLessons.length} пройдено
              </p>
            </button>
          );
        })}
      </div>
    </div>
  );
}