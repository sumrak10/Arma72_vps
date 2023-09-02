import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from arma_bot.database.metadata import Base

from ..users.models import *



class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    telegram_user_id: Mapped[int] = mapped_column(ForeignKey("telegram_users.id"))
    # telegram_user: Mapped["TelegramUser"] = relationship("TelegramUser")

    status_id: Mapped[int] = mapped_column(ForeignKey("order_statuses.id"))
    # status: Mapped["OrderStatus"] = relationship()

    sales_manager_id: Mapped[int] = mapped_column(ForeignKey("telegram_users.id"))
    # sales_manager: Mapped["TelegramUser"] = relationship()

    # product: Mapped[List["ProductInOrder"]] = relationship()

    client_name: Mapped[str]
    contacts: Mapped[str]
    summ: Mapped[int]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())



class ProductInOrder(Base):
    __tablename__ = "products_in_orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))

    product_id: Mapped[int]
    product_name: Mapped[str]
    product_img: Mapped[str]
    count: Mapped[int]
    summ: Mapped[int]
    summ_type: Mapped[str]
    option_id: Mapped[int]
    option_value: Mapped[str]

class OrderStatus(Base):
    __tablename__ = "order_statuses"

    id: Mapped[int] = mapped_column(primary_key=True)

    verbose_name: Mapped[str]



