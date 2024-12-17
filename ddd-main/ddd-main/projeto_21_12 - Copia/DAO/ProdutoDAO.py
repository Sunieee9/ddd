from models import Product, db

class ProductDAO:
    @staticmethod
    def add_product(name, description, price, stock_quantity, category_id):
        new_product = Product(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            category_id=category_id
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product  
    
    @staticmethod
    def get_product_by_id(id_product):
        return Product.query.get(id_product)

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def update_product(id_product, name, description, price, stock_quantity, category_id):
        product = Product.query.get(id_product)
        if product:
            if name:
                product.name = name
            if description:
                product.description = description
            if price:
                product.price = price
            if stock_quantity:
                product.stock_quantity = stock_quantity
            if category_id:
                product.category_id = category_id
            db.session.commit()
        return product

    @staticmethod
    def delete_product(id_product):
        product = Product.query.get(id_product)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
