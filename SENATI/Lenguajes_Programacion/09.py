print("\n____________________________________________________________________________________________")
print("\n--------------------------------------------------------------------------------------------")
print()
print("                                 Bienvenid@ al interfaz de compra")
print()
print("\n____________________________________________________________________________________________")
print("\n--------------------------------------------------------------------------------------------")
print()


salsa = 56
rock = 63
pop = 87
folclore = 120.5

compra = input("                ¿Qué discos deesa comprar? (salsa, rock, pop, folclore): ")
print()

cantidad = int(input("                ¿Cuántos discos desea comprar? "))
print()

if compra=="salsa":
    if 1<= cantidad <=3:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"nPrecio S/:",cantidad*salsa," \nDescuento: Ninguno","\nNuevo precio a pagar S/:", cantidad*salsa)
    
    elif cantidad==4:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*salsa," \nDescuento: 6% equivalente a S/:",(((cantidad*salsa)*4)/100),"\nNuevo precio a pagar S/:", (cantidad*salsa)-(((cantidad*salsa)*4)/100))
    
    elif 5<=cantidad<=10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*salsa," \nDescuento: 8% equivalente a S/:",(((cantidad*salsa)*8)/100),"\nNuevo precio a pagar S/:", (cantidad*salsa)-(((cantidad*salsa)*8)/100))
        
    elif cantidad>10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*salsa," \nDescuento: 10.2% equivalente a S/:",(((cantidad*salsa)*10.2)/100),"\nNuevo precio a pagar S/:", (cantidad*salsa)-(((cantidad*salsa)*10.2)/100))

elif compra=="rock":
    if 1<= cantidad <=3:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"nPrecio S/:",cantidad*rock," \nDescuento: Ninguno","\nNuevo precio a pagar S/:", cantidad*rock)
    
    elif cantidad==4:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*rock," \nDescuento: 6% equivalente a S/:",(((cantidad*rock)*4)/100),"\nNuevo precio a pagar S/:", (cantidad*rock)-(((cantidad*rock)*4)/100))
    
    elif 5<=cantidad<=10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*rock," \nDescuento: 8% equivalente a S/:",(((cantidad*rock)*8)/100),"\nNuevo precio a pagar S/:", (cantidad*rock)-(((cantidad*rock)*8)/100))
        
    elif cantidad>10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*rock," \nDescuento: 10.2% equivalente a S/:",(((cantidad*rock)*10.2)/100),"\nNuevo precio a pagar S/:", (cantidad*rock)-(((cantidad*rock)*10.2)/100))
        
elif compra=="pop":
    if 1<= cantidad <=3:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"nPrecio S/:",cantidad*pop," \nDescuento: Ninguno","\nNuevo precio a pagar S/:", cantidad*pop)
    
    elif cantidad==4:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*pop," \nDescuento: 6% equivalente a S/:",(((cantidad*pop)*4)/100),"\nNuevo precio a pagar S/:", (cantidad*pop)-(((cantidad*pop)*4)/100))
    
    elif 5<=cantidad<=10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*pop," \nDescuento: 8% equivalente a S/:",(((cantidad*pop)*8)/100),"\nNuevo precio a pagar S/:", (cantidad*pop)-(((cantidad*pop)*8)/100))
        
    elif cantidad>10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*pop," \nDescuento: 10.2% equivalente a S/:",(((cantidad*pop)*10.2)/100),"\nNuevo precio a pagar S/:", (cantidad*pop)-(((cantidad*pop)*10.2)/100))

elif compra=="folclore":
    if 1<= cantidad <=3:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"nPrecio S/:",cantidad*folclore," \nDescuento: Ninguno","\nNuevo precio a pagar S/:", cantidad*folclore)
    
    elif cantidad==4:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*folclore," \nDescuento: 6% equivalente a S/:",(((cantidad*folclore)*4)/100),"\nNuevo precio a pagar S/:", (cantidad*folclore)-(((cantidad*folclore)*4)/100))
    
    elif 5<=cantidad<=10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*folclore," \nDescuento: 8% equivalente a S/:",(((cantidad*folclore)*8)/100),"\nNuevo precio a pagar S/:", (cantidad*folclore)-(((cantidad*folclore)*8)/100))
        
    elif cantidad>10:
        print("Compra: ",compra,"\nCantidad: ",cantidad,"\nPrecio S/:",cantidad*folclore," \nDescuento: 10.2% equivalente a S/:",(((cantidad*folclore)*10.2)/100),"\nNuevo precio a pagar S/:", (cantidad*folclore)-(((cantidad*folclore)*10.2)/100))
                
else:
    print()
    print("                          \nEl disco solicitado no exite o aún no está disponible.")
    print("                                        \nGracias por su comprensión")
    print()

print()
print("\n                           Su compra fue realizada con exito")
print("\n                   Gracias por su compra, agradecemos su preferencia ")
print()
print()