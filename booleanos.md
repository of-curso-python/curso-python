# Operaciones booleanas

https://docs.python.org/3.5/reference/expressions.html#boolean-operations

En el contexto de las operaciones booleanas, y también cuando las expresiones son utilizadas por las sentencias de control de flujo,
los siguientes valores se interpretan como falsos:
- `False`
- `None`
- `0`
- Cadenas y contenedores vacíos (incluidas cadenas, tuplas, listas y diccionarios , Conjuntos y frozensets).

Todos los demás valores se interpretan como verdaderos.
Los objetos definidos por el usuario pueden personalizar su valor de verdad proporcionando un método __bool __ ().


El operador `not` produce `True` si su argumento es falso, de lo contrario produce `False`.

La expresión `x and y` primero evalúa `x`; Si `x` es falso, se devuelve su valor;
De lo contrario, `y` se evalúa y se devuelve el valor resultante.

La expresión `x or y` primero evalúa `x`; Si `x` es verdadero, se devuelve su valor;
De lo contrario, `y` se evalúa y se devuelve el valor resultante.
