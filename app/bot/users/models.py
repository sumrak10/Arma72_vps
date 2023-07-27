from typing import List, Any, Optional, Dict


from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.accessor import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str]
    last_name: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("telegram_user_roles.id"))
    role: Mapped["TelegramUserRole"] = relationship(back_populates="users")





class TelegramUserRole(Base):
    __tablename__ = "telegram_user_roles"
    
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    verbose_name: Mapped[Optional[str]]
    permissions: Mapped[Dict[str, Any]]

    users: Mapped[List["TelegramUser"]] = relationship(back_populates="role")