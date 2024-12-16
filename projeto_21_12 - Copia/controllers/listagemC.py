from flask import Blueprint, render_template
from models.cadastroM import cadastros

lista_controller = Blueprint('lista', __name__)

@lista_controller.route('/lista')
def listagem():
    return render_template('listagem.html', cadastros = cadastros)