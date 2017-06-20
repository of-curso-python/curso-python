Una tupla consista en valores separados por coma.

https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences

Ejemplo:
``` python
tupla = 1,2,'tres',4
print(tupla)
(1, 2, 'tres', 4)
```
Las tuplas son inmutables y normalmente contienen una secuencia heterogénea de elementos a los que se accede a través del desempaquetamiento o la indexación.

**Tuplas de un solo elemento**

La sintaxis tiene algunas peculiaridades adicionales al crear tuplas de un solo elemento o ninguno.
Ejemplo:
``` python
tupla = ()
cadena = 'hola'
tupla = (cadena,)
```
**Empaquetamiento**
``` python
tupla = 1,2,'tres',4
```
**Desempaquetamiento**
``` python
tupla = (10, 15)
primer_numero, segundo_numero = tupla
```


