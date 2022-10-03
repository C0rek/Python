'''
CONSIGNA:
    Se posee una Base de Datos de Clientes (Código, Nombre, Saldo deudor de la cuenta) de una empresa almacenado en una matriz strings de N 
filas por 3 columnas. Los datos de los clientes están ordenados por código de cliente.
Realice un menú en que invoque procedimientos y/o funciones para realizar lo siguiente:

a) Cargar la matriz. Recordar que la matriz tiene debe estar ordenada por código
b) Insertar un nuevo cliente manteniendo la matriz ordenada por código. Antes de insertar debe verificar que el cliente no exista. (verificación por código).
c) Buscar y mostrar el saldo de un cliente determinado. (debe ingresar un código y mostrar un error si no existe)
d) Buscar y mostrar el saldo a cobrar por la empresa. (recuerde que la matriz contiene string por lo cual deberátransformar los saldos en números para sumar), indicando además quien es el mayor deudor.
'''

def cargar_datos():
    N = int(input("Ingrese cuantos clientes desea agregar:"))
    matriz=[[0 for i in range(3)] for j in range(N)]
    for i in range (N):
        matriz[i][0]=int(input("Ingrese el codigo del cliente:"))
        matriz[i][1]=input("Ingrese el nombre del cliente:")
        matriz[i][2]=float(input("Ingrese el saldo de la cuenta del cliente:"))
    print(sorted(matriz,key=lambda x:x[0]))
    return matriz


def nuevo_cliente(X):
    lista=[]
    for i in range (1):
        codigo = int(input("Ingrese el codigo del cliente:"))
        lista.append(codigo)
        nombre=input("Ingrese el nombre del cliente:")
        lista.append(nombre)
        saldo=float(input("Ingrese el saldo de la cuenta del cliente:"))
        lista.append(saldo)
    matriz.append(lista)
    print(sorted(matriz,key=lambda x:x[0]))


def buscar_saldo(X):
    cliente=input("Ingrese el nombre del cliente: ")
    c=0
    for i in range (len(matriz)):
        if cliente==matriz[i][1]:
            c=c+1
            print(matriz[i])
    if c==0:
        print("Ese cliente no existe")
        return

def buscar_cobro_total(X):
    aux=0
    mayor=matriz[0][2]
    for i in range(len(matriz)):
        if (mayor<matriz[i][2]):
            mayor=matriz[i]
        aux = aux+matriz[i][2]
    print("Monto total a cobrar por la empresa: ",aux)
    print("El cliente que mas debe es: ",mayor)
def menu():
    print("(1) - Cargar matriz ")
    print("(2) - Insertar nuevo cliente")
    print("(3) - Buscar saldo del cliente")
    print("(4) - Buscar el saldo a cobrar por la empresa")
    print("(5) - Salir")


#main
matriz=[]
lista=[]
while True:
    menu()
    a =int(input("Ingrese una opcion:"))
    while( a>0 and a<6 ):
        if a == 1 :
            matriz=cargar_datos()
            break
        if a == 2 :
            nuevo_cliente(matriz)
            break
        if a == 3 :
            buscar_saldo(matriz)
            break
        if a == 4 :
            buscar_cobro_total(matriz)
            break
        if a == 5 : 
            quit()   
    else:
        print("Ingrese una opcion correcta")