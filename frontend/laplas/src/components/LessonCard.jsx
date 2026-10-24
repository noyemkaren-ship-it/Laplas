export default function LessonCard({ lesson, done, onClick }) {
  return (
    <button className={`lesson-row ${done ? "done" : ""}`} onClick={onClick}>
      <span className="lesson-num">{lesson.num}</span>
      <span className="lesson-name">{lesson.name}</span>
      {done && <span className="check">✓</span>}
    </button>
  );
}