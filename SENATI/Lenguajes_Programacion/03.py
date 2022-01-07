#Calcular el sueldo de un empleado, ingrese los siguientes datos: nombre, horas de trabajo y el salario por hora.
#Luego incrementar el sueldo en 15%.

print("                                         Bienvenido al interfaz de cálculo")
print()
print("                             En el presente formulario ingrese sus datos segun corresponda")
print()
print()

a = input("         Ingrese su nombre y apellido: ")
b = int(input("         Ingrese el monto de su salario: "))
c = int(input("         Ingrese el monto de su salario por horas de trabajo: "))

q =b*c
w =(b*c)*0.15
e =q+w

print()
print("         Le corresponde un sueldo es de $:",e)
print()