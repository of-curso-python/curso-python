# Operadores de comparación

https://docs.python.org/2.7/reference/expressions.html#comparisons

Todas las operaciones de comparación en Python tienen la misma prioridad, que es menor que la de cualquier aritmética.

Las comparaciones pueden encadenarse arbitrariamente,
por ejemplo, `x < y <= z` es equivalente a `x < y and y <= z`, con la excepción de que `y` sólo se evalúa una vez.

## Comparación de valores

Los operadores `<,>, ==,> =, <=, !=` Comparan los valores de dos objetos.

- Las cadenas (instancias de `str`) comparan lexicográficamente
usando los puntos numéricos de código Unicode (el resultado de la función incorporada ord ()) de sus caracteres.

- Las secuencias (instancias de tupla, lista) se pueden comparar sólo dentro de cada uno de sus tipos.
La comparación de igualdad a través de estos tipos da como resultado una desigualdad:
```python
(1,) == [1]
False
```
y la comparación de orden a través de estos tipos eleva `TypeError`
``` python
(1,) < [1]
TypeError: unorderable types: tuple() < list()
```

- La comparación lexicográfica entre las colecciones integradas funciona de la siguiente manera:

    Para que dos colecciones comparen iguales, deben ser del mismo tipo, tener la misma longitud,
y cada par de elementos correspondientes debe comparar igual (por ejemplo, `[1,2] == (1,2)` es falso
porque el tipo no es lo mismo).
Las colecciones que soportan la comparación de órdenes se ordenan igual que sus primeros elementos desiguales
(por ejemplo, `[1,2, x] <= [1,2, y]` tiene el mismo valor que `x <= y`).
Si no existe un elemento correspondiente, la colección más corta se ordena primero
(por ejemplo, `[1,2] <[1,2,3]` es verdadero).
