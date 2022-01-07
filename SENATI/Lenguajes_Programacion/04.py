#Ingresar 2 números y luego escoger la operación que se quiere hacer con ellos
#(suma, resta, multiplicación o división) y reportar el resultado.

print()
print("                     Bienvenido al interfaz de operaciones básicas")
print()
print("             Ingrese los datos respectivos para realizar la operación deseada: ")
print()
print()

num_1 = int(input("         1er número: "))
num_2 = int(input("         2do número: "))

print()
operacion = input("         suma, resta, division, multiplicacion: ")
print()

if operacion == "suma":
    print("         El resultado de la operación es:",(num_1+num_2))
    print()

if operacion == "resta":
    print("         El resultado de la operación es:",(num_1-num_2))
    print()

if operacion == "division":
    print("         El resultado de la operación es:",(num_1/num_2))
    print()

if operacion == "multiplicacion":
    print("         El resultado de la operación es:", (num_1*num_2))
    print()