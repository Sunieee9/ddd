from flask import Flask, render_template
from controllers.loginC import login_controller
from controllers.homeC import home_controller
from controllers.livroC import livro_controller
from controllers.cadastroC import cadastro_controller
from controllers.listagemC import lista_controller
from database import init_db

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma chave secreta para proteger a sessão do aplicativo (necessária para sessões em Flask)
app.secret_key = 'MRY'

# Registra os blueprints para organizar as rotas e controladores
app.register_blueprint(login_controller)  # Registra o blueprint do controlador de login
app.register_blueprint(home_controller)   # Registra o blueprint do controlador da página inicial
app.register_blueprint(livro_controller)  # Registra o blueprint do controlador de livros
app.register_blueprint(cadastro_controller)  # Registra o blueprint do cadastro de usuários
app.register_blueprint(lista_controller)  # Registra o blueprint da lista de usuários

# Trata erros de acesso negado (status 401) com uma página personalizada
@app.errorhandler(401)
def acesso_negado(error):
    # Exibe a página '401.html' quando ocorre um erro 401 (não autorizado)
    return render_template('401.html'), 401

# Trata erros de página não encontrada (status 404) com uma página personalizada
@app.errorhandler(404)
def page_not_found(error):
    # Exibe a página '404.html' quando ocorre um erro 404 (página não encontrada)
    return render_template('404.html'), 404

# Se o arquivo for executado diretamente, inicia o servidor Flask em modo de depuração
if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        app.run(debug=True)
