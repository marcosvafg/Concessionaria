# Classe Concessionaria

from carro import Carro

class Concessionaria:
    # Método construtor
    def __init__(self, nome):
        self.nome = nome
        self.carros = self.recuperar_carros()

    # Métodos de acesso
    def get_nome(self):
        return self.nome

    def get_carros(self):
        return self.carros

    # Método para adicionar um carro
    def add_carro(self, carro):
        self.carros.append(carro)
        self.gravar_carro(carro)

    # Função para abrir o arquivo V12 MOTORS.txt
    # e retornar a lista de carros
    def recuperar_carros(self):
        carros = []

        arquivo = open(self.nome + '.txt', 'r')

        for linha in arquivo:
            lista = linha.strip('\n').split(',')
            carro = Carro(lista[0], lista[1], int(lista[2]), int(lista[3]), lista[4], lista[5])
            carros.append(carro)

        arquivo.close()
        return carros


    # Método para escrever o arquivo de carros
    def gravar_carro(self, carro):
        linha = carro.modelo + ',' + carro.marca + ',' + str(carro.ano) +\
            ',' + str(carro.preco) + ',' + carro.estado + ',' + carro.placa

        arquivo = open(self.nome + '.txt', 'a+')
        arquivo.write(linha + '\n')
        arquivo.close()
