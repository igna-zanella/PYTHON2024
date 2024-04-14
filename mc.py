
# MC
# primero lista de precios
# menu para elegir la hamburguesa
# agrandar o no el combo
# forma de pago si es en efectivo 10% descuento
# si es tarjeta en cuotas que te diga las cuotas
# si es jubilado un 5%
# """

print("""
BIENVENIDOS A MC PYTHON

Combos disponibles:

    1) MC Pollo con Queso $4800
    2) MC Vegana $5500
    3) MC Medallones lomitos $6300
    4) MC Vegana Doble $7800
    5) MC Tasty $9990
    6) MC Whopper $10750
    7) MC Ultra Beef $12350

""")

precios = [4800, 5500, 6300, 7800, 9990, 10750, 12350]
preciosCombo = [1000, 600, 1800]

opcion = int(input("Ingresá el menú que deseás: "))

if opcion > 7 or opcion < 1:
    print("\n", opcion, "no es una opción válida. Reintentalo.")
else:
    # total = precios[opcion-1]
    print("\nTu combo sale $", precios[opcion-1])

    agrandarCombo = input("\n¿Deseás mejorarlo? (sí = S / no = N)" ).upper()

    if agrandarCombo == "S":
        print("""
            \n¡Con estas ofertas agrandás tu COMBO!

        1) Papas extra grandes - $ 1000
        2) Gaseosa tamaño MAX - $ 600
        3) Postre MC Super Cream - $ 1800
        4) mmm... mejor la próxima vez.
            """)
        opcionCombo = int(input("Elegí tu opción: "))
        
        if opcionCombo > 4 or opcionCombo < 1:
            print("\n", opcionCombo, "no es una opción válida. Reinténtelo.")
        elif opcionCombo == 4:
            print("\n¡No hay problema! Vamos al pago")
        else:
            precios[opcion-1] += preciosCombo[opcionCombo-1]
            print("\n¡Agrandaste tu combo! Vamos al pago")
    elif agrandarCombo == "N":
        print("\n¡Perfecto! Vamos al pago")
    else:
        print("\nOpción no válida")

total = precios[opcion-1]

print("\nPromo jubilados de 5%")
jubilado = input("¿Sos jubilado? (sí = S / no = N) ").upper()

if jubilado == "S":
    total = total - (total * .05)
elif jubilado == "N":
    pass
    
print("\nEl precio de tu combo es $", total)


print("""
¿Cómo vas a pagar?
        
    1) EFECTIVO (10% de descuento)
    2) TARJETA DE DÉBITO
    3) TARJETA DE CRÉDITO
        """)
    
pago = input("Elegí una opción: ")

if pago == "1":
    total = total - (total * .10)
    print("\nEl importe total con el descuento es $", total)
    print("Por favor, acercate a la caja con el ticket para finalizar tu compra ¡Disfrutá tu combo!")
    
elif pago == "2":
    print("\nEl importe total es $", precios[opcion-1])
    print("Prepará tu tarjeta y seguí las instrucciones del posnet ¡Disfrutá tu combo!")
elif pago == "3":
    print("""
        PLAN DE CUOTAS
        
        1) 1 cuota (sin interés)
        2) 2 cuotas (interés del 10%)
        3) 3 cuotas (interés del 30%)
        """)

# print(total)
print("\nGracias. Vuelva prontos.")
