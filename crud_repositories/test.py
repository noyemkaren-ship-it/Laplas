from base import Session
from models import Test
from sqlalchemy import select
from db_methods import create, get_all, get_by_parameter
from schemas import TestSchema, TestOut, Answer

class TestCrudRepository:
    @staticmethod
    def create_test(test: TestSchema) -> TestOut:
        new_test = Test(
            subject=test.subject,
            question=test.question,
            answer=test.answer,
        )
        create(new_test)
        return TestOut(
            subject=test.subject,
            question=test.question,
        )

    @staticmethod
    def get_by_subject(subject: str):
        return get_by_parameter(Test, "subject", subject)

    @staticmethod
    def get_all():
        return get_all(Test)

    @staticmethod
    def get_by_id(test_id: int) -> Test | None:
        with Session() as session:
            return session.execute(select(Test).where(Test.id == test_id)).scalar_one_or_none()

    @staticmethod
    def answer_test(answ: Answer) -> bool:
        test = TestCrudRepository.get_by_id(answ.test_id)
        if test is not None:
            if test.answer == answ.answer:
                return True
        return False