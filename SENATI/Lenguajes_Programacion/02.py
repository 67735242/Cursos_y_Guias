#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta.
#Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida.

print("             Ingrese la cantidad de presupuesto invertido:")
print()

a = int(input("     Primer inversor:"))
b = int(input("     Segundo Inversor:"))
c = int(input("     Tercer inversor:"))

total = (a+b+c)

print()
print()
print("     El porcentaje del 1er inversor es:",(a*100)/total,"%")
print("     El porcentaje del 2do inversor es:",(b*100)/total,"%")
print("     El porcentaje del 3do inversor es:",(c*100)/total,"%")
print()