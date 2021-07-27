import math as mate
def menuSecundario():
    try:
        print("escribe el valor de a")
        a = int(input())
        print("escribe el valor de b")
        b = float(input())
        print("escribe el valor de c")
        c = float(input())
        try:
            b2 = b**2
            # print(f'b2 = {b2}')
            multiplicacion = 4*a*c
            # print(f'multipliacion {multiplicacion}')
            multiplicacionRaiz = b2-multiplicacion
            # print(f'rmultiplicacion de raiz con 2{multiplicacionRaiz}')
            raiz = mate.sqrt(multiplicacionRaiz)
            # print(raiz)
            arribaPositivo = -b+ raiz
            arribaNegativo = -b- raiz
            abajo = 2*a
            resultadoPositivo = arribaPositivo/abajo
            resultadoNegativo = arribaNegativo/abajo
            print(f'el resultado - = {resultadoNegativo}')
            print(f'el resultado + = {resultadoPositivo}')
        except:
            print("el valor es indefinido")
    except:
        print("lo siento el valor que has introducido no es numerico o el resultado de la operacion es indefinido")

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def printFibonaci(n):
    print("\nesta es la serie fibonaci")
    for x in range(n):
        print(fib(x))

def calcularTablas():
    tabla1 = [i*1 for i in range(1,11)]
    tabla2 = [i*2 for i in range(1,11)]
    tabla3 = [i*3 for i in range(1,11)]
    tabla4 = [i*4 for i in range(1,11)]
    tabla5 = [i*5 for i in range(1,11)]
    tabla6 = [i*6 for i in range(1,11)]
    tabla7 = [i*7 for i in range(1,11)]
    print(f'tabla del 1 {tabla1}')
    print(f'tabla del 2 {tabla2}')
    print(f'tabla del 3 {tabla3}')
    print(f'tabla del 4 {tabla4}')
    print(f'tabla del 5 {tabla5}')
    print(f'tabla del 6 {tabla6}')
    print(f'tabla del 7 {tabla7}')

def menuPrincipal():
    bandera = False
    while bandera==False:
        print("\nestas son tus opciones \n1:serie fibonaci \n2:tablas del 1 al 7\n3:formula ggeneral\n4:salir")
        try:
            opcion = int(input())
            if(opcion>4 | opcion<1): print("no es un numero valido")
            elif(opcion==1):printFibonaci(30)
            elif(opcion==2):calcularTablas()
            elif(opcion==3):menuSecundario()
            elif(opcion==4):bandera=True
        except:
            print("no se acpetan letras")



menuPrincipal()