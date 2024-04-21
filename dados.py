
import random ### para realizar un entero pidiendo rango

# print(""""
# Bienvenidos al 18 

# no te pases del 18 si queres ganar
# """)

# i=0
# cant = int(input("Ingrese cantidad de jugadores: "))
# dec = "si" 

# while i <= cant:
#     j1 = input("Ingrese su nombre: ")
#     input("ENTER para tirar")
#     i = i+1
#     total=0
#     while True:
#         dec=input("¿Tira otra vez?: ")
#         if dec == "si":
#             print(i)
#             dado = random.randint(1, 6)
#             print(j1,"Su número es",dado)
#             total+=dado
#         elif dec == "no":
#             break
#         print("Su puntaje es", total)
        

# alt 219 █
# alt 220 ▄
# alt 223 ▀

# print("""
#     █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
#     █                  █
#     █                  █
#     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
#     """)
# by jgs
#
# alt 179 │
# alt 191 ┐
# alt 192 └
# alt 196 ─
# alt 217 ┘
# alt 218 ┌
# alt 7 •

print('''
    ┌─────────┐
    │         │
    │    •    │
    │         │ 
    └─────────┘
    ┌─────────┐
    │      •  │
    │         │
    │  •      │ 
    └─────────┘
    ┌─────────┐
    │      •  │
    │    •    │
    │  •      │ 
    └─────────┘
    ┌─────────┐
    │  •   •  │
    │         │
    │  •   •  │
    └─────────┘
    ┌─────────┐
    │  •   •  │
    │    •    │
    │  •   •  │
    └─────────┘
    ┌─────────┐
    │  •   •  │
    │  •   •  │
    │  •   •  │
    └─────────┘
    ''')


import random

ROJO = '\033[31m'
VERDE = '\033[92m'
FIN_LINEA = '\033[0m'
NEGRO   = '\033[30m'
AMARILLO  = '\033[33m'
AZUL    = '\033[34m'
MAGENTA = '\033[35m'
CIAN    = '\033[36m'
BLANCO   = '\033[37m'

lado_1 = f'''{VERDE}
    ┌─────────┐
    │         │
    │    •    │
    │         │
    └─────────┘
'''
lado_2 = f'''{VERDE}
    ┌─────────┐
    │      •  │
    │         │
    │  •      │
    └─────────┘
'''
lado_3 = f'''{VERDE}
    ┌─────────┐
    │      •  │
    │    •    │
    │  •      │
    └─────────┘
'''
lado_4 = f'''{VERDE}
    ┌─────────┐
    │  •   •  │
    │         │
    │  •   •  │
    └─────────┘
'''
lado_5 = f'''{VERDE}
    ┌─────────┐
    │  •   •  │
    │    •    │
    │  •   •  │
    └─────────┘
'''
lado_6 = f'''{VERDE}
    ┌─────────┐
    │  •   •  │
    │  •   •  │
    │  •   •  │
    └─────────┘
'''

# print(f""""

# {AMARILLO}
# BIENVENIDOS A {FIN_LINEA}
# {VERDE}
#                  ___   _        _   ___ 
#                 | __| | |      / | ( _ )
#                 | _|  | |__    | | / _ \\
#                 |___| |____|   |_| \___/
                                        
#                       .-------.
#                      /   o   /|
#                     /_______/o|
#                     | o     | |
#                     |   o   |o/
#                     |     o |/
#                     '-------'   
# {FIN_LINEA}{AMARILLO}
# ... tirá el dado y no te pasés de 18 si querés ganar 🤩
# {FIN_LINEA}

# """)
print(f""""

{AMARILLO}
BIENVENIDOS A {FIN_LINEA}
{VERDE}
                 ___   _        _   ___ 
                | __| | |      / | ( _ )
                | _|  | |__    | | / _ \\
                |___| |____|   |_| \___/
                                        
            ┌─────────┐ ┌─────────┐ ┌─────────┐
            │  •   •  │ │  •   •  │ │  •   •  │
            │  •   •  │ │  •   •  │ │  •   •  │
            │  •   •  │ │  •   •  │ │  •   •  │
            └─────────┘ └─────────┘ └─────────┘
    
{FIN_LINEA}{AMARILLO}
... tirá el dado y no te pasés de 18 si querés ganar 🤩
{FIN_LINEA}

""")

cant_jugadores = int(input("Ingresá la cantidad de jugadores: "))
lista_numeros = []
lista_jugadores = []
# for x in range(cant_jugadores):

i=1
while i <= cant_jugadores:
    print(AMARILLO + "\nTurno",str(i) + FIN_LINEA)
    numero = 0
    jugadores = input("¿Cuál es tu nombre? ")
    print(AMARILLO + "Hola", jugadores, "¡Vamos a jugar! 😏" + FIN_LINEA)
    lista_jugadores.append(jugadores)
    while True and numero < 19:
        rep = input("'S' para tirar el dado o 'N' para retirarte: ").upper()
        if rep == "N":
            print("bye bye")
            i+=1
            break
        elif rep == "S":
            dado = random.randint(1,6)
            numero += dado
            print(VERDE + "Sacaste un ", str(dado), "🎲" + FIN_LINEA)
            if dado == 1:
                print(lado_1)
            elif dado == 2:
                print(lado_2)
            elif dado == 3:
                print(lado_3)
            elif dado == 4:
                print(lado_4)
            elif dado == 5:
                print(lado_5)
            else:
                print(lado_6)
            print(AMARILLO + "Hasta acá llevás", str(numero), "puntos." + FIN_LINEA)
    if numero > 18:
        print(ROJO + "\n¡Perdiste! 🙈" + FIN_LINEA)
        i+=1
    else:
        print(AMARILLO + "\nTe plantaste con", str(numero), "puntos 😅" + FIN_LINEA)
        lista_numeros.append(numero)

print(lista_numeros)
if lista_numeros == []:
    print(ROJO + "¡¡¡Todos pierden!!! 😭" + FIN_LINEA)
else:
    maximo = max(lista_numeros)
    if lista_numeros.count(maximo) > 1:
        print (AMARILLO + "\n¡Empate! 😜" + FIN_LINEA)
        print(lista_numeros.count(maximo))
    else:
        i = lista_numeros.index(maximo)
        print(VERDE + "\nGanó", lista_jugadores[i],"con", str(maximo), "puntos 😎" + FIN_LINEA)
