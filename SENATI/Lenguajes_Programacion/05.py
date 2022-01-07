#Diseñe un algoritmo que lea tres números y determine el número mayor.#

print()
print("                     Bienvenido al interfaz de cálculo")
print()
print("             Ingrese los datos para hallar el número mayor: ")
print()
print()

A = int(input("       Ingrese 1er número:"))
B = int(input("       Ingrese 2do número:"))
C = int(input("       Ingrese 3er número:"))

if(A>B and A>C):
    print()
    print("     El número mayor es: ",A)

else:
    if(B>A and B>C):
        print()
        print("     El número mayor es: ",B)
    else:
        print()
        print("     El número mayor es: ",C)
