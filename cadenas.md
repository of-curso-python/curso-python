
# Métodos de cadena
https://docs.python.org/3.5/library/stdtypes.html#string-methods

**str.capitalize()**

Retorna una copia de la cadena con su primer caracter en mayúscula y el resto en minúscula.

**str.center(width[, fillchar])**

Retorna una cadena centrada.
El relleno se realiza utilizando el `fillchar` especificado (por defecto es un espacio ASCII).
La cadena original se devuelve si el ancho es menor o igual que `len(str)`


**str.count(sub[, start[, end]])**

Devuelve el número de ocurrencias no superpuestas de subcadenas en el rango [start, end].
Los argumentos opcionales de inicio(`start`) y de fin(`end`) se interpretan como en la notación de corte(`slice`).

**str.endswith(suffix[, start[, end]])**

Retorna `True` si la cadena finaliza con el sufijo especificado `suffix`, de lo contrario retorna `False`.
El sufijo puede ser una tupla de sufijos para buscar.
Con inicio opcional(`start`), el test comienza en esa posición. Con el extremo opcional(`end`),
deje de comparar en esa posición.

**str.find(sub[, start[, end]])**

Retorna el índice mas bajo en la cadena en donde la subcadena es encontrada dentro de `s[start:end]`.
Los argumentos opcionales `start` y `end` son intepretados como en la notación de `str.slice`. Retorna -1 si la subcadena no es econtrada. 

**str.index(sub[, start[, end]])**

Parecido a `str.find()`, pero lanza la excepción `ValueError` cuando la subcadena no es encontrada.


**str.join(iterable)**

Retorna una cadena que es la concatenación de cadenas en un iterable(una lista o tupla por ejemplo).
Un `TypeError` sera lanzado si hay algún valor no-cadena en el iterable.
El separador entre elementos es la cadena que proporciona este método.
```
','.join(['hola', 'mundo'])
'hola,mundo'
```

**str.ljust(width[, fillchar])**

Retorna la cadena justificada a la izquierda en una cadena de longitud `width`.
El relleno se realiza utilizando el `fillchar` especificado (por defecto es un espacio ASCII).
La cadena original se devuelve si el ancho es menor o igual que len (s).
```
'hola'.ljust(10, '*')
'hola******'
```
**str.lower()**

Retorna una copia de la cadena con todos los caracteres en minuscula.

**str.lstrip([chars])**

Retorna una copia de la cadena con todos los caracteres iniciales eliminados.
El argumento `chars` es una cadena que especifica el conjunto de caracteres a eliminar.
Si se omite o no, el argumento chars predeterminado es quitar espacios en blanco.

**str.replace(old, new[, count])**

Retorna una copia de la cadena con todas las ocurrencias de la subcadena reemplazadas por la nueva. Si el argumento
opcional `count` es especificado, solamente las `count` ocurrencias son reemplazadas.

**str.rstrip([chars])**

Retorna una copia de la cadena con los caracteres finales removidos. El argumento `char` es una cadena especificando el
grupo de caracteres a eliminar. Si es omitido o es `None`, el argumento `chars` es por defecto espacios en blanco.

**str.split(sep=None, maxsplit=-1)**

Devuelve una lista de las palabras de la cadena, usando `sep` como delimitador. Si `maxsplit` es especificado, se realiza el máximo las divisiones `maxsplit`. Si `maxsplit` no se especifica o -1, entonces no hay límite en el número de divisiones.

```
'1,2,3'.split(',')
['1', '2', '3']
```

**str.startswith(prefix[, start[, end]])**

Retorna `True` si la cadena inicia con el prefijo, de lo contrario retorna `False`. El prefijo puede ser una tupla de prefijos que buscar. El argumento opcional `start` es para iniciar la busqueda desde esa posición. Con el argumento opcional `end` deja de comparar la cadena en esa posición.

**str.strip([chars])** 

Retorna una copia de la cadena con los caracteres `chars` removido al inicio y al final. 
Si `chars` es omitido o es `None`, por defecto se eliminan los espacios en blanco.

**str.upper()**

Retorna una copia de la cadena con todos los caracteres convertidos a mayúsculas.

**str.zfill(width)**

Retorna una copia de la cadena rellenada a la izquierda para hacer dicha cadena de la longitud `width`.
