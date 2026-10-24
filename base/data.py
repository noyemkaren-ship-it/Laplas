from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass