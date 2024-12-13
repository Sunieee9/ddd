from flask import Blueprint, render_template, request
from models.cadastroM import cadastros, add_cadastro

cadastro_controller = Blueprint('cadastro', __name__)

# Cadastro de usuários
@cadastro_controller.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', cadastro = cadastros)

@cadastro_controller.route('/cadastro', methods = ['POST'])
def add_cadastro():
    add_cadastro(request.form["name"], request.form["email"], request.form["password"], request.form["telephone"], request.form["registration_date"])
    return render_template('cadastro.html', cadastro = cadastros)