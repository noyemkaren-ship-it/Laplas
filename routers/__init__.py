from fastapi import APIRouter
from .test import router as test_router
from .user import router as UserRouter
from .lesson import router as lessonRouter
from .pages import router as pagesRouter
from private_tutor import router as private_tutorRouter

routers: list[APIRouter] = [
    UserRouter,
    lessonRouter,
    test_router,
    pagesRouter,
    private_tutorRouter
]

__all__ = [
    "routers",
]