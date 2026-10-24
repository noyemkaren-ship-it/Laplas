from fastapi import APIRouter, Request
from controlers import LessonController
from models import Lesson
from schemas import Lesson as LessonSchema, LessonOut, CompletedSchema

router = APIRouter(prefix="/lesson", tags=["Lesson"])

@router.get("/all_lessons")
async def get_all_lessons():
    return LessonController.get_all()

@router.get("/lesson/{num}")
async def get_lesson_by_num(num: int):
    return LessonController.get_by_num(num)

@router.post("/lesson", response_model=LessonOut)
async def create_lesson(lesson: LessonSchema, request: Request):
    return LessonController.create(request, lesson)

@router.get("/subject/{subject}")
async def get_all_by_subject(subject: str):
    return LessonController.get_by_subject(subject)

@router.post("/completed_lesson")
async def completed_lesson_api(completed_lesson: CompletedSchema, request: Request):
    result = LessonController.completed(
        request,
        completed_lesson.lesson_id
    )
    return f"xp: {result}"

@router.get("/my_completed_lesson")
async def completed_lessons(request: Request):
    return LessonController.get_all_completed(request)
