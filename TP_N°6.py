"""1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
    a) Llevar un registro de todos los datos de alumnos de la escuela (Nombre,
    Apellido, fecha de nacimiento, DNI, Nombre de Tutor, registro de todas las
    notas, cantidad de faltas, cantidad de amonestaciones recibidas.
    Recomendación: Para llevar un registro de estos dato se puede
    utilizar un diccionario estructurado de la siguiente manera:
    {
    “Alumnos” : [alumno1,alumno2,alumno3 ]
    }
    Donde cada alumno es otro diccionario estructurado de la
    siguiente forma:
    {
    “Nombre”: nombre de alumno,
    “Apellido” : apellido de alumno,
    “DNI” : DNI de alumno
    “Fecha de nacimiento”, fecha de nacimiento de alumno,
    “Tutor” : nombre y apellido de tutor,
    “Notas” : todas las notas del alumno,
    “Faltas” : cantidad de faltas,
    “amonestaciones” : cantidad de amonestaciones
    }
    En esta estructura:
    Datos = {
    “Alumnos” : [alumno1,alumno2,alumno3 ]
    }
    Para acceder por ejemplo al numero de DNI del tercer alumno
    podríamos hacer algo así:
    Datos[“Alumnos”][2][“DNI”]
Este es un ejemplo de estructura, se puede cambiar
completamente o hacer algunos cambios sobre el para mejorar el
orden (si lo consideran necesario)
b) Mostrar los datos de cada alumno
c) Modificar los datos de los alumnos
d) Agregar alumnos
e) Expulsar alumnos"""


datos_alumnos={
    'Alumnos' : [
        {
        'Nombre': "Milagros",
        'Apellido' : "Tapia",
        'DNI' : "43441001",
        'Fecha de nacimiento': "17/06/2001",
        'Tutor' : "Graciela Cutipa",
        'Notas' : [10,9,8,7],
        'Faltas' : 2,
        'Amonestaciones' : 0
        },

        {
        'Nombre': "Juan",
        'Apellido' : "Perez",
        'DNI' : "46441023",
        'Fecha de nacimiento': "15/07/2004",
        'Tutor' : "Osar Perez",
        'Notas' : [7,8,8,7],
        'Faltas' : 6,
        'Amonestaciones' : 2
        },

        {
        'Nombre': "Luis",
        'Apellido' : "Martinez",
        'DNI' : "46229209",
        'Fecha de nacimiento': "27/08/2006",
        'Tutor' : "Lucia Martinez",
        'Notas' : [6,7,9,6],
        'Faltas' : 4,
        'Amonestaciones' : 1
        },

        {
        'Nombre': "Rodrigo",
        'Apellido' : "Fernandez",
        'DNI' : "46229118",
        'Fecha de nacimiento': "27/01/2006",
        'Tutor' : "Ana Martinez",
        'Notas' : [6,8,10,6],
        'Faltas' : 5,
        'Amonestaciones' : 4
        },
    ]
}


def mostrar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']: 
        if alumno["DNI"]==dni:
            for dato in alumno:
                print(f"{dato}: {alumno[dato]}")
            return
    print("Alumno no encontrado.")


def mostrar_todos_alumnos(datos_alumnos):
    for alumno in datos_alumnos['Alumnos']: 
        for dato in alumno:
            print(f"{dato}: {alumno[dato]}")
        print("-------------------------------------")


def ingresar_datos():
    nuevo_alumno={}
    nuevo_alumno['Nombre'] = input(f"Ingrese el nombre del alumno: ")
    nuevo_alumno['Apellido'] = input(f"Ingrese el apellido del alumno: ")
    nuevo_alumno['DNI'] = input(f"Ingrese el DNI del alumno: ")
    nuevo_alumno['Fecha de nacimiento'] = input(f"Ingrese la Fecha de nacimiento del alumno: ")
    nuevo_alumno['Tutor'] = input(f"Ingrese el nombre del tutor: ")
    notas_str = input("Ingrese las notas separadas por comas (ej: 10,9,8): ")
    lista=[]
    for nota in notas_str.split(','):
        lista.append(int(nota))
    nuevo_alumno["Notas"] = lista
    nuevo_alumno['Faltas'] = int(input(f"Ingrese el numero de faltas: "))
    nuevo_alumno['Amonestaciones'] = int(input(f"Ingrese el numero de amonestaciones: "))

    return nuevo_alumno


