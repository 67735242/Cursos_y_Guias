#Escribe un programa que solicité al usuario ingresar cuatro números para luego mostrar el promedio de los tres.

print("                         Ingrese 4 numeros, para mostrar el promedio de tres de ellos: ")
print()
a = float(input("           Ingrese 1er número:"))
b = float(input("           Ingrese 2do número:"))
c = float(input("           Ingrese 3er número:"))
d = float(input("           Ingrese 4to número:"))

x = (a+b+c)/3

print()
print("             El promedio de los tres número es:",round(x,2))
