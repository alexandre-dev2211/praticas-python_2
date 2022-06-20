# Retornando o maior e o menor número de um conjuto (considerando positivos e negativos inteiros):

n = 0

c = []

while n >= 0:
    n = int(input("Digite um número: "))
    c.append(n)

print(c)

print(min(c))

print(max(c))
