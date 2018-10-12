# Classe Vendedor
class Vendedor:
    # Método construtor
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    # Métodos de acesso
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_matricula(self):
        return self.matricula