from fastapi import APIRouter, Request
from schemas import Answer, TestSchema
from controlers import TestController

router = APIRouter(tags=["test"])

@router.post("/test")
def test_route(request: Request, test: TestSchema):
    return TestController.create_test(request, test)

@router.post("/answer")
def test_route(request: Request, answer: Answer):
    return TestController.answer_test(answer, request)

@router.get("/test_by_id/{id}")
async def test_route(test_id: int):
    return TestController.get_by_id(test_id)
