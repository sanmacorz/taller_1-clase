numero = str(input("Ingrese un número: "))
longitud = str(len(str(numero)))
indice = 1
inverso = ""

while indice <= int(longitud):
    valor = str(numero[-indice])
    indice += 1
    inverso = inverso + str(valor)
print(inverso)

if numero == inverso:
    print("El número " + str(numero) + " SÍ es capicúa!")
else:
    print("El número " + str(numero) + " NO es capicúa!")