n = int(input("Digite un número: "))
contador = 0
lista = []
while contador < n:
    contador = contador +1
    if (contador % 5) == 0:
        lista.append(str(contador))

print(lista)