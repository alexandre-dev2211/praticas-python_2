# Lendo dez números e exibindo o menor e o maior valor:

lista = list()

for n in range(10):
    n = n + 1
    print(n)
    lista.append(n)

min = min(lista)

print("Menor número: ", min)

max = max(lista)

print("Maior número: ", max)
