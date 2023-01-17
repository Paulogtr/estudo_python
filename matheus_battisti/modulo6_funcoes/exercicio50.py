#Crie uma função que exibe a multiplicação de dois numeros
# Os número devem ser passados por parametro

def multiplica(a, b):
    num1 = a
    num2 = b
    resultado = num1 * num2
    print(resultado)

multiplica(5, 10)

#segunda forma de resolução mais simples
def multiplicacao(a, b):
    print(a * b)

multiplicacao(10, 10)

#passando paramentro externo
valor1 = 10
valor2 = 20

multiplicacao(valor1, valor2)