class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

matheus = Pessoa("Matheus", 29, "Programação")

print(matheus.nome)
print(matheus.idade)
print(matheus.profissao)