#Consigna
"""
    Se desea elaborar un programa que simule la atención de pacientes en un consultorio. Se debe crear una lista de pacientes que esperan ser atendidos. 
Inicialmente la lista de espera está vacía y los pacientes se atienden por orden de llegada. A medida que llegan los pacientes se agregan después del último, salvo
que la atención del nuevo paciente sea una urgencia, en este caso se lo agrega al comienzo de la lista. 
Realice un menú que invoque a módulos para realizar lo siguiente:
a) Ingresar un nuevo paciente a la lista de espera.
b) Indicar cuál es el paciente a ser atendido, atenderlo y eliminarlo de la lista.
c) Registrar un paciente con urgencia, arreglar la lista y además, guardarlo en otra lista
d) Determinar cuántos pacientes esperan para ser atendidos antes que un paciente X.
e) Mostrar cuántos pacientes se atendieron desde el comienzo, y cuántos faltan atender
f) Mostrar la lista de pacientes que se atendieron con urgencia.
"""

def cargar_paciente():
    print("Ingrese el nombre del paciente a ingresar")
    nombre=input("> ")
    cargar=pacientes.append(nombre)
    print(pacientes)

def turno_paciente():
    print("\nEl paciente a ser atendido es:" ,pacientes[0])
    eliminar=pacientes.pop(0)
    print("\nLista de espera",pacientes)

def paciente_urgencias():
    print("Ingrese el nombre del paciente para urgencias")
    nombre=input("> ")
    pacientes.insert(0,nombre)
    espera=pacientes        #lo guardo en otra lista
    print(pacientes)


def menu():
    print("(1) - Ingresar paciente a la lista de espera")
    print("(2) - Indicar proximo paciente")
    print("(3) - Registrar un paciente con urgencia")
    print("(4) - Pacientes espera")
    print("(5) - Mostrar pacientes ")
    print("(6) - Salir")

#main
pacientes=["Ginebra"]
while True:
    print()
    print("Menu")
    menu()
    a =int(input("Ingrese una opcion:"))
    while( a>0 and a<7):
        if a == 1 :
            cargar_paciente()
            break
        if a == 2 :
            turno_paciente()
            break
        if a == 3 :
            paciente_urgencias()
            break
        if a == 4 :

            break
        if a == 5 :
            break
        if a == 6 : 
            quit()   
    else:
        print("Ingrese una opcion correcta")
