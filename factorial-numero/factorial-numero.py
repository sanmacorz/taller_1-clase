#!/usr/bin/env python3
# Calcular un número n, entero y positivo, y calcule su factorial e imprimalo junto con el número leído.

numero = int(input("Ingrese un número: "))
i = numero
resultado = 1

while i >= 1:
    resultado *= i
    i -= 1
    
print("El factorial de " + str(numero) + " es " + str(resultado))