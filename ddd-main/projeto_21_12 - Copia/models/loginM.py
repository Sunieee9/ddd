class Login:
    # Construtor da classe Login, inicializando com usuário e senha
    def __init__(self, email, senha):
        self.email = email  # Armazena o nome de usuário
        self.senha = senha      # Armazena a senha do usuário

    # Método para validar o nome de usuário e a senha
    def validate(self, email, password):
        # Retorna True se o nome de usuário e a senha passados coincidem com os armazenados
        return self.email == email and self.senha == password
