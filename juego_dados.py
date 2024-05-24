
import random
cant=int(input("Indique cantidad de jugadores: "))
puntajes=[]
nombres=[]
seguir=[]
for i in range(cant):
    nombre=input("Ingrese nombre: ")
    nombres.append(nombre)
    print("Juega el jugador :",nombre)
    puntaje=0
    dado=random.randint(1,6)
    print("Dado 1: ",dado)
    puntaje+=dado
    dado=random.randint(1,6)
    print("Dado 2: ",dado)
    puntaje+=dado
    dado=random.randint(1,6)
    print("Dado 3: ",dado)
    puntaje+=dado
    print("Puntaje ",puntaje)
    puntajes.append(puntaje)
    seguir.append(True)

flag=0
while flag<cant:
    for i in range(cant):
        if seguir[i]==True:
            if puntajes[i]>18:
                print("¡Te pasaste! 🙃")
                flag+=1
                seguir[i]=False
            else:
                print("Puntaje de",nombres[i],puntajes[i])
                print("¿"+nombres[i]+" quiere otro dado? 🎲")
                opc=input()
                if opc=="n":
                    flag+=1
                    seguir[i]=False
                if seguir[i]==True:
                    dado=random.randint(1,6)
                    print(dado)
                    puntajes[i]+=dado
                    print("Puntaje de",nombres[i],puntajes[i])
puntmax=0
indice=""
for i in range(cant):
    if puntajes[i]>puntmax and puntajes[i]<=18:
        puntmax=puntajes[i]
        indice=i
if puntmax==0:
    print("¡Se pasaron todos! 🙃")
else:
    maximo = max(puntajes)
    if puntajes.count(maximo) > 1:
        print ("\n¡Empate! 😜")
        # print(puntajes.count(maximo))
    else: 
        print("Ganador:",nombres[indice],puntajes[indice], "😎")
print("\nResultados finales:")
for i in range(cant):
    print(nombres[i],puntajes[i])