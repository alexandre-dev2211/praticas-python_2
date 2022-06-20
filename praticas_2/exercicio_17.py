# Exibindo o maior número dentro de um conjunto:

n = int(input("Digite um número: "))

a = []

while n < 10:
    n = int(input("Digite um número: "))
    a.append(n)

print(a)    

print(max(a))
