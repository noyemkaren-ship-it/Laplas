from controlers import UserController
from schemas import UserLogin, UserIn, UserOut
from fastapi import (
    Request,
    Response,
    APIRouter,
)

uc = UserController()
router = APIRouter(tags=["user"], prefix="/user")

@router.get("/all", response_model=list[UserOut])
async def get_all_us(request: Request):
    return uc.get_all(request)


@router.post("/login", response_model=UserOut)
async def login_api(response: Response, user: UserLogin):
    return uc.login(user, response)


@router.post("/register", response_model=UserOut)
async def register_api(response: Response, user: UserIn):
    return uc.register(user, response)