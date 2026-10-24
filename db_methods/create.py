from sqlalchemy.exc import IntegrityError, DataError

from base import Session


def create(model):
    with Session() as session:
        try:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model
        except (IntegrityError, DataError) as e:
            session.rollback()
            print(e)
            raise