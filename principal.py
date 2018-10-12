# Código principal do programa
# Importando as classes
from concessionaria import Concessionaria
from carro import Carro
from comprador import Comprador
from vendedor import Vendedor

# Criando uma concessionaria
v12 = Concessionaria('V12 MOTORS')

print(v12.get_nome())
print(v12.get_carros())

# Criando um carro e adicionando
toro = Carro('TORO', 'FIAT', 2018, 60000, 'NOVO', 'PPP0303')
v12.add_carro(toro)

# Criando um carro e adicionando
fit = Carro('FIT', 'HONDA', 2015, 5000, 'USADO', 'PPP0404')
v12.add_carro(fit)

# for para imprimir os modelos
for item in v12.get_carros():
    print(item.get_placa())

# Registar a venda do up
# Criar um comprador
# Criar um vendedor
#joao = Comprador('João', '123')
#jose = Vendedor('José', '456', '001')
#up.registar_venda(joao, jose)
#print(up.get_venda())

# atribuição por referência
# x = 10
# y = x
# atribuição por valor