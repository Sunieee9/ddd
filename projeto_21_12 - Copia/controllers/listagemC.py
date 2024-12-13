from flask import Blueprint, render_template
from models.cadastroM import cadastros, editar_cadastro

lista_controller = Blueprint('lista', __name__)

@lista_controller.route('/lista')
def listagem():
    return render_template('listagem.html', cadastros = cadastros)

@lista_controller.route('/<int:id>', methods=['POST', 'PUT'])
def editar(id):
    editar_cadastro(id)
    return render_template('listagem.html',cadastros = cadastros)