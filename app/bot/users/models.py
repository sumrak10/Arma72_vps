from database.accessor import gino as db



class TelegramUser(db.Model):
    __tablename__ = "telegram_users"
    
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    role = db.Column(db.Integer, db.ForeignKey("telegram_user_roles.id"))

    async def get_role_rights(self) -> dict:
        role = await TelegramUserRole.query.where(TelegramUserRole.id==self.role).gino.first()
        print(role.__dict__['__values__'])
        return role

class TelegramUserRole(db.Model):
    __tablename__ = "telegram_user_roles"
    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    verbose_name = db.Column(db.String(128), nullable=False)
    superuser = db.Column(db.Boolean, nullable=False)
    client = db.Column(db.Boolean, nullable=False)
    hr = db.Column(db.Boolean, nullable=False)
    sales_manager = db.Column(db.Boolean, nullable=False)