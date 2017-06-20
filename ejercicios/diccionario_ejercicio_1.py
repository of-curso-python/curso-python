import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }

    return estudiantes


# - Crear un script que genere el diccionario de estudiantes
#   usando "generar_diccionario_estudiantes"

# - Imprimir todos las llaves del diccionario generado de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y
#   cursa <anio> en la universidad"

# - Del diccionario de estudiantes creado imprimir los estudiantes
#   de la ciudad de 'Managua' de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad"

# - Del diccionario de estudiantes creado imprimir los estudiantes de 'Masaya' que cursen 1er anio de universidad.
#   de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad"

# - Del diccioanrio de estudiantes creado imprimir los estudiantes que sean menor de 21 anios
#   de la forma:
#   "El <nombre_estudiante> de <edad>, es de la ciudad de <ciudad> y cursa <anio> en la universidad"
