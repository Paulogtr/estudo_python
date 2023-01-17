#maneira correta para copiar uma lista sem alterar a lista de referencia
# utilizamos [:] para copiar a lista 

lista = ['Matehus', 'Paulo', 'Luiz']

nova_lista = lista[:]

print(lista)
print(nova_lista)

nova_lista[0] = 'João'

print(lista)
print(nova_lista)