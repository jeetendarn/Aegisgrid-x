from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.branch import Branch
from app.models.network import Network
from app.models.device import Device
from app.models.asset import Asset
from app.models.application import Application

from app.models.user_role import user_role
from app.models.role_permission import role_permission