from base import Session
from schemas import Lesson as LessonSchema, LessonOut
from db_methods import create, get_all, get_by_parameter
from models import Lesson, Completed
from crud_repositories import UserCrudRepository
from sqlalchemy import select, delete as sql_delete

class LessonRepository:

    @staticmethod
    def _to_schema(l: Lesson) -> LessonSchema:
        return LessonSchema(
            name=l.name,
            subject=l.subject,
            num=l.num,
            lesson_html=l.lesson_html,
            lesson_type=l.lesson_type,
        )

    @staticmethod
    def completed(user_id: int, lesson_id: int) -> int:
        if UserCrudRepository.get_by_id(user_id) is None:
            raise ValueError(f"User {user_id} not found")
        elif LessonRepository.by_id(lesson_id) is None:
            raise ValueError(f"Lesson {lesson_id} not found")
        UserCrudRepository.update_user_xp_by_id(user_id, 5)
        new_completed = Completed(
            user_id=user_id,
            lesson_id=lesson_id
        )
        create(new_completed)
        return 5

    @staticmethod
    def get_id_by_num(num: int) -> int:
        results = get_by_parameter(Lesson, "num", num)
        if not results:
            raise ValueError(f"Lesson num={num} not found")
        return results[0].id

    @staticmethod
    def delete_by_id(lesson_id: int) -> None:
        with Session() as session:
            stmt = sql_delete(Lesson).where(Lesson.id == lesson_id)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def get_user_completed(user_id: int):
        return get_by_parameter(Completed, "user_id", user_id)

    @staticmethod
    def create(les: LessonSchema) -> LessonOut:
        new_l = Lesson(
            name=les.name,
            subject=les.subject,
            num=les.num,
            lesson_html=les.lesson_html,
            lesson_type=les.lesson_type,
        )
        create(new_l)
        return LessonOut(
            name=les.name,
            subject=les.subject,
            num=les.num,
        )

    @staticmethod
    def all() -> list[Lesson]:
        return get_all(Lesson)

    @staticmethod
    def by_subject(subject: str) -> list[Lesson]:
        return get_by_parameter(Lesson, "subject", subject)

    @staticmethod
    def by_id(lesson_id: int) -> LessonSchema:
        results = get_by_parameter(Lesson, "id", lesson_id)
        if not results:
            raise ValueError(f"Lesson {lesson_id} not found")
        return LessonRepository._to_schema(results[0])

    @staticmethod
    def get_by_num(num: int) -> LessonSchema:
        results = get_by_parameter(Lesson, "num", num)
        if not results:
            raise ValueError(f"Lesson {num} not found")
        return LessonRepository._to_schema(results[0])