import { useEffect, useState } from "react";
import { api } from "../api";

export default function Subject({ subject, onOpenLesson, onBack }) {
  const [lessons, setLessons] = useState([]);
  const [completed, setCompleted] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([api.getLessonsBySubject(subject), api.getMyCompleted()])
      .then(([ls, comp]) => {
        setLessons(ls);
        setCompleted(comp);
      })
      .finally(() => setLoading(false));
  }, [subject]);

  const doneIds = new Set(completed.map((c) => c.lesson_id));

  if (loading) return <div className="center">Загрузка...</div>;

  return (
    <div>
      <button className="btn-ghost" onClick={onBack}>
        ← Назад
      </button>
      <h1 className="page-title">{subject}</h1>
      <div className="lesson-list">
        {lessons.map((l) => (
          <button
            key={l.id ?? l.num}
            className={`lesson-row ${doneIds.has(l.id) ? "done" : ""}`}
            onClick={() => onOpenLesson(l.num)}
          >
            <span className="lesson-num">{l.num}</span>
            <span className="lesson-name">{l.name}</span>
            <span className="lesson-type">{l.lesson_type}</span>
            {doneIds.has(l.id) && <span className="check">✓</span>}
          </button>
        ))}
      </div>
    </div>
  );
}