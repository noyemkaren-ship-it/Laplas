from mako.lookup import TemplateLookup
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from crud_repositories import LessonRepository, UserCrudRepository, TestCrudRepository
from utils.req import get_id
from utils.fub_checker import FubChecker
from schemas import Lesson as LessonSchema, TestSchema
from db_methods import get_by_parameter
from models import Lesson, Test, Completed

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

    def _require_admin(self, request: Request):
        user = self._get_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        if not user.admin:
            raise HTTPException(status_code=403, detail="Access denied: not an admin")
        return user

    # ---------- public pages ----------

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
            lesson_db_id = LessonRepository.get_id_by_num(num)
        except ValueError:
            raise HTTPException(status_code=404, detail="Lesson not found")

        is_completed = False
        if user:
            completed = LessonRepository.get_user_completed(user_id=user.id)
            is_completed = any(c.lesson_id == lesson_db_id for c in completed)

        return self._render("lesson_detail.mako", {
            "request": request,
            "user": user,
            "lesson": lesson,
            "is_completed": is_completed,
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
            "active_subject": None,
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

    def admin_panel(self, request: Request):
        admin = self._require_admin(request)
        lessons = LessonRepository.all()
        tests = TestCrudRepository.get_all()
        users = UserCrudRepository.get_all(user_id=admin.id)

        return self._render("admin_panel.mako", {
            "request": request,
            "user": admin,
            "lessons": lessons,
            "tests": tests,
            "users": users,
            "active_tab": request.query_params.get("tab", "lessons"),
        })

    def admin_lesson_form(self, request: Request):
        admin = self._require_admin(request)
        return self._render("admin_lesson_form.mako", {
            "request": request,
            "user": admin,
            "error": None,
            "form": {},
        })

    async def admin_lesson_create(self, request: Request):
        admin = self._require_admin(request)
        form = await request.form()

        name = (form.get("name") or "").strip()
        subject = (form.get("subject") or "").strip()
        num_raw = (form.get("num") or "").strip()
        lesson_html = form.get("lesson_html") or ""
        lesson_type = (form.get("lesson_type") or "text").strip()

        error = None
        if not name:
            error = "Name is required"
        elif not subject:
            error = "Subject is required"
        elif not num_raw.isdigit():
            error = "Num must be a positive integer"
        elif not lesson_html.strip():
            error = "Lesson HTML is required"

        if not error:
            fub = FubChecker(lesson_html)
            if fub.is_bad():
                error = "Lesson HTML contains forbidden content"
            else:
                fub.text = name
                if fub.is_bad():
                    error = "Lesson name contains forbidden content"

        if not error and get_by_parameter(Lesson, "num", int(num_raw)):
            error = f"Lesson with num={num_raw} already exists"

        if error:
            return self._render("admin_lesson_form.mako", {
                "request": request,
                "user": admin,
                "error": error,
                "form": {
                    "name": name,
                    "subject": subject,
                    "num": num_raw,
                    "lesson_html": lesson_html,
                    "lesson_type": lesson_type,
                },
            })

        LessonRepository.create(LessonSchema(
            name=name,
            subject=subject,
            num=int(num_raw),
            lesson_html=lesson_html,
            lesson_type=lesson_type,
        ))
        return RedirectResponse("/admin_panel?tab=lessons", status_code=303)

    def admin_test_form(self, request: Request):
        admin = self._require_admin(request)
        return self._render("admin_test_form.mako", {
            "request": request,
            "user": admin,
            "error": None,
            "form": {},
        })

    async def admin_test_create(self, request: Request):
        admin = self._require_admin(request)
        form = await request.form()

        subject = (form.get("subject") or "").strip()
        question = (form.get("question") or "").strip()
        answer = (form.get("answer") or "").strip()

        error = None
        if not subject:
            error = "Subject is required"
        elif not question:
            error = "Question is required"
        elif not answer:
            error = "Answer is required"

        if error:
            return self._render("admin_test_form.mako", {
                "request": request,
                "user": admin,
                "error": error,
                "form": {"subject": subject, "question": question, "answer": answer},
            })

        TestCrudRepository.create_test(TestSchema(
            subject=subject,
            question=question,
            answer=answer,
        ))
        return RedirectResponse("/admin_panel?tab=tests", status_code=303)

    def admin_lesson_delete(self, request: Request, lesson_id: int):
        self._require_admin(request)
        LessonRepository.delete_by_id(lesson_id)
        return RedirectResponse("/admin_panel?tab=lessons", status_code=303)

    def admin_test_delete(self, request: Request, test_id: int):
        self._require_admin(request)
        TestCrudRepository.delete_by_id(test_id)
        return RedirectResponse("/admin_panel?tab=tests", status_code=303)

    def admin_user_delete(self, request: Request, user_id: int):
        admin = self._require_admin(request)
        if admin.id == user_id:
            raise HTTPException(status_code=400, detail="Cannot delete yourself")
        UserCrudRepository.delete_by_id(user_id)
        return RedirectResponse("/admin_panel?tab=users", status_code=303)