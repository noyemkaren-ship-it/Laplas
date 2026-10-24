from sqlalchemy import select, delete as sql_delete
from db_methods import create, get_by_parameter, get_all as db_get_all
from base import Session
from schemas import UserIn, UserLogin, UserOut
from models import User
from utils.hesh_password import hash_psw, verify_psw
from utils.errors_codes import LogicError


class UserCrudRepository:
    @staticmethod
    def create_admin(
        key: int,
        name: str = "admin",
        email: str = "noyemkaren@gmail.com",
        password: str = "Kirov288A",
        age: int = 20,
        num: str = "+7 906 012 21 00",
    ) -> None:
        if key != 2012:
            raise LogicError("Access denied: Not an admin")
        if get_by_parameter(User, "email", email):
            raise LogicError("Admin email already exists")

        with Session() as session:
            admin = User(
                name=name,
                email=email,
                password=hash_psw(password),
                age=age,
                admin=True,
                num=num,
            )
            session.add(admin)
            session.commit()
            session.refresh(admin)

    @staticmethod
    def create(user: UserIn) -> User:
        if get_by_parameter(User, "email", user.email):
            raise LogicError("Email already exists")
        if get_by_parameter(User, "name", user.name):
            raise LogicError("Name already exists")

        new_user = User(
            name=user.name,
            email=user.email,
            password=hash_psw(user.password),
            age=user.age,
            num=user.num,
        )
        return create(new_user)   # ← возвращаем результат db_methods.create

    @staticmethod
    def have_got_email_and_password(ul: UserLogin) -> bool:
        user = UserCrudRepository.get_by_email(ul.email)
        if user is None:
            return False
        return verify_psw(ul.password, user.password)

    @staticmethod
    def get_by_id(us_id: int) -> User | None:
        res = get_by_parameter(User, "id", us_id)
        return res[0] if res else None

    @staticmethod
    def get_by_email(email: str) -> User | None:
        res = get_by_parameter(User, "email", email)
        return res[0] if res else None

    @staticmethod
    def delete_by_email(email: str) -> None:
        with Session() as session:
            stmt = sql_delete(User).where(User.email == email)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def get_all(user_id: int) -> list[User]:
        with Session() as session:
            user = session.execute(
                select(User).where(User.id == user_id)
            ).scalars().first()
            if not user:
                raise LogicError("User not found")
            if not user.admin:
                raise LogicError("Access denied: Not an admin")
            return db_get_all(User)

    @staticmethod
    def update_user_xp_by_id(user_id: int, xp: int) -> int:
        with Session() as session:
            user = session.execute(
                select(User).where(User.id == user_id)
            ).scalars().first()
            if user is None:
                raise LogicError("User not found")

            user.xp = (user.xp or 0) + xp
            session.commit()
            return user.xp

    @staticmethod
    def is_admin(user_id: int) -> bool:
        with Session() as session:
            user = session.execute(
                select(User).where(User.id == user_id)
            ).scalars().first()
            if not user:
                raise LogicError("User not found")
            return bool(user.admin)