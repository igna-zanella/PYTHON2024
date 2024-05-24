

#usar funcion enumerate para tener el indice y el valor 

import random
cant=int(input("Indique cantidad de jugadores: "))
cont=0
puntajes=[]
seguir=[True]
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
    while True:
        if puntaje>18:
            print("te pasaste")
            flag = True
            seguir.append(flag)
            break
        opc=input("Quiere otro dado? ").upper()
        if opc=="N":
            print("Puntaje",puntaje)
            break
        elif opc == "S": 
            dado=random.randint(1,6)
            print(dado)
            puntaje+=dado
            print("Puntaje",puntaje)
        else:
            print(opc,"opción no válida.")
    puntajes.append(puntaje)
    cont+=1
print(puntajes)
cont=0
puntmax=0
indice=0
#aca usar for y referenciar al indice y probar
while cont<cant: 
    if puntajes[cont]>puntmax and puntajes[cont]<=18:
        puntmax=puntajes[cont]
        indice=cont
    cont+=1
print(puntmax, indice+1)