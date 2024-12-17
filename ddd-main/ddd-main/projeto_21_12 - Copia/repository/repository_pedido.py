from DAO import OrdersDAO

class OrdersRepository:
    def __init__(self) -> None:
        self.orders_dao = OrdersDAO()

    def add_order(self, person_id, date, status, total):
        # Agora o método é de instância, então usa 'self' sem o @staticmethod
        return self.orders_dao.add_order(person_id, date, status, total)

    def get_order_by_id(self, id_orders):
        return self.orders_dao.get_order_by_id(id_orders)

    def get_all_orders(self):
        return self.orders_dao.get_all_orders()

    def update_order(self, id_orders, status=None, total=None):
        return self.orders_dao.update_order(id_orders, status, total)

    def delete_order(self, id_orders):
        return self.orders_dao.delete_order(id_orders)
