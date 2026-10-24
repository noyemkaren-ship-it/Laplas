from fastapi import APIRouter
from .test import router as test_router
from .user import router as UserRouter
from .lesson import router as lessonRouter
from .pages import router as pagesRouter

routers: list[APIRouter] = [
    UserRouter,
    lessonRouter,
    test_router,
    pagesRouter,
]

__all__ = [
    "routers",
]