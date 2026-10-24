from fastapi import APIRouter, Request
from controlers.page import PageController

router = APIRouter(tags=["Pages"])
pc = PageController()


@router.get("/")
async def root(request: Request):
    return pc.root(request)

@router.get("/lessons")
async def lessons_page(request: Request):
    return pc.lessons(request)

@router.get("/lesson/{num}")
async def lesson_detail(request: Request, num: int):
    return pc.lesson_detail(request, num)

@router.get("/tests")
async def tests_page(request: Request):
    return pc.tests(request)

@router.get("/tests/subject/{subject}")
async def tests_by_subject(request: Request, subject: str):
    return pc.test_by_subject(request, subject)

@router.get("/subjects")
async def all_subjects(request: Request):
    return pc.all_subjects(request)

@router.get("/login")
async def login_page(request: Request):
    return pc.login_page(request)

@router.get("/register")
async def register_page(request: Request):
    return pc.register_page(request)

@router.get("/profile")
async def profile_page(request: Request):
    return pc.profile(request)


@router.get("/admin_panel")
async def admin_panel(request: Request):
    return pc.admin_panel(request)

@router.get("/admin_panel/lesson/new")
async def admin_lesson_form(request: Request):
    return pc.admin_lesson_form(request)

@router.post("/admin_panel/lesson/new")
async def admin_lesson_create(request: Request):
    return await pc.admin_lesson_create(request)

@router.get("/admin_panel/test/new")
async def admin_test_form(request: Request):
    return pc.admin_test_form(request)

@router.post("/admin_panel/test/new")
async def admin_test_create(request: Request):
    return await pc.admin_test_create(request)

@router.post("/admin_panel/lesson/{lesson_id}/delete")
async def admin_lesson_delete(request: Request, lesson_id: int):
    return pc.admin_lesson_delete(request, lesson_id)

@router.post("/admin_panel/test/{test_id}/delete")
async def admin_test_delete(request: Request, test_id: int):
    return pc.admin_test_delete(request, test_id)

@router.post("/admin_panel/user/{user_id}/delete")
async def admin_user_delete(request: Request, user_id: int):
    return pc.admin_user_delete(request, user_id)