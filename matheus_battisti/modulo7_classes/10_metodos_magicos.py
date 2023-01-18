class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'O nome do usuario é {self.nome} e tem {self.idade} anos e é um {self.profissao}'

matheus = Pessoa('Matheus', 29, 'Programador')

print(matheus.__str__())