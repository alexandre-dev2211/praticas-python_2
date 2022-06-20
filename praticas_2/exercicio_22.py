# Calculo de associação de resistores em paralelo:

r1 = 0

r2 = 0

while r1 == 0:
    r1 = float(input("Digite o valor do Resistor 1: "))

while r2 == 0:
    r2 = float(input("Digite o valor do Resistor 2: "))

r = r1 * r2 / r1 + r2     

print("A associação dos Resistores informados é igual á: ", r)
