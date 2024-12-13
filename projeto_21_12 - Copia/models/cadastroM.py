from flask import request

class Cadastro:
    def __init__(self, id_person, name, email, password, telephone, registartiom_date):
        self.id_person = id_person
        self.name = name
        self.email = email
        self.password = password
        self.telephone = telephone
        self.registratiom_date = registartiom_date

cadastros = []

def add_cadastro(name, email, password, telephone, registartiom_date):
    id_person = len(cadastros) + 1
    novo_cadastro = Cadastro(id_person, name, email, password, telephone, registartiom_date)
    cadastros.append(novo_cadastro)
        
def editar_cadastro(id_person):
    for cadastro in cadastros:
        if cadastros.id_person == id_person:
            dados_atualizado = request
            cadastros.update(cadastro)
            return