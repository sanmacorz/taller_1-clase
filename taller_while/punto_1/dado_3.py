import random

n = int(input("Digite las veces que quiere tirar el dado: "))
veces_tirado = 0
contador = 0

while veces_tirado < n:
    dado = random.randint(1, 6)
    print(dado)
    if dado == 3:
        contador = contador + 1
    veces_tirado = veces_tirado + 1

print("El número 3 se repite " + str(contador) + " veces.")