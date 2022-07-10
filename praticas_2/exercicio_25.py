# Calculadora com Menu:

print("1 - Adição")

print("2 - Subtração")

print("3 - Multiplicação")

print("4 - Divisão")

print("5 - Sair")

menu = int(input("Digite a Opção Desejada: "))

if menu == 1:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    adicao = n1 + n2
    print(f'A soma dos números é igual a: {adicao}')  
elif menu == 2:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    subtracao = n1 - n2
    print(f'O resultado da subtração é igual a: {subtracao}')
elif menu == 3:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    multplicacao = n1 * n2
    print(f'O produto da multiplicação é igual a: {multplicacao}')
elif menu == 4:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    divisao = n1 / n2
    print(f'O resultado da divisão é igual a: {divisao}')
elif menu == 5:
    print('Saindo...')            