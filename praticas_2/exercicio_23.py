# Calculando a média de idades:

from statistics import mean

g = []

for i in range(10):
    i = int(input("Digite a idade: "))
    g.append(i)
    if i > 10:
        break
          
print(g) 

print(mean(g))
