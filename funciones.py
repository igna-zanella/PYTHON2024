def saludar():
    print("Hola mundo")
def tabla_del5():
    for i in range(1,11):
        print(f"5 x {i} = {5*i}")
def imprimir(num):
    print(num)
def multiplicar(num1=1,num2=1):
    return num1*num2
def dividir(num1,num2):
    return num1/num2
def sumar5(num):
    num+=5
    print(num)
def pasarimpares(numeros):
    for i in range(0,len(numeros)):
        numeros[i]+=1
def main():
    saludar()
    tabla_del5()
    n=20
    imprimir(20)
    print(multiplicar(7,10))#o lo pueden guardar resultado=multiplicar(2,5)
    print(dividir(3,6))
    print(dividir(6,3))
    print(multiplicar(15))

    num=45
    print(num)
    sumar5(num)
    print(num)
    numeros=[2,4,6]
    print(numeros)
    pasarimpares(numeros)
    print(numeros)
main()
