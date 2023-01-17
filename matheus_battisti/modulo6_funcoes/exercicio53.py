# escreva uma função que recebe uma lista de numeros
# A função deve retornar os numeros pares da lista

def lista(lista):
    nova_lista = []

    for numero in lista:
        if numero % 2 == 0:
            nova_lista.append(numero)

    return nova_lista

nums = [1,2,3,4,5,6,7,8,9]

lista_par = lista(nums)

print(lista_par)