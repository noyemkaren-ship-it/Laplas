from sqlalchemy import select, func

from base import Session


def get_all(model):
    with Session() as session:
        return list(session.scalars(select(model)).all())


def get_all_rnd(model):
    with Session() as session:
        query = select(model).order_by(func.random())
        return list(session.scalars(query).all())


def get_by_parameter(model, parameter_name, parameter_value):
    with Session() as session:
        column = getattr(model, parameter_name)
        query = select(model).where(column == parameter_value)
        return list(session.scalars(query).all())