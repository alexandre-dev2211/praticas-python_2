# Calculando a soma de 50 números pares:

lista = list()

n = 0

for n in range(26):
    n = n * 2
    lista.append(n)

print(lista)    

sum = sum(lista)

print("A soma da lista é: ", sum)
