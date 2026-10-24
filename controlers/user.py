from fastapi import HTTPException, Request, Response
from utils.responses import Label
from crud_repositories import UserCrudRepository
from schemas import UserLogin, UserIn, UserOut
from utils.hesh_password import verify_psw
from utils.req import create_cookie, get_id


class UserController:
    def __init__(self):
        self.us = UserCrudRepository()

    def login(self, user: UserLogin, response: Response) -> UserOut:
        user_in_db = self.us.get_by_email(user.email)

        if user_in_db is None:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if not verify_psw(user.password, user_in_db.password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        create_cookie(response, user_in_db.id)
        return UserOut.model_validate(user_in_db)

    def register(self, user: UserIn, response: Response) -> UserOut:
        created = self.us.create(user)
        create_cookie(response, created.id)
        return UserOut.model_validate(created)

    def get_all(self, request: Request) -> list[UserOut]:
        user_id = self._get_user_id_from_request(request)
        users = self.us.get_all(user_id)
        return [UserOut.model_validate(u) for u in users]

    def me(self, request: Request) -> UserOut:
        user_id = self._get_user_id_from_request(request)
        user = self.us.get_by_id(user_id)
        return UserOut.model_validate(user)

    from utils.req import get_id

    @staticmethod
    def _get_user_id_from_request(request: Request) -> int:
        user_id = get_id(request)
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authenticated")
        return user_id

