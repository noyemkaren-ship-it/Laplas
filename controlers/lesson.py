from crud_repositories import LessonRepository
from schemas import Lesson as LessonSchema, LessonOut
from fastapi import Request, HTTPException
from crud_repositories import UserCrudRepository
from models import Lesson, Completed
from utils.fub_checker import FubChecker

class LessonController:
    @staticmethod
    def _get_user_id_from_request(request: Request) -> int:
        user_id = request.cookies.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        try:
            return int(user_id)
        except ValueError:
            raise HTTPException(status_code=401, detail="Invalid session")

    @staticmethod
    def _is_admin(us_id: int) -> bool:
        return UserCrudRepository.is_admin(user_id=us_id)

    @staticmethod
    def get_all() -> list[Lesson]:
        return LessonRepository.all()

    @staticmethod
    def create(request: Request, data: LessonSchema):
        fub_checker = FubChecker(data.lesson_html)

        if fub_checker.is_bad():
            raise HTTPException(status_code=400, detail="Bad request")

        fub_checker.text = data.name

        if fub_checker.is_bad():
            raise HTTPException(status_code=400, detail="Bad request")

        del fub_checker
        user_id = LessonController._get_user_id_from_request(request)
        if LessonController._is_admin(user_id):
            return LessonRepository.create(data)
        raise HTTPException(status_code=400, detail="User already exists and you are not an admin")

    @staticmethod
    def get_by_subject(subject: str) -> list[Lesson]:
        return LessonRepository.by_subject(subject=subject)

    @staticmethod
    def get_by_num(num: int) -> LessonSchema:
        return LessonRepository.get_by_num(num=num)

    @staticmethod
    def completed(request: Request, lesson_id: int):
        user_id = LessonController._get_user_id_from_request(request)
        return LessonRepository.completed(
            user_id=user_id,
            lesson_id=lesson_id
        )

    @staticmethod
    def get_all_completed(request: Request) -> list[Completed]:
        user_id = LessonController._get_user_id_from_request(request)
        return LessonRepository.get_user_completed(user_id=user_id)