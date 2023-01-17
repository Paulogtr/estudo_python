#crie uma lista com elementos de 1 a 10
# percorra a lista com um loop
# quando encontrar o elemento 4 remova-o
# exiba a lista 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
while i < len(lista):
    if lista[i] == 4:
       del lista[i]
    i = i + 1

print(lista)