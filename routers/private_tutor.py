from fastapi import APIRouter, Request
from controlers import PrivateTutorController
from schemas import PrivateTutorSchema

router = APIRouter(tags=["Private Tutor"])


@router.get("/private-tutors")
async def get_private_tutors(request: Request):
    return PrivateTutorController.get_all(request)

@router.post("/private-tutors")
async def post_private_tutors(request: Request, pt: PrivateTutorSchema):
    return PrivateTutorController.create(request, pt)