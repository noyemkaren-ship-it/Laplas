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