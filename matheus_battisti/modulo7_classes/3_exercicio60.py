# Crie uma classe Carro com as propriedades, portas, motor, se tem teto soalr, marca, preço
# Crie objetos preenchendo os valores das propriedades

class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco

ferrari = Carro(2, 4.0, False, 'ferrari', 1000000)
        
