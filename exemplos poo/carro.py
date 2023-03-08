class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        if self.velocidade - valor >= 0:
            self.velocidade -= valor
        else:
            self.velocidade = 0

    def mostrar_informacoes(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Velocidade:", self.velocidade, "km/h")


carro1 = Carro("Chevrolet", "Onix", 2020)
carro2 = Carro("Fiat", "Uno", 2015)

carro1.acelerar(50)
carro1.mostrar_informacoes()

carro2.acelerar(30)
carro2.frear(10)
carro2.mostrar_informacoes()

"""
Neste exemplo, temos uma classe chamada Carro que tem quatro atributos: marca, 
modelo, ano e velocidade. A classe também tem três métodos: acelerar, frear e 
mostrar_informacoes.

Em seguida, criamos duas instâncias da classe Carro (carro1 e carro2) e chamamos os 
métodos acelerar, frear e mostrar_informacoes para cada uma delas. Isso imprimirá na 
tela as informações de cada carro, incluindo sua velocidade atual.
"""
