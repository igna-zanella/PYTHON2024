
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

print(f""""
    
{AMARILLO}BIENVENIDOS A {FIN_LINEA}
{VERDE}
  ___   _        _   ___ 
 | __| | |      / | ( _ )
 | _|  | |__    | | / _ \\
 |___| |____|   |_| \___/
                         
        .-------.
       /   o   /|
      /_______/o|
      | o     | |
      |   o   |o/
      |     o |/
      '-------'   
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
    print("\nTurno",i)
    numero = 0
    jugadores = input("¿Cuál es tu nombre? ")
    print("Hola", jugadores, "¡Vamos a jugar! 🎲")
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
            print("Sacaste un ", dado)
            print("Hasta acá llevás", numero, "puntos.")
    if numero > 18:
        print("\n¡Perdiste! 🙈")
        i+=1
    else:
        print("\nTe plantaste con", numero, "puntos ✨") #😅😏
        lista_numeros.append(numero)

print(lista_numeros)
maximo = max(lista_numeros)
if lista_numeros.count(maximo) > 1:
    print ("\n¡Empate! 😜")
    print(lista_numeros.count(maximo))
else:
    i = lista_numeros.index(maximo)
    print("\nGanó", lista_jugadores[i],"con", maximo, "puntos 😎")
