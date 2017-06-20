# Métodos de lista.
https://docs.python.org/2.7/tutorial/datastructures.html#more-on-lists

**list.append(x)**

Agrega un elemento al final de la lista.

**list.extend(iterable)**

Extiende la lista al agregar todos los elementos de `iterable`.

**list.insert(i, x)**

Inserta un elemento a una posición dada.
El primer argumento es el índice del elemento antes del cual iniciar la inserción.
``` python
mi_lista = ['a','b','c']
mi_lista.insert(1, 'nuevo elemento')
print(mi_lista)
['a', 'nuevo elemento', 'b', 'c']
```

**list.remove(x)**

Elimina el primer elemento de la lista cuyo valor sea `x`. Lanza un error si el elemento no existe en la lista.

**list.pop([i])**

Elimina un elemento de la posición dada en la lista y lo retorna.
Si el índice `i` no es especificado, `a.pop()` elimina y retorna el ultimo elemento de la lista.

**list.clear()**

Elimina todos los elementos de la lista.

**list.index(x[, start[, end]])**

Retorna un índice en la lista del primer elemento cuyo valor es `x`. Lanza `ValueError` si el elemento no existe en la lista.
Los argumentos opcionales `start` y `end` son interpretados como en la natación de `slice` para limitar la busqueda a una
sub secuencia de la lista.

**list.count(x)**
Retorna el número de veces que `x` aparece en la lista.


**list.sort(key=None, reverse=False)**

Ordena los elementos de la lista.
El argumento opcional `key` es una funcion usada para extraer la llave que se usara para la comparación
durante el ordenamiento.

``` python
mi_lista = ['z', 'x', 'a', 'd']
mi_lista.sort()
print(mi_lista)
['a', 'd', 'x', 'z']
```

*Ejemplo 2*

``` python
mi_lista = [{'nombre': 'Olga'}, {'nombre': 'Ana'}]
mi_lista.sort(key=lambda x: x['nombre'])
print(mi_lista)
[{'nombre': 'Ana'}, {'nombre': 'Olga'}]
```

**list.reverse()**

Invierte los elementos de una lista.

**list.copy()**

Retorna una copia **superficial** de la lista. Equivalente a `mi_lista[:]`


## Listas por comprensión

Lista de comprensiones proporcionan una forma concisa de crear listas. Las aplicaciones comunes son hacer nuevas listas donde cada elemento es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o crear una subsecuencia de aquellos elementos que satisfacen una determinada condición.

Por ejemplo:

``` python
estudiantes = ['Oscar', 'Lucia', 'Pedro', 'Carlos']
```
Supongamos que necesitamos una lista con la inicial de cada estudiante.
Podemos hacer:
``` python
iniciales = []
for estudiante in estudiantes:
    iniciales.append(estudiante[0])

print(iniciales)
['O', 'L', 'P', 'C']
```
o por comprensión
``` python
iniciales = [estudiante[0] for estudiante in estudiantes]
print(iniciales)
['O', 'L', 'P', 'C']
```
