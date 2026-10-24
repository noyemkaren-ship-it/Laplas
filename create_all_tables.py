from base import Base
from base import engine
from models import *
from crud_repositories import UserCrudRepository
from utils.hesh_password import hash_psw

Base.metadata.create_all(engine)
UserCrudRepository.create_admin(2012, password="Kirov288A")
