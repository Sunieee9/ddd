from flask import Blueprint, render_template
from models.cadastroM import cadastros
from repository import PersonRepository

# Criação do blueprint para gerenciar a listagem
lista_controller = Blueprint('lista', __name__)

# Rota para exibir a lista de usuários cadastrados
@lista_controller.route('/lista')
def listagem():

    lista_repository = PersonRepository()

    cadastros = lista_repository.get_all_persons()
    # Renderiza o template 'listagem.html' e passa a lista de cadastros para ele
    return render_template('listagem.html', cadastros=cadastros)
