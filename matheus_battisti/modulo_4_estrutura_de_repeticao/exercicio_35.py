saque = int(input('Digite o valor que deseja sacar: '))

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0

while saque > 0:
    while saque >= 100:
        nota_100 = nota_100 + 1
        saque = saque - 100
    while saque >= 50:
        nota_50 = nota_50 + 1
        saque = saque - 50
    while saque >= 20:
        nota_20 = nota_20 + 1
        saque = saque - 20
    while saque >= 10:
        nota_10 = nota_10 + 1
        saque = saque - 10
    
    
print(f'você recebera {nota_100} notas de R$100')   
