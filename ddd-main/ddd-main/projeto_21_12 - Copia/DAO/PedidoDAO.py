from models import Orders, db

class OrdersDAO:
    @staticmethod
    def add_order(person_id, date, status, total):
        new_order = Orders(person_id=person_id, date=date, status=status, total=total)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def get_order_by_id(id_orders):
        return Orders.query.get(id_orders)

    @staticmethod
    def get_all_orders():
        return Orders.query.all()

    @staticmethod
    def update_order(id_orders, status=None, total=None):
        order = OrdersDAO.get_order_by_id(id_orders)
        if order:
            if status:
                order.status = status
            if total:
                order.total = total
            db.session.commit()
        return order

    @staticmethod
    def delete_order(id_orders):
        order = OrdersDAO.get_order_by_id(id_orders)
        if order:
            db.session.delete(order)
            db.session.commit()
        return order