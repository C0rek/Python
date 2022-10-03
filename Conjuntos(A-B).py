#   Creado por ** C0rek **
#   2021


#  Enunciado: Dado 2 vectores A y B de N y M elementos respectivamente. Realice un algoritmo para generar un 
# vector C que contenga solamente los elementos de B que no están en  A


MAX = 32767 # Establesco un maximo para no exceder el programa
#Pide datos de los conjutos

N = int(input("Ingrese la cantidad de elementos de A: "))
if N > MAX:
    print("Rango maximo superado")
else:
    M = int(input("Ingrese la cantidad de elementos de M: "))
    if M > MAX:
        print("Rango maximo superado")

#creo los vectores
A=[]*N
B=[]*M

#se carga el vector A
print("Carguemos A")
for i in range(N):
    aux = int(input("Ingrese el valor: "))
    if aux > MAX:
        print("Rango maximo superado")
    else: 
        A.append(aux)


#se carga el vector B
print("\nCarguemos B")
for j in range(M):
    aux = int(input("Ingrese el valor: "))
    if aux > MAX:
        print("Rango maximo superado")
    else:
        B.append(aux)

#se establece los conjutos
conjunto_1= set(A)
conjunto_2= set(B)

#diferencia entre B y A
diferencia = conjunto_2.difference(conjunto_1)


if diferencia == set():             #Si no hay diferencia
    print("No hay elementos que no esten en A")
else:
    print("Elemento/s que no estan en A:", diferencia)

C = list(diferencia)    #se transforma el set a un vector
