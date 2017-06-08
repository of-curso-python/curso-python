import argparse # import de modulo argparser
import logging # import de modulo logging. Usar logs es importante en toda app.


# Obtenemos un logger cuyo nombre es el valor __name__
logger = logging.getLogger(__name__)

# Establecemos el umbral para este logger. En este caso va registrar
# errores que son igual o menos severos que DEBUG.
# log level en orden de severidad: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.DEBUG)

# Establecemos un manejador para el logger.
logger.addHandler(logging.StreamHandler())

logger.info('** El valor de la variable "__name__" es: "{}"'.format(__name__))

# Asignamos valor a la constante SALUDO.
# (Las constantes las escribimos en mayúscula).
SALUDO = 'Hola {nombre} {apellido}.'


def saludar(nombre, apellido):
    """ Retorna un mensaje de saludo.
    nombre -- nombre de una persona.
    apellido -- apellido de una persona.
    (De esta manera se documentan las funciones en python)

    """

    mensaje = SALUDO.format(nombre=nombre, apellido=apellido)
    return mensaje



if __name__ == '__main__':

    logger.info('** Estas ejecutando directamente este modulo')

    # Crea una instancia de ArgumentParser y es asignada a la variable "parser".
    parser = argparse.ArgumentParser(description='Esto es un ejemplo de python.')

    logger.info('** Especificando argumentos posicionales.')
    # Especifica que opciones de línea de comando esta app va a aceptar. En este caso
    # acepta 'nombre' y 'apellido'. Ambos parametros son posicionales y requeridos.
    parser.add_argument('nombre')
    parser.add_argument('apellido')

    # El metodo 'parser_args()' obtiene los valores introducidos al momento
    # de ejecutar el script.
    args = parser.parse_args()

    logger.info('** Invocando funcion "saludar con los argumentos.')
    # Invoca a la funcion "saludar" pasando como argumentos los recibidos
    # desde la linea de comando.
    mensaje = saludar(args.nombre, args.apellido)

    # Imprimir el mensaje
    print(mensaje)
