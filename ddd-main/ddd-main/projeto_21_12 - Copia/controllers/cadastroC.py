from flask import Blueprint, render_template, request, jsonify
from repository import PersonRepository, OrdersRepository, ProductRepository
# Instância do repositório
person_repository = PersonRepository()

# Criação de um blueprint para o cadastro
cadastro_controller = Blueprint('cadastro', __name__)

# Rota para exibir a página de cadastro
@cadastro_controller.route('/cadastro')
def cadastro():
    # Obtém todas as pessoas registradas para exibir na página de cadastro (se necessário)
    cadastros = person_repository.get_all_persons()
    return render_template('cadastro.html', cadastro=cadastros)

# Rota para adicionar um novo cadastro, acessada através do método POST
@cadastro_controller.route('/cadastro', methods=['POST'])
def add():
    # Captura os dados enviados pelo formulário
    nome = request.form["name"]
    email = request.form["email"]
    senha = request.form["password"]
    telefone = request.form["telephone"]
    data_nascimento = request.form["registration_date"]

    person_repository.add_person(
        name=nome,
        email=email,
        password=senha,
        access_level='admin',  # Define um nível de acesso padrão
        telefone=telefone,
        register_date=data_nascimento
    )

    # Após o cadastro, redireciona o usuário para a página de login
    return render_template('login.html')

@cadastro_controller.route('/ped')
def adddd():
    person_id = 1
    date = "17012008"
    status = "pendente"
    total = 10

    # Crie uma instância de OrdersRepository antes de chamar add_order
    orders_repository = OrdersRepository()

    new_order = orders_repository.add_order(person_id=person_id, date=date, status=status, total=total)

    return jsonify(new_order.to_json()), 201

@cadastro_controller.route('/procd')
def procd():
    name = "Pulseira"
    description = "coisa que poem no pulso"
    price = 1000
    stock_quantity = 5
    category_id = 1

    produto_repository = ProductRepository()

    new_produto = produto_repository.add_product(name = name, description = description, price = price, stock_quantity = stock_quantity, category_id = category_id)

    return jsonify(new_produto.to_json()), 201

    