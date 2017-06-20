# Diccionarios

A diferencia de las secuencias, que están indexadas por un rango de números, los diccionarios son indexados por claves, que pueden ser de cualquier tipo inmutable; Cadenas y números siempre pueden ser claves.

Lo mejor es pensar en un diccionario como un conjunto no ordenado de pares `llave: valor`, con el requisito de que las claves sean únicas (dentro de un diccionario). `{}` crea un diccionario. Colocar una lista separada por comas de pares de `llave: valor` dentro de las llaves añade pares iniciales `llave:valor` al diccionario;

Las operaciones principales en un diccionario son almacenar un valor con una llave y extraer el valor dado la llave. También es posible borrar un par `llave: valor` con `del`. Si se trata de almacenar en el diccionario utilizando una llave que ya está en uso, el `valor` antiguo asociado con esa `llave` se olvida. Es un error extraer un valor utilizando una clave inexistente.

El método `keys()` de un diccionario devuelve una lista de todas las `llaves` utilizadas en el diccionario, en orden aleatorio (si lo desea ordenado, solo aplique la función `sorted()`).

Para comprobar si una sola `llave` está en el diccionario, utilice la palabra clave `in`.

Ejemplo:
``` python
estudiante = {'nombre': 'Ana', 'edad': 25}

# Acceder a la llave 'nombre'
>>> estudiante['nombre']
'Ana'

# Actualizar llave "nombre":

>>> estudiante['nombre'] = 'Carlos'
>>> estudiante
{'edad': 25, 'nombre': 'Carlos'}

# Eliminar la llave 'edad'
del estudiante['edad']
estudiante
{'nombre': 'Carlos'}

# Obtener una las llaves del diccionario
estudiante.keys()
['nombre']


# Comprobar si la llave 'edad' exite:
'edad' in estudiante
False


```

