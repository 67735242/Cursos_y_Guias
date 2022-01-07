#Diseñe un algoritmo que verifique si la cantidad de dígitos ingresados de un DNI es correcta o no (el DNI tiene 8 dígitos).

print()
print("                                        Algoritmo de verificación de digitos - DNI")
print()
print("                        Ingrese los dígitos del DNI para validar si la cantidad es correcta o no: ")
print()
print()

a = input("             Ingrese los números del DNI:")
codigo=len(a)

if codigo>8:
    print()
    print("             Los datos son incorrectos:")
    print()

elif codigo<8:
    print()
    print("             Los datos son incorrectos:")
    print()


else:
    print()
    print("             Los datos son correctos:")
    print()