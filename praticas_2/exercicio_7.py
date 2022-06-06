# Lendo dez inteiros positivos, ignorando negativos e exibindo a média:

lista = list()

n = 0

for n in range (1, 11):
    n = int(input("Digite um número: "))
    n + 1
    lista.append(n)
    
print(lista)  

for n in lista:
   if n < 0:
    lista.remove(n)

print(lista)

sum  = sum(lista)

lenght = len(lista)

mid  = sum /lenght 

print("Esta é a soma da lista com os números negativos ignorados: ", sum)

print("Esta é a média da lista: ", mid)
