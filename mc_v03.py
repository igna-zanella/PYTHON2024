# # MC
# primero lista de precios
# menu para elegir la hamburguesa
# agrandar o no el combo
# forma de pago si es en efectivo 10% descuento
# si es tarjeta en cuotas que te diga las cuotas
# si es jubilado un 5%
# """
# alt 185 ╣
# alt 186 ║
# alt 187 ╗
# alt 188 ╝
# alt 200 ╚
# alt 201 ╔
# alt 202 ╩
# alt 203 ╦
# alt 204 ╠
# alt 205 ═
# alt 206 ╬
#

while True:
    print('\033[33m' + """
    TE DAMOS LA BIENVENIDA A MC PYTHON

    Combos disponibles:

        ╔═════════════════════════════════════╗
        ║                                     ║
        ║  1) MC Pollo con Queso_____ $4800   ║
        ║  2) MC Vegana______________ $5500   ║
        ║  3) MC Medallones lomitos__ $6300   ║
        ║  4) MC Vegana Doble________ $7800   ║
        ║  5) MC Tasty_______________ $9990   ║
        ║  6) MC While______________ $10750   ║
        ║  7) MC Ultra Beef_________ $12350   ║
        ║  8) SALIR                           ║
        ║                                     ║
        ╚═════════════════════════════════════╝  

    """ + '\033[0m')

    precios = [4800, 5500, 6300, 7800, 9990, 10750, 12350]
    preciosCombo = [1250, 690, 1830]

    opcion = input("Ingresá el menú que deseás: ")

    if opcion == "8":
        print('\033[33m' + "\n¡Te esperamos pronto!" + '\033[0m')
        exit()
    elif opcion.isalpha() or int(opcion) > 7 or int(opcion) < 1:
        print('\033[31m' + "\n", opcion, "no es una opción válida. Reintentalo." + '\033[0m')
    else:
        # total = precios[opcion-1]
        # print("\nTu combo sale $" , precios[int(opcion-1)])
        print("\nTu combo sale " + '\033[32m' + "$" + str(precios[int(opcion)-1]) + '\033[0m')
        
        while True:
            print('\033[33m' + """
        \n¡Con estas ofertas agrandás tu COMBO!

        ╔═════════════════════════════════════════╗
        ║                                         ║
        ║  1) Papas extra grandes________ $1250   ║
        ║  2) Gaseosa tamaño MAX__________ $690   ║
        ║  3) Postre MC Super Cream______ $1830   ║
        ║  4) mmm... mejor la próxima vez         ║
        ║                                         ║
        ╚═════════════════════════════════════════╝

        """ + '\033[0m')
            opcionCombo = input("Elegí tu opción: ")
            
            if opcionCombo == "4":
                print("\n¡No hay problema! Vamos al pago")
                break
            elif opcionCombo.isalpha() or int(opcionCombo) > 4 or int(opcionCombo) < 1:
                print('\033[31m' + "\n", opcionCombo, "no es una opción válida. Reintentalo." + '\033[0m')
            else:
                precios[int(opcion)-1] += preciosCombo[int(opcionCombo)-1]
                print("\n¡Agrandaste tu combo! Vamos al pago")
                print("Hasta acá pagás " + '\033[32m' + "$" + str(precios[int(opcion)-1]) + '\033[0m')
                break
        break

total = precios[int(opcion)-1]
# jubilado = None
n = True

while n:
    print('\033[33m' + "\n¡Promo jubilados/as! 👵 Descuento del 5% 👴" + '\033[0m')
    jubilado = input("¿Sos jubilado/a? (S = sí / N = no) ").upper()
    
    if jubilado == "S":
        total = total - (total * .05)
        n = False
    elif jubilado == "N":
        n = False
    else:
        print('\033[31m' + "\nOpción no válida" + '\033[0m')
    
print("\nEl precio final de tu combo es " + '\033[32m' + "$" + str(total) + '\033[0m')

n = True
while n:    
    print('\033[33m' + """
    ¿Cómo vas a pagar?

    ╔═══════════════════════════════════╗
    ║                                   ║
    ║  1) EFECTIVO (10% de descuento)   ║
    ║  2) TARJETA DE DÉBITO             ║
    ║  3) TARJETA DE CRÉDITO            ║
    ║                                   ║
    ╚═══════════════════════════════════╝            

            """ + '\033[0m')

    pago = input("Elegí una opción: ")

    if pago == "1":
        total = total - (total * .10)
        # print("\nEl importe total con el descuento es $", total)
        print("\nEl importe total con el descuento es " + '\033[32m' + "$" + str(total) + '\033[0m')
        print('\033[33m' + "Por favor, acercate a la caja con el ticket para finalizar la compra ¡Disfrutá tu combo!" + '\033[0m')
        n = False
    elif pago == "2":
        print("\nEl importe total es " + '\033[32m' + "$" + str(total) + '\033[0m')
        print('\033[33m' + "Prepará tu tarjeta y seguí las instrucciones del posnet ¡Disfrutá tu combo!" + '\033[0m')
        n = False
    elif pago == "3":
        # c = True
        while True:
            print('\033[33m' + """
    ╔═══════════════════════════════════╗
    ║                                   ║
    ║         PLAN DE CUOTAS            ║
    ║                                   ║
    ║  1) 1 cuota (sin interés)         ║
    ║  2) 2 cuotas (interés del 25%)    ║
    ║  3) 3 cuotas (interés del 35%)    ║
    ║                                   ║
    ╚═══════════════════════════════════╝ 
                
                """ + '\033[0m')
            cuota = input("Elegí la cantidad de cuotas: ")

            if cuota == "1":
                print("\nEl importe total es " + '\033[32m' + "$" + str(total) + '\033[0m')
                # c = False
                break
            elif cuota == "2":
                total = total + (total * .25) 
                # print("\nEl importe total es $", '\033[32m' + str(total) + '\033[0m', "en 2 cuotas de $", '\033[32m' + str(round(total/2, 2)) + '\033[0m')
                print("\nEl importe total es " + '\033[32m' + "$" + str(round(total,2)) + '\033[0m', "en 2 cuotas de " + '\033[32m' + "$" + '\033[32m' + str(round(total/2, 2)) + '\033[0m')
                # c = False
                break
            elif cuota == "3":
                total = total + (total * .35) 
                print("\nEl importe total es " + '\033[32m' + "$" + str(round(total,2)) + '\033[0m', "en 3 cuotas de " + '\033[32m' + "$" + '\033[32m' + str(round(total/3, 2)) + '\033[0m')
                # c = False
                break
            else:
                print('\033[31m' + "\nOpción no válida" + '\033[0m')
        print('\033[33m' + "Prepará tu tarjeta y seguí las instrucciones del posnet ¡Disfrutá tu combo!" + '\033[0m')
        n = False
    else:
        print('\033[31m' + "\nOpción no válida" + '\033[0m')
            

# print(total)
print('\033[33m' + "\n¡Gracias por elegirnos!" + '\033[0m')