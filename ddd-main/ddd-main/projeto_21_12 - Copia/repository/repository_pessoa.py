from DAO import PersonDAO

class PersonRepository:
    def __init__(self) -> None:
        self.person_dao = PersonDAO()

    def get_person(self, id_person):
        return self.person_dao.get_person(id_person)
    
    def add_person(self, name, email, password, access_level, telefone, register_date):
        return self.person_dao.add_person(name, email, password, access_level, telefone, register_date)

    def get_all_persons(self):
        return self.person_dao.get_all_persons()

    def get_person_by_email(self, email):
        return self.person_dao.get_person_by_email(email)

    def edit_person(self, id_person, name=None, email=None, password=None, access_level=None, telefone=None):
        return self.person_dao.edit_person(id_person, name, email, password, access_level, telefone)

    def delete_person(self, id_person):
        return self.person_dao.delete_person(id_person)
