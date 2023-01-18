# Crie uma classe Carro com as propriedaes, marca, valor, numero de portas e tanque de gasolina
# Crie um metodo que abastece o tanque de gasolina
# Crie um metodo dirigir que remove gasolina baseado em um km rodade

class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer(self, litros):
        if self.tanque >= 100:
            print('O tanque esta cheio')
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque -= (km / km_por_litro)


fusca = Carro("VW", 15000, 4, 100)

print(fusca.marca)
fusca.abastecer(100)

