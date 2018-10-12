# Classe Comprador
class Comprador:
    # Método construtor
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    # Métodos de acesso
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf