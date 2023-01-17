# Escreva uma função ue desenha uma escada no terminal
# Os numeros de degraus deve ser informado por parametro

def escadinha(degraus):
    i = 1
    while i <= degraus:
        print('#' * i)
        i = i + 1

escadinha(10)