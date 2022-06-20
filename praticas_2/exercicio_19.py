# Calculando um conjunto de notas de um aluno:

from statistics import mean 


b = []

n = 10

for n in range(10, 20):
    n = int(input("Digite a nota: "))
    if n < 10:
        print("Nota Inválida!")
        break
    elif n > 20:
        print("Nota Inválida")  
        break    
    else:
        b.append(n) 

print(b)

print(mean(b))
