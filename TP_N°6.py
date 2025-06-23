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


def mostrar_alumno(dni,datos_alumno):
    for alumno in datos_alumno['Alumnos']: 
        if alumno["DNI"]==dni:
                for dato in alumno:
                    print(f"{dato}: {alumno[dato]}")
    return print(f"Alumno no encontrado")

dni= input("Ingrese el DNI del alumno que desee ver la informacion: ")
mostrar_alumno(dni,datos_alumnos)


