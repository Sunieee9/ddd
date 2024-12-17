from DAO import OrdersProductsDAO

class OrdersProductsRepository:
    def __init__(self):
        self.order_product = OrdersProductsDAO()

    def create_order_product(self, orders_id, products_id, quantity, total_f):
        return self.order_product.add_order_product(orders_id, products_id, quantity, total_f)

    def find_order_product_by_id(self, id_orders_products):
        return self.order_product.get_order_product_by_id(id_orders_products)

    def list_all_order_products(self):
        return self.order_product.get_all_order_products()

    def find_order_products_by_order(self, orders_id):
        return self.order_product.get_by_order_id(orders_id)

    def update_order_product(self, id_orders_products, quantity=None, total_f=None):
        return self.order_product.update_order_product(id_orders_products, quantity, total_f)

    def delete_order_product(self, id_orders_products):
        return self.order_product.delete_order_product(id_orders_products)
