from Cliente import Cliente
from Conta import Conta

class Main:
    pass

c1 = Cliente('João', '99999-9999')
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, "Numero: ", conta.numero, "Seu Saldo: ", conta.saldo)