def agregar_alumno(datos_alumnos):
    nuevo_alumno=ingresar_datos()
    for alumno in datos_alumnos['Alumnos']:
        if alumno["DNI"]==nuevo_alumno['DNI']:
            print("Error: este alumno ya existe")
            return
    datos_alumnos['Alumnos'].append(nuevo_alumno)
    print("Alumno agregado correctamente.")


def modificar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']:
        if alumno["DNI"]==dni:
            print("¿Qué dato desea modificar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. DNI")
            print("4. Fecha de nacimiento")
            print("5. Tutor")
            print("6. Notas")
            print("7. Faltas")
            print("8. Amonestaciones")
            dato_modificar=input("¿Que dato desea modificar? ")
            if dato_modificar!="DNI":
                dato_modificar=dato_modificar.capitalize()

            if dato_modificar=="Nombre" or dato_modificar=="Apellido" or dato_modificar=="DNI" or dato_modificar=="Fecha de nacimiento" or dato_modificar=="Tutor":
                modifica=input(f"Ingrese el nuevo {dato_modificar}: ")
                alumno[dato_modificar]=modifica
            elif dato_modificar=="Faltas" or dato_modificar=="Amonestaciones":
                modifica=int(input(f"Ingrese la nueva cantidad de {dato_modificar}: "))
                alumno[dato_modificar]=modifica
            elif dato_modificar=="Notas":
                notas_str = input("Ingrese las nuevas notas separadas por comas: ")
                lista=[]
                for notas in notas_str.split(','):
                    lista.append(int(notas))
                alumno["Notas"] =lista
            else:
                print("Error: Opción no valida")
            print("Dato modificado correctamente.")
            return
    print("Alumno no encontrado.")


def eliminar_alumno(dni,datos_alumnos):
    for alumno in datos_alumnos['Alumnos']: 
        if alumno["DNI"]==dni:
            datos_alumnos['Alumnos'].remove(alumno)
            print("Alumno eliminado correctamente.")
            return
    print("Alumno no encontrado.")


print()
print("Bienvenido al Sistema de Gestión de la Nuestra Escuela")
while True:
    print("----------------------")
    print("1- MOSTRAR ALUMNO")
    print("2- MOSTRAR TODOS LOS ALUMNOS")
    print("3- AGREGAR ALUMNO")
    print("4- MODIFICAR ALUMNO")
    print("5- ELIMINAR ALUMNO")
    print("6- SALIR")
    print("----------------------")

    operacion= int(input("Ingrese el numero correspondiente a la operacion que desee realizar: "))
    if operacion==1:
        dni= input("Ingrese el DNI del alumno que desee ver la informacion: ")
        print("\n")
        mostrar_alumno(dni,datos_alumnos)
    elif operacion==2:
        print("\n")
        mostrar_todos_alumnos(datos_alumnos)
    elif operacion==3:
        agregar_alumno(datos_alumnos)
        print("\n")
        mostrar_todos_alumnos(datos_alumnos)
    elif operacion==4:
        dni= input("Ingrese el DNI del alumno que desee modificar: ")
        modificar_alumno(dni,datos_alumnos)
        print("\n")
        mostrar_todos_alumnos(datos_alumnos)
    elif operacion==5:
        dni= input("Ingrese el DNI del alumno que desee eliminar: ")
        eliminar_alumno(dni,datos_alumnos)
        print("\n")
        mostrar_todos_alumnos(datos_alumnos)
    elif operacion==6:
        print("Saliendo del programa, ¡Hasta luego!") 
        break
    else:
         print("Error: Operación no encontrada")