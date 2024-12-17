from models import Orders_Products, db

class OrdersProductsDAO:
    @staticmethod
    def add_order_product(orders_id, products_id, quantity, total_f):
        new_order_product = Orders_Products(
            orders_id=orders_id,
            products_id=products_id,
            quantity=quantity,
            total_f=total_f
        )
        db.session.add(new_order_product)
        db.session.commit()
        return new_order_product

    @staticmethod
    def get_order_product_by_id(id_orders_products):
        return Orders_Products.query.get(id_orders_products)

    @staticmethod
    def get_all_order_products():
        return Orders_Products.query.all()

    @staticmethod
    def get_by_order_id(orders_id):
        return Orders_Products.query.filter_by(orders_id=orders_id).all()

    @staticmethod
    def update_order_product(id_orders_products, quantity=None, total_f=None):
        order_product = Orders_Products.query.get(id_orders_products)
        if not order_product:
            return None
        
        if quantity is not None:
            order_product.quantity = quantity
        if total_f is not None:
            order_product.total_f = total_f
        
        db.session.commit()
        return order_product

    @staticmethod
    def delete_order_product(id_orders_products):
        order_product = Orders_Products.query.get(id_orders_products)
        if order_product:
            db.session.delete(order_product)
            db.session.commit()
            return True
        return False
