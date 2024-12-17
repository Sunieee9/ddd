from DAO import ProductDAO

class ProductRepository:
    def __init__(self) -> None:
        self.product_dao = ProductDAO()

    def add_product(self, name, description, price, stock_quantity, category_id):
        return self.product_dao.add_product(name, description, price, stock_quantity, category_id)

    def get_product_by_id(self, id_product):
        return self.product_dao.get_product_by_id(id_product)

    def get_all_products(self):
        return self.product_dao.get_all_products()

    def update_product(self, id_product, name, description, price, stock_quantity, category_id):
        return self.product_dao.update_product(id_product, name, description, price, stock_quantity, category_id)

    def delete_product(self, id_product):
        return self.product_dao.delete_product(id_product)
