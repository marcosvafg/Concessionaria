# Classe Carro
class Carro:
    # Metodo construtor
    def __init__(self, modelo, marca, ano, preco, estado, placa):
        # Atributos
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.estado = estado
        self.placa = placa
        self.comprador = None
        self.vendedor = None

    # Método de acesso
    def get_modelo(self):
        return self.modelo

    def get_placa(self):
        return self.placa

    def get_venda(self):
        return 'Comprador: ' + self.comprador.get_nome() +\
               ' / Vendedor: ' + self.vendedor.get_nome()

    # Método para registrar venda
    def registar_venda(self, comprador, vendedor):
        self.comprador = comprador
        self.vendedor = vendedor