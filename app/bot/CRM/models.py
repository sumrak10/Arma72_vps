from database.accessor import gino as db





class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    telegram_user = db.Column(db.Integer, db.ForeignKey("telegram_users.id"))
    client_name = db.Column(db.String(256), nullable=False)
    contacts = db.Column(db.String(512), nullable=False)
    summ = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey("order_statuses.id"))

    sales_manager = db.Column(db.Integer, db.ForeignKey("telegram_users.id"))


class ProductInOrder(db.Model):
    __tablename__ = "products_in_orders"

    id = db.Column(db.Integer, primary_key=True)

    order = db.Column(db.Integer, db.ForeignKey("orders.id"))

    product_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(512), nullable=False)
    product_img = db.Column(db.String(1024), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    summ = db.Column(db.Integer, nullable=False)
    summ_type = db.Column(db.String(64), nullable=False)
    option_id = db.Column(db.Integer, nullable=False)
    option_value = db.Column(db.String(5256), nullable=False)

class OrderStatus(db.Model):
    __tablename__ = "order_statuses"

    id = db.Column(db.Integer, primary_key=True)

    verbose_name = db.Column(db.String(128), nullable=False)



