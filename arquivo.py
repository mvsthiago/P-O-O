from random import sample
i = 0
while i != 1:
    numero = sample(range(0,60),6)
    i = i + 1
numero.sort()
print(numero)
