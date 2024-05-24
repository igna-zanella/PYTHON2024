


#usar funcion enumerate para tener el indice y el valor 

# flag1 = 0

# while True:
#     preg = input("diga nro: ")
#     if preg == "si":
#         flag1 == 0
#         print(flag1)
#     elif preg == "no":
#         flag1 = 1
#         print(flag1)
#         break

import random

cant=int(input("Indique cantidad de jugadores: "))
cont=0
puntajes=[]
seguir=[]
lista_jugadores = []

for i in range(cant):
    jugadores = input("¿Cuál es tu nombre? ")
    print("Hola", jugadores, "¡Vamos a jugar! 😏" )
    lista_jugadores.append(jugadores)
    print("Juega el jugador n°: ",cont+1)
    puntaje=0
    dado=random.randint(1,6)
    print("Dado 1:", dado)
    puntaje+=dado
    dado=random.randint(1,6)
    print("Dado 2:",dado)
    puntaje+=dado
    dado=random.randint(1,6)
    print("Dado 3:",dado)
    puntaje+=dado
    print("Puntaje",puntaje)
    flag = True
    seguir.append(flag)

    while seguir[i] == True:
        for x in (seguir):
            if seguir[i] == False:
                if puntaje>18:
                    print("te pasaste")
                    flag = False
                    seguir[i] = flag
                    # print(seguir[i])
                    break
                opc=input("Quiere otro dado? ").upper()
                if opc=="N":
                    print("Puntaje",puntaje)
                    flag = False
                    seguir[i] = flag
                    # print(seguir[i])
                    # break
                elif opc == "S": 
                    dado=random.randint(1,6)
                    print(dado)
                    puntaje+=dado
                    print("Puntaje",puntaje, lista_jugadores[i])
                    flag = True
                    seguir[i] = flag
                    # print(seguir[i])
                else:
                    print(opc,"opción no válida.")
    puntajes.append(puntaje)
    cont+=1

print(seguir)
cont=0
puntmax=0
indice=0


#aca usar for y referenciar al indice y probar
for i in range(cant):
    if seguir[i] < cant:
        print(lista_jugadores[i], puntajes[i])

        

