from app.base.base_dao import BaseDAO
from app.modules.user.model import User


class UserDao(BaseDAO[User]):
    model = User