class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def ligar(self):
        print('Carro ligado')

polo = Carro('VW', 60000)

print(polo.marca)

polo.ligar()