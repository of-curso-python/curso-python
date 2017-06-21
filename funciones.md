# Funciones

La palabra clave `def` introduce una definición de función.
Debe ser seguido por el nombre de la función y la lista entre paréntesis de parámetros formales.
``` python
def hola(nombre):
    print 'Hola {0}'.format(nombre)
```
Las sentencias que forman el cuerpo de la función comienzan en la línea siguiente y deben estar indentado.

``` python
def hola(nombre='Pedro'):
    print 'Holaa {0}'.format(nombre)

# Esta funcion acepta un argumento opcional 'nombre'.
# El argumento `nombre` tiene un valor por defecto definido que es la cadena 'Pedro'
# Esta funcion puede ser llamada de la siguiente manera:

>>> hola()
Hola Pedro

>>> hola(nombre='Ana')
Hola Ana

```
