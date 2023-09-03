from ..utils.repository import SQLAlchemyRepository
from ..models.users import Users
from ..schemas.orders import UserSchema

class UsersRepository(SQLAlchemyRepository):
    model = Users