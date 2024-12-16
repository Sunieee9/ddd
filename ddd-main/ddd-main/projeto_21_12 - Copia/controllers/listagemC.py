from flask import Blueprint, render_template
from models.cadastroM import cadastros

# Criação do blueprint para gerenciar a listagem
lista_controller = Blueprint('lista', __name__)

# Rota para exibir a lista de usuários cadastrados
@lista_controller.route('/lista')
def listagem():
    # Renderiza o template 'listagem.html' e passa a lista de cadastros para ele
    return render_template('listagem.html', cadastros=cadastros)
