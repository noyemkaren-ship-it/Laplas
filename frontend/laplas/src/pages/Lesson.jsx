import { useEffect, useState } from "react";
import { api } from "../api";

export default function Lesson({ num, onBack, onCompleted }) {
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [completing, setCompleting] = useState(false);
  const [result, setResult] = useState(null);
  const [done, setDone] = useState(false);

  useEffect(() => {
    api.getLessonByNum(num)
      .then(setLesson)
      .catch((e) => setResult("Ошибка загрузки: " + e.message))
      .finally(() => setLoading(false));
  }, [num]);

  const complete = async () => {
    if (!lesson?.id) {
      setResult(
        "⚠️ Бэк не вернул id урока — добавь id в LessonSchema на бэке"
      );
      return;
    }
    setCompleting(true);
    try {
      const res = await api.completeLesson(lesson.id);
      setResult(typeof res === "string" ? res : "✅ XP получен!");
      setDone(true);
      onCompleted?.();
    } catch (e) {
      setResult("Ошибка: " + e.message);
    } finally {
      setCompleting(false);
    }
  };

  if (loading) return <div className="center">Загрузка...</div>;
  if (!lesson) return <div className="center">Урок не найден</div>;

  return (
    <div>
      <button className="btn-ghost" onClick={onBack}>
        ← Назад
      </button>
      <article className="lesson-article">
        <h1>{lesson.name}</h1>
        <p className="muted">
          {lesson.subject} · урок #{lesson.num} · {lesson.lesson_type}
        </p>
        <div
          className="lesson-html"
          dangerouslySetInnerHTML={{ __html: lesson.lesson_html }}
        />
      </article>

      <div className="lesson-footer">
        <button
          className={`btn-primary ${done ? "btn-done" : ""}`}
          onClick={complete}
          disabled={completing || done}
        >
          {done
            ? "✓ Урок пройден"
            : completing
            ? "..."
            : "Завершить урок"}
        </button>
        {result && <div className="result">{result}</div>}
      </div>
    </div>
  );
}