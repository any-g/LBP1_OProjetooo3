class User:
    def __init__(self, nome, senha, id):
        self.nome = nome
        self.senha = senha
        self.id = id

users = [User("Any", 1234, 0)]
users.append(User("Admin", 5678, 1))
