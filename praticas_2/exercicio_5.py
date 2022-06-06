# Recebendo dez valores do usuário e somando - os:

lista = list()

for n in range(10):
    n = int(input("Digite o número: "))
    n + 1
    lista.append(n)

print("Esta é a lista de números: ", lista)  

sum = sum(lista)

print("Esta é a soma dos números contidos na lista: ", sum)
