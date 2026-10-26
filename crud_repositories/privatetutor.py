from models import PrivateTutor
from db_methods import create, get_all, delete, get_by_parameter
from schemas import PrivateTutorSchema


class PrivateTutorRepository:
    @staticmethod
    def get_all():
        return get_all(PrivateTutor)

    @staticmethod
    def create(pt: PrivateTutorSchema):
        new_tutor = PrivateTutor(
            name=pt.name,
            subject=pt.subject,
            description=pt.description,
            initials=pt.initials,
        )
        create(new_tutor)
        return pt

    @staticmethod
    def get_by_subject(subject: str):
        return get_by_parameter(PrivateTutor, "subject", subject)

    @staticmethod
    def delete_by_id(pt_id: int):
        return delete(PrivateTutor, pt_id)