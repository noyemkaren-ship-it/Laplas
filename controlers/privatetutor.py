from http.client import HTTPResponse
from starlette.responses import HTMLResponse
from crud_repositories.privatetutor import PrivateTutorRepository
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
    def _get_user(request: Request) -> User:
        user_id = get_id(request)
        if user_id is None:
            raise HTTPException(status_code=400, detail="User does not exist")
        try:
            return UserCrudRepository.get_by_id(user_id)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="User does not exist")

    @staticmethod
    def _render(template_name: str, context: dict) -> HTMLResponse:
        tpl = lookup.get_template(template_name)
        html = tpl.render(**context)
        if isinstance(html, bytes):
            html = html.decode("utf-8")
        return HTMLResponse(content=html)

    @staticmethod
    def get_all(request: Request) -> HTMLResponse:
        all_tutors = PrivateTutorRepository.get_all()
        subjects = sorted({l.subject for l in all_tutors})
        user = PrivateTutorController._get_user(request)
        return PrivateTutorController._render("tutors.mako", {
            "request": request,
            "user": user,
            "tutors": all_tutors,
            "subjects": subjects,
            "lessons_count": len(all_tutors),
        })

    @staticmethod
    def create(request: Request, pt: PrivateTutorSchema):
        user = PrivateTutorController._get_user(request)
        if user.admin:
            return PrivateTutorRepository.create(pt)
        return HTTPException(status_code=400, detail="User already exists")