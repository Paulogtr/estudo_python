# Crie um programa que gera um numero de 1 a 10
# peça para o usuario adivinhar o numero
# E identifique se ele acertou o ou não;
import random


def teste_de_sorte():
    aleatorio = random.randint(1,10)
    usuario = int(input("Digite o numero: "))
    print(f"O numero sorteado foi: {aleatorio}")
    if usuario == aleatorio:
        print('Parabéns você acertou!')
    else:
        print('Você errou, tente novamente!')

print(teste_de_sorte())