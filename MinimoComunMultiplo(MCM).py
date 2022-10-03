#Creado por C0rek 10/08/21

# Consigna: Dado dos números naturales determinar el Mínimo Común Múltiplo de esos 2 números. Realizar programa en Python. 

def MCM(x,y):
    z = max(x,y)
    while True:
        if( z % x == 0) and ( z % y == 0 ) :
            return z
        z += 1


#main
A = int(input("Ingrese un numero positivo: "))
if (A>0):
    B = int(input("Ingrese otro numero positivo: "))
    if (B>0):
        print("El MCM entre",A, "y" ,B,"es", MCM(A,B))
    else:
        print("ERROR!\nIngrese un numero entero")
else:
    print("ERROR!\nIngrese un numero entero")

