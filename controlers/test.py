from urllib import request
from fastapi import HTTPException
from schemas import Answer, TestSchema
from crud_repositories import TestCrudRepository
from crud_repositories import UserCrudRepository
from fastapi import Request
from utils.req import get_id

usc = UserCrudRepository()

class TestController:

    @staticmethod
    def _get_user_id_from_request(request: Request) -> int:
        user_id = get_id(request)
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        return user_id

    @staticmethod
    def get_by_id(test_id: int):
        return TestCrudRepository.get_by_id(test_id)

    @staticmethod
    def answer_test(answ: Answer, request: Request):
        if TestCrudRepository.answer_test(answ):
            user_id = TestController._get_user_id_from_request(request)
            usc.update_user_xp_by_id(user_id, 10)
            return {"message": "Okay"}
        return {"message": "Not okay"}

    @staticmethod
    def create_test(request: Request, test: TestSchema):
        user_id = TestController._get_user_id_from_request(request)
        if usc.is_admin(user_id):
            TestCrudRepository.create_test(test)
            return {"message": "Okay"}
        return {"message": "Not okay"}

