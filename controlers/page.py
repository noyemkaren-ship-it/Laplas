from mako.lookup import TemplateLookup
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from schemas import UserOut
from crud_repositories import LessonRepository, UserCrudRepository, TestCrudRepository
from utils.req import get_id

lookup = TemplateLookup(
    directories=["templates"],
    input_encoding="utf-8",
    output_encoding=None,
    encoding_errors="replace",
    default_filters=["str"],
)


class PageController:

    @staticmethod
    def _get_user(request: Request):
        user_id = get_id(request)
        if user_id is None:
            return None
        try:
            return UserCrudRepository.get_by_id(user_id)
        except Exception:
            return None

    def _render(self, template_name: str, context: dict) -> HTMLResponse:
        tpl = lookup.get_template(template_name)
        html = tpl.render(**context)
        if isinstance(html, bytes):
            html = html.decode("utf-8")
        return HTMLResponse(content=html)

    def root(self, request: Request):
        user = self._get_user(request)
        lessons = LessonRepository.all()
        subjects = sorted({l.subject for l in lessons})
        return self._render("index.mako", {
            "request": request,
            "user": user,
            "subjects": subjects,
            "lessons_count": len(lessons),
        })

    def lessons(self, request: Request):
        user = self._get_user(request)
        lessons = LessonRepository.all()
        subjects = sorted({l.subject for l in lessons})
        return self._render("lessons.mako", {
            "request": request,
            "user": user,
            "lessons": lessons,
            "subjects": subjects,
        })

    def lesson_detail(self, request: Request, num: int):
        user = self._get_user(request)
        try:
            lesson = LessonRepository.get_by_num(num)
        except ValueError:
            raise HTTPException(status_code=404, detail="Lesson not found")
        completed = []
        if user:
            completed = LessonRepository.get_user_completed(user_id=user.id)
        completed_ids = {c.lesson_id for c in completed}
        return self._render("lesson_detail.mako", {
            "request": request,
            "user": user,
            "lesson": lesson,
            "is_completed": num in [c.lesson_id for c in completed] or False,
            "completed_ids": completed_ids,
        })

    def tests(self, request: Request):
        user = self._get_user(request)
        tests = TestCrudRepository.get_all()
        subjects = sorted({t.subject for t in tests})
        return self._render("tests.mako", {
            "request": request,
            "user": user,
            "tests": tests,
            "subjects": subjects,
        })

    def test_by_subject(self, request: Request, subject: str):
        user = self._get_user(request)
        tests = TestCrudRepository.get_by_subject(subject)
        return self._render("tests.mako", {
            "request": request,
            "user": user,
            "tests": tests,
            "subjects": [subject],
            "active_subject": subject,
        })

    def all_subjects(self, request: Request):
        lessons = LessonRepository.all()
        subjects = sorted({l.subject for l in lessons})
        user = self._get_user(request)
        return self._render("subjects.mako", {
            "request": request,
            "user": user,
            "subjects": subjects,
        })

    def login_page(self, request: Request):
        return self._render("login.mako", {"request": request, "user": None})

    def register_page(self, request: Request):
        return self._render("register.mako", {"request": request, "user": None})

    def profile(self, request: Request):
        user = self._get_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        completed = LessonRepository.get_user_completed(user_id=user.id)
        return self._render("profile.mako", {
            "request": request,
            "user": user,
            "completed": completed,
        })