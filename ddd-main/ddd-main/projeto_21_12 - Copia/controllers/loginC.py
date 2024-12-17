from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from repository import PersonRepository

# Cria um blueprint
login_controller = Blueprint('login_controller', __name__)

# Define a rota para a página de login
@login_controller.route('/login', methods=['POST', 'GET'])
def login_page():
    # Se a requisição for POST, significa que o formulário de login foi enviado
    if request.method == "POST":
        email = request.form['email']  # Obtém o email do formulário
        password = request.form['password']  # Obtém a senha do formulário

        person_repository = PersonRepository()
        person = person_repository.get_person_by_email(email)  # Verificar se a pessoa exite pelo email

        if person and person.password == password:
            session['email_logado'] = person.email  # Armazena o email na sessão
            session['role'] = person.access_level  # Armazena o nivel do usuario na sessão
            flash(f'{person.name} está logado com sucesso!')  # Exibir usuario

            # Redireciona para a página correspondente ao papel do usuário
            if person.access_level == 'admin':
                return redirect(url_for('login_controller.admin_page'))
            else:
                return redirect(url_for('login_controller.user_page'))   

        flash('Usuário ou senha incorretos.')  # Exibir erro
        return redirect(url_for('login_controller.login_page'))  # Redireciona para a página de login caso de erro

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
    flash("Você foi deslogado com sucesso.")  # Exibe mensagem de logout
    # Redireciona para a página inicial
    return redirect(url_for('home.home'))
