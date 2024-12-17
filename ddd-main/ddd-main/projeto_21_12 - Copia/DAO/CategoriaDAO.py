from models import Category, db
from sqlalchemy.orm import joinedload

class CategoryDAO:  # Criação do elemetento category

    @staticmethod
    def add_category(name, description):  # Funcionalidade para adicionar categoria
        new_category = Category(name = name, description = description)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def get_category(id_category):  # Vasualizar Category
        return Category.query.get(id_category)

    @staticmethod
    def get_all_category(): # Visualizar todos as tuuplas em category
        return Category.query.all()

    @staticmethod
    def get_filter_category(name):  # Filtrar category por nome
        query = Category.query.filter((Category.name.ilike(f"%{name}%")))
        return query.all()

    @staticmethod
    def edit_category(id_category, name, description): # Editar category
        category = CategoryDAO.get_category(id_category)
        if name:
            category.name = name
            db.session.commit()
        return category    