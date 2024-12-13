from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from models.homeM import User

# Cria as senhas cadastradas no site
admin_user = User("admin", "senhaforte", "admin")  # Usuário administrador
user1 = User("user1", "1234", "user")              # Usuário comum
user_list = [admin_user, user1]                    # Lista de usuários registrados

# Cria um blueprint
login_controller = Blueprint('login_controller', __name__)

# Define a rota para a página de login
@login_controller.route('/login', methods=['POST', 'GET'])
def login_page():
    # Se a requisição for POST, significa que o formulário de login foi enviado
    if request.method == "POST":
        email = request.form['email']  # Obtém o nome de usuário do formulário
        password = request.form['password']  # Obtém a senha do formulário

        # Verifica as credenciais do usuário
        for user in user_list:
            if user.validate(email, password):  # Valida o usuário e a senha
                session['email_logado'] = user.email  # Armazena o nome de usuário na sessão
                session['role'] = user.role               # Armazena o papel (role) do usuário na sessão
                flash(f'{user.email} logado com sucesso!')

                # Redireciona para a página correspondente ao papel do usuário
                if user.role == 'admin':
                    return redirect(url_for('login_controller.admin_page'))
                else:
                    return redirect(url_for('login_controller.user_page'))
        
        # Exibe uma mensagem de erro se as credenciais não forem válidas
        flash('Usuário ou senha incorretos.')
        return redirect(url_for('login_controller.login_page'))
    
    # Renderiza a página de login se a requisição for GET
    return render_template('login.html')

# Define a rota para a página do administrador
@login_controller.route('/admin')
def admin_page():
    # Verifica se o usuário está logado e se o papel (role) é de administrador
    if 'email_logado' not in session or session.get('role') != 'admin':
        flash("Você precisa estar logado como administrador para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('admin.html')  # Renderiza a página do administrador

# Define a rota para a página do usuário comum
@login_controller.route('/user')
def user_page():
    # Verifica se o usuário está logado
    if 'email_logado' not in session:
        flash("Você precisa estar logado para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('user.html')  # Renderiza a página do usuário

# Define a rota para o logout
@login_controller.route('/logout')
def logout():
    # Remove as informações de login e papel do usuário da sessão
    session.pop('email_logado', None)
    session.pop('role', None)
    flash("Você foi deslogado com sucesso.")
    # Redireciona para a página inicial
    return redirect(url_for('home.home'))
