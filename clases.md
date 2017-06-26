``` python

class Clase:
    <declaración-1>
    .
    .
    .
    <declaración-N>
    
```
Las definiciones de clases, al igual que las definiciones de funciones (instrucciones def)
deben ejecutarse antes de que tengan efecto alguno.

En la práctica, las declaraciones dentro de una clase son definiciones de funciones, pero otras declaraciones son permitidas, y a veces resultan útiles. Las definiciones de funciones dentro de una clase normalmente tienen una lista de argumentos peculiar, dictada por las convenciones de invocación de métodos;


Los objetos clase soportan dos tipos de operaciones: hacer referencia a atributos e instanciación.

Para hacer referencia a atributos se usa la sintaxis estándar de todas las referencias a atributos en Python: `objeto.nombre`.
Los nombres de atributo válidos son todos los nombres que estaban en el espacio de nombres de la clase cuando ésta se creó.
Por lo tanto, si la definición de la clase es así:

``` python

class MiClase:
    """Simple clase de ejemplo"""
    i = 12345
    def f(self):
        return 'hola mundo'
```
entonces `MiClase.i` y `MiClase.f` son referencias de atributos válidas, que devuelven un entero y un objeto función respectivamente. Los atributos de clase también pueden ser asignados, o sea que podés cambiar el valor de `MiClase.i` mediante asignación. `__doc__` también es un atributo válido, que devuelve la documentación asociada a la clase: "Simple clase de ejemplo".


La instanciación de clases usa la notación de funciones. Por ejemplo (para la clase de más arriba):
``` python
x = MiClase()
```
crea una nueva instancia de la clase y asigna este objeto a la variable local `x`.

La operación de instanciación crea un objeto vacío. Muchas clases necesitan crear objetos con instancias en un estado inicial particular. Por lo tanto una clase puede definir un método especial llamado `__init__()`, de esta forma:

``` python
def __init__(self):
    self.datos = []
```

Cuando una clase define un método `__init__()`, la instanciación de la clase automáticamente invoca a `__init__()` para la instancia recién creada. Entonces, en este ejemplo, una instancia nueva e inicializada se puede obtener haciendo:
```python
x = MiClase()
```

Por supuesto, el método `__init__()` puede tener argumentos para mayor flexibilidad. En ese caso, los argumentos que se pasen al operador de instanciación de la clase van a parar al método `__init__()`. Por ejemplo,
``` python
>>> class Estudiante(object):
...     def __init__(self, nombre, apellido):
...         self.nombre_estudiante = nombre
...         self.apellido_estudiante = apellido
...
>>> x = Estudiante('John', 'Doe')
>>> x.nombre_estudiante, x.apellido_estudiante
('John', 'Doe')
```
