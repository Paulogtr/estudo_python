def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num
    
    return soma

print(soma_todos(5,4,3,2,66,5,34))