from flask import Blueprint, render_template, request
from models.cadastroM import cadastros, add_cadastro

# Criação de um blueprint para o cadastro
cadastro_controller = Blueprint('cadastro', __name__)

# Rota para exibir a página de cadastro
@cadastro_controller.route('/cadastro')
def cadastro():
    # Renderiza o template 'cadastro.html', passando a lista de cadastros existentes
    return render_template('cadastro.html', cadastro=cadastros)

# Rota para adicionar um novo cadastro, acessada através do método POST
@cadastro_controller.route('/cadastro', methods=['POST'])
def add():
    # Adiciona um novo cadastro utilizando os dados enviados pelo formulário na requisição
    add_cadastro(
        request.form["name"],               # Nome do usuário
        request.form["email"],              # E-mail do usuário
        request.form["password"],           # Senha do usuário
        request.form["telephone"],          # Telefone do usuário
        request.form["registration_date"]   # Data de registro do usuário
    )
    # Após o cadastro, redireciona o usuário para a página de login
    return render_template('login.html', cadastro=cadastros)