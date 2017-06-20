# Sets

Python también incluye un tipo de datos para conjuntos (sets). Un `set` es una colección desordenada sin elementos duplicados. Los usos básicos incluyen pruebas de membresía y eliminación de entradas duplicadas. Los objetos `Set` también soportan operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.
``` python
# Lista de nombres con el elemento "Ana" duplicado.

>>> nombres = ['Ana', 'Mario', 'Carlos', 'Ana', 'Luis']

# Un set sin duplicados

>>> set_de_nombres = set(nombres)
>>> print set_de_nombres
set(['Mario', 'Ana', 'Carlos', 'Luis'])

# Probar membresia
>>> 'Mario' in set_de_nombres
True
```
