class User:
    # Construtor da classe User, inicializando o nome de usuário, senha e papel do usuário
    def __init__(self, email, password, role):
        self.email = email      # Armazena o nome de usuário
        self.password = password      # Armazena a senha do usuário
        self.role = role              # Armazena o papel (role) do usuário, como "admin" ou "user"

    # Método para validar o nome de usuário e a senha
    def validate(self, email, password):
        # Retorna True se o nome de usuário e senha passados correspondem aos armazenados no objeto
        return self.email == email and self.password == password
