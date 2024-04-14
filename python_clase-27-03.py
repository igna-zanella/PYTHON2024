
# Ejercicio 1
# Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiente con mostrar True o False):
# •	Si los dos números son iguales
# •	Si los dos números son diferentes
# •	Si el primero es mayor que el segundo
# •	Si el segundo es mayor o igual que el primero


print("\nIngrese dos números para averiguar si son iguales o cuál es el mayor: ")
num1 = int(input("\nPrimer Número: "))
num2 = int(input("Segundo Número: "))

if num1 == num2:
    print("\nLos números son iguales")
elif num1 != num2:
    if num1 > num2:
        print("\nLos números son diferentes y el primero es el mayor.")
    else:
        print("\nLos números son diferentes y el segundo es el mayor.")

# Ejercicio 2
# Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiente con mostrar True o False).

cadena = input("\nIngrese un texto para determinar si su longitud es menor e igual a 3 caracteres o mayor a 10: ")

if len(cadena) >=3 and len(cadena) <10:
    print(True)
else:
    print(False)

# Ejercicio 3
# Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
# •	Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# •	Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
# •	Multiplica el numero_usuario por 9 en sí mismo
# •	Multiplica el numero_magico por el numero_usuario en sí mismo
# •	Finalmente muestra el valor final del numero_usuario por pantalla

numero_magico = 12345679
numero_usuario = int(input("\nIngrese un número entero entre 1 y 9 para obtener un número mágico: "))

if numero_usuario > 0 and numero_usuario < 10:
    numero_usuario*=9
    # print(numero_usuario)
    numero_usuario *= numero_magico
    print("\nSu número mágico es: ", numero_usuario)
else:
    print("\nEl número que ingresó no es válido.")
    

# def saludar (nombre):
#     print("Hola",nombre)
    
# n = input("Ingrese su nombre: ")
# saludar(n)

# Ejercicio 4
# Realizar una calculadora con menú para cada operación.

print("\nIngrese dos números para realizar una operación aritmética: ")

num1 = int(input("\nPrimer número: "))
num2 = int(input("Segundo número: "))

print("\n¿Qué operación desea realizar? \n\n 1.- \033[92mSuma\033[0m\n 2.- \033[92mResta\033[0m\n 3.- \033[92mMultiplicación\033[0m\n 4.- \033[92mDivisión\033[0m\n \033[31mDIGITE '0' PARA SALIR\033[0m")

opcion = int(input("\nElija una opción: "))

if opcion == 1 and opcion !=0:
    print("El resultado de la suma es:",num1 + num2)
elif opcion == 2 and opcion !=0:
    print("El resultado de la resta es:",num1 - num2)
elif opcion == 3 and opcion !=0:
    print("El resultado de la multiplicación es:",num1 * num2)
elif opcion == 4 and opcion !=0:
    print("El resultado de la división es:",num1 / num2)
else:
    print("\nGracias. Vuelva prontos.")
    


