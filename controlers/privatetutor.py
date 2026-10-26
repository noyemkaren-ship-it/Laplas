from http.client import HTTPResponse
from starlette.responses import HTMLResponse
from crud_repositories import PrivateTutorRepository
from schemas import PrivateTutorSchema
from utils.req import get_id
from fastapi import Request, HTTPException
from crud_repositories import UserCrudRepository
from mako.lookup import TemplateLookup
from fastapi.responses import HTMLResponse, RedirectResponse
from models import User

uc = UserCrudRepository()

lookup = TemplateLookup(
    directories=["templates"],
    input_encoding="utf-8",
    output_encoding=None,
    encoding_errors="replace",
    default_filters=["str"],
)


class PrivateTutorController:
    @staticmethod
    def _get_user(request: Request):
        """Возвращает пользователя или None, если он не авторизован."""
        user_id = get_id(request)
        if user_id is None:
            return None
        try:
            return UserCrudRepository.get_by_id(user_id)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def _render(template_name: str, context: dict) -> HTMLResponse:
        tpl = lookup.get_template(template_name)
        html = tpl.render(**context)
        if isinstance(html, bytes):
            html = html.decode("utf-8")
        return HTMLResponse(content=html)

    @staticmethod
    def get_all(request: Request) -> HTMLResponse:
        # 1. Читаем фильтр по предмету из query string
        subject = request.query_params.get("subject")

        # 2. Получаем всех репетиторов
        all_tutors = PrivateTutorRepository.get_all()

        # 3. Список предметов строим по ПОЛНОМУ списку (до фильтрации),
        #    иначе после выбора предмета пропадут остальные чипы
        subjects = sorted({t.subject for t in all_tutors if t.subject})

        # 4. Применяем фильтр
        tutors = all_tutors
        if subject:
            tutors = [t for t in all_tutors if t.subject == subject]

        # 5. Пользователь может быть None (аноним)
        user = PrivateTutorController._get_user(request)

        return PrivateTutorController._render("tutors.mako", {
            "request": request,
            "user": user,
            "tutors": tutors,
            "subjects": subjects,
            "tutors_count": len(all_tutors),
            "active_subject": subject,
        })

    @staticmethod
    def create(request: Request, pt: PrivateTutorSchema):
        user = PrivateTutorController._get_user(request)
        if user is None:
            raise HTTPException(status_code=401, detail="Authentication required")
        if not user.admin:
            raise HTTPException(status_code=403, detail="Admin privileges required")
        return PrivateTutorRepository.create(pt)