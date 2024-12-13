from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash, session
from models.livroM import Livrinhos, Livro

# Cria um blueprint 
livro_controller = Blueprint('livro', __name__)

@livro_controller.route('/livro', methods=['GET', 'POST'])
def livro():
    # Verifica se o usuário está logado, caso contrário, redireciona para a página de login
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página de livros.")
        return redirect(url_for('login_controller.login_page'))

    # Se o método for POST, pega o ID do livro do formulário e chama a função para adicionar ao carrinho
    if request.method == 'POST':
        id = request.form.get('id')  
        return add_to_cart(id)

    # mostra a página de livros, mostrando a lista de livros disponível
    return render_template('livros.html', livros=Livrinhos)

# Função para adicionar um livro ao carrinho
def add_to_cart(id):
    # Cria uma resposta que redireciona para o carrinho
    resp = make_response(redirect(url_for('livro.ver'))) 
    # Tenta obter o valor do cookie para o livro com o ID fornecido
    cookie = request.cookies.get(f'produto_{id}')  
    if cookie:
        # Se o cookie já existe, incrementa a quantidade em 1 e atualiza o cookie
        resp.set_cookie(f'produto_{id}', str(int(cookie) + 1), max_age=60*60*24)  # faz um cookie com validade de 24 horas
    else:
        # Se o cookie não existe, cria o cookie com a quantidade inicial de 1
        return resp 

@livro_controller.route('/carrinho/del', methods=['POST'])
def delete():
    # Verifica se o usuário está logado, caso contrário, redireciona para a página de login
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página do carrinho.")
        return redirect(url_for('login_controller.login_page'))

    # Obtém o ID do livro a ser removido a partir do formulário
    id = request.form.get('id')  
    # Cria uma resposta que redireciona para o carrinho
    resp = make_response(redirect(url_for('livro.ver')))  
    # Tenta obter o valor do cookie para o livro com o ID fornecido
    cookie = request.cookies.get(f'produto_{id}')  
    if cookie:
        if int(cookie) > 1:
            # Se a quantidade no cookie for maior que 1, reduz a quantidade em 1
            resp.set_cookie(f'produto_{id}', str(int(cookie) - 1), max_age=60*60*24) 
        else:
            # Se a quantidade é 1, remove o cookie ao expirar imediatamente
            resp.set_cookie(f'produto_{id}', '0', expires=0)   
    return resp

@livro_controller.route('/carrinho', methods=['GET'])
def ver():
    # Verifica se o usuário está logado, caso contrário, redireciona para a página de login
    if 'usuario_logado' not in session:
        flash("Você precisa estar logado para acessar a página do carrinho.")
        return redirect(url_for('login_controller.login_page'))

    carrinho = []  # Lista dos itens do carrinho
    total = 0  # Variável para o total da compra
    # Itera sobre os livros disponíveis e verifica se há algum no carrinho
    for livro in Livrinhos:
        quantidade = int(request.cookies.get(f'produto_{livro.id}', 0)) 
        if quantidade > 0:
            subtotal = quantidade * livro.preco  # Calcula o subtotal para o livro
            total += subtotal  # Adiciona ao total do carrinho
            carrinho.append({
                'nome': livro.titulo,
                'preco': livro.preco,
                'quantidade': quantidade,
                'subtotal': subtotal,
                'id': livro.id 
            })
    # Renderiza a página do carrinho, passando os itens do carrinho e o total
    return render_template('carrinho.html', carrinho=carrinho, total=total)
