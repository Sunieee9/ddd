from models import Person, db

class PersonDAO:
    @staticmethod
    def add_person(name, email, password, access_level, telefone, register_date):
        new_person = Person(
            name=name,
            email=email,
            password=password,
            access_level=access_level,
            telefone=telefone,
            register_date=register_date
        )
        db.session.add(new_person)
        db.session.commit()
        return new_person

    @staticmethod
    def get_person(id_person):
        return Person.query.get(id_person)

    @staticmethod
    def get_all_persons():
        return Person.query.all()

    @staticmethod
    def get_person_by_email(email):
        return Person.query.filter_by(email=email).first()

    @staticmethod
    def edit_person(id_person, name=None, email=None, password=None, access_level=None, telefone=None):
        person = PersonDAO.get_person(id_person)
        if not person:
            return None
        if name:
            person.name = name
        if email:
            person.email = email
        if password:
            person.password = password
        if access_level:
            person.access_level = access_level
        if telefone:
            person.telefone = telefone
        db.session.commit()
        return person

    @staticmethod
    def delete_person(id_person):
        person = PersonDAO.get_person(id_person)
        if not person:
            return None
        db.session.delete(person)
        db.session.commit()
        return person
