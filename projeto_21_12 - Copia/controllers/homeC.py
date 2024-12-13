from flask import Blueprint, render_template, request, redirect, url_for, session, flash

# Cria um blueprint
home_controller = Blueprint('home', __name__)

# Define a rota para a página inicial
@home_controller.route('/', methods=['POST', 'GET'])
def home():
    # Obtém o nome do usuário logado (se houver) a partir da sessão
    usuario_logado = session.get('usuario_logado')
    # mostra a página 'home.html' e passa o nome do usuário logado como variável para o template
    return render_template('home.html', usuario=usuario_logado)

# Função executada antes de cada requisição, para verificar a autenticação do usuário
@home_controller.before_request
def autenticar_usuario():
    # Verifica se a rota solicitada é protegida, ou seja, requer autenticação
    rota_protegida = request.endpoint in ['home.admin_page', 'home.user_page']
    # Se a rota é protegida e o usuário não está logado, redireciona para a página de login
    if rota_protegida and 'usuario_logado' not in session:
        return redirect(url_for('login_controller.login_page'))
