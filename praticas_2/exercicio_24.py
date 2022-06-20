# Calculadora de velocidade:

km = 0

ms = 0

menu = int(input("Escolha a opção desejada: 1 - Km/h para m/s e m/s para Km/h ou 2 - Sair: "))

while menu == 1:
    km = float(input("Digite o Km/h: "))
    ms = float(input("Digite o valor m/s: "))
    ms = km / 3.6
    km = ms * 3.6
    print("A velocidade em m/s é: ", ms)
    print("A velocidade em Km/h é: ", km)
    menu = int(input("Escolha a opção desejada: 1 - Km/h para m/s e m/s para Km/h ou 2 - Sair: "))

if menu == 2:
    print("Saiu!")    
    