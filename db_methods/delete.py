from sqlalchemy import delete as sql_delete

from base import Session


def delete(model, obj_id: int):
    with Session() as session:
        session.execute(sql_delete(model).where(model.id == obj_id))
        session.commit()