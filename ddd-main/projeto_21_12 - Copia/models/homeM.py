class User:
    # Construtor da classe User, inicializando o nome de usuário, senha e papel do usuário
    def __init__(self, username, password, role):
        self.username = username      # Armazena o nome de usuário
        self.password = password      # Armazena a senha do usuário
        self.role = role              # Armazena o papel (role) do usuário, como "admin" ou "user"

    # Método para validar o nome de usuário e a senha
    def validate(self, username, password):
        # Retorna True se o nome de usuário e senha passados correspondem aos armazenados no objeto
        return self.username == username and self.password == password
