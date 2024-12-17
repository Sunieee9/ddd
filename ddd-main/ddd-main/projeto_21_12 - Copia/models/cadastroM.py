from flask import request

class Cadastro:
    def __init__(self, id_person, name, email, password, telephone, registration_date):
        # Inicializa os atributos da classe Cadastro
        self.id_person = id_person  # Identificador único da pessoa
        self.name = name            # Nome da pessoa
        self.email = email          # Email da pessoa
        self.password = password    # Senha da pessoa (armazenada em texto plano, o que não é seguro)
        self.telephone = telephone  # Telefone da pessoa
        self.registration_date = registration_date  # Corrigido nome do parâmetro

# Lista para armazenar os objetos do tipo Cadastro
cadastros = []

def add_cadastro(name, email, password, telephone, registration_date):
    # Adiciona um novo cadastro à lista cadastros
    id_person = len(cadastros) + 1  # Gera um ID único baseado no tamanho da lista
    novo_cadastro = Cadastro(id_person, name, email, password, telephone, registration_date)  # Cria um novo objeto Cadastro
    cadastros.append(novo_cadastro)  # Adiciona o objeto à lista
    print(id_person, novo_cadastro)

        
def editar_cadastro(id_person):
    # Edita um cadastro existente baseado no ID da pessoa
    for cadastro in cadastros:
        if cadastros.id_person == id_person:  # Verifica se o ID corresponde a um cadastro existente
            dados_atualizado = request  # Obtém os dados atualizados da requisição
            cadastros.update(cadastro)  # Atualiza os dados do cadastro correspondente
            return
