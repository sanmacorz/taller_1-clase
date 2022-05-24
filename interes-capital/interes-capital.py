#!/usr/bin/env python3
# Calcule e imprima en cuántos meses, uniendo los dos capitales, pueden hacer el negocio que desean.

c1 = int(input("Ingrese una cantidad: "))
c2 = int(input("Ingrese una cantidad: "))
c3 = int(input("Ingrese una cantidad: "))
meses = 0

while (c1 + c2) < c3:
    c1 += (c1 * 0.03)
    c2 += (c2 * 0.04)
    meses += 1
    
print("Para alcanzar el capital deseado de " + str(c3) + " pesos, se tardarían un total de " + str(meses) + " meses.")