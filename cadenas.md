
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


