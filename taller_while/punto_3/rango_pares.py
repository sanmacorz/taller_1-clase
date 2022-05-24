rango = []
rango = [int(item) for item in input ("Digite los valores del rango: ").split()]

if (rango % 2) == 0:
    z = "El número es par"
    print(z) 
else:
    z = "El número es impar"
    print(z)