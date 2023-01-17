# Escreva uma função que recebe uma lista de numeros
# Calcule a média dos numeros da lista 

def lista_numeros(l):
    soma = 0
    media = 0
    
    for num in l:
        soma += num
    media = soma / len(l)

    return media    
    

x = lista_numeros([9,7,8])

print(x)