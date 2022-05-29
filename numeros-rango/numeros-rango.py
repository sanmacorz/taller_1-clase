#!/usr/bin/env python3
# Dado un rango de números enteros, obtener la cantidad de números que contiene

rango = []
rango = [int(item) for item in input ("Digite los valores del rango: ").split()]
print(rango)
print("La cantidad de numeros que contiene son " + str(len(rango)))