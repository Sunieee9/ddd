class Livro:
    # Construtor da classe Livro, que inicializa cada instância com um id, título e preço
    def __init__(self, id, titulo, preco):
        self.id = id            # Identificador único do livro
        self.titulo = titulo    # Título do livro
        self.preco = preco      # Preço do livro

# Cria uma lista de Livro chamada Livrinhos, contendo alguns livros de exemplo
Livrinhos = [
    Livro(1, 'Harry Potter', 500),    # Livro com id 1, título "Harry Potter" e preço 500 (ps: o mais divo)
    Livro(2, 'Crepúsculo', 30),       # Livro com id 2, título "Crepúsculo" e preço 30
    Livro(3, 'Cruella', 200)          # Livro com id 3, título "Cruella" e preço 200
]
