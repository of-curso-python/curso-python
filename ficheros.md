# Lectura y escritura de archivos

https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files


**Método `open()`**

https://docs.python.org/2.7/library/functions.html#open

Devuelve un objeto de archivo, y es más comúnmente usado con dos argumentos: `open (filename, mode)`.

- `filename` es el nombre del archivo que se va a abrir.
- `mode` es una cadena que indica cómo se va a abrir el archivo.
   Los valores de `mode` más comúnmente utilizados son `'r'` para lectura, `'w'` para escritura y `'a'` para añadir

## Modo escritura
``` python
# abrir el archivo con nombre `hola.txt` en modo de escritura
>>> f = open('hola.txt', 'w')
>>> f.write('Hola Mundo desde un archivo')
>>> f.close()
```
Al tratar de realizar una operación de lectura o escritura en un archivo que no fue abierto en ese modo, un error tipo `IOError`
sera lanzado. Por ejemplo:
``` python
# Abrir archivo en modo escritura no le da a la aplicación permisos para ejecutar acciones de lectura.

>>> f = open('hola.txt', 'w')
>>> f.readline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: File not open for reading
```

## Modo lectura
Para leer el contenido de un archivo, llame a `f.read(size)`, que lee una cantidad de datos y la devuelve como una cadena.
`size` es un argumento numérico opcional. Cuando el tamaño se omite o negativo, todo el contenido del archivo será leído y
devuelto.

``` python
>>> f = open('hola.txt', 'r')
>>> f.read()    
'Hola Mundo desde un archivo'
```

 **Es un problema si el archivo es dos veces más grande que la memoria de su máquina.** Para evitar esto se puede usar
 el método `f.readline()`:
 
`f.readline()` lee una sola línea del archivo; Un carácter de nueva línea (`\n`) se deja al final de la cadena, y
sólo se omite en la última línea del archivo si el archivo no termina en una nueva línea.
Esto hace que el valor de retorno sea inequívoco; Si `f.readline()` devuelve una cadena vacía,
se ha alcanzado el final del archivo, mientras que una línea en blanco está representada por `\n`,
una cadena que contiene solo una nueva línea.

``` python
f = open('hola.txt', 'r')
>>> f.readline()
'Hola Mundo desde un archivo'
>>> f.readline()
''
```

Para leer líneas de un archivo, puede realizar bucle sobre el objeto de archivo.
Esto es eficiente en uso de memoria, rápido, y simple:

``` python
>>> for linea in f:
...     print linea
... 
Hola Mundo desde un archivo
>>> 
```

**Cuando haya terminado de trabajar con un archivo, llame a `f.close()` para cerrarlo y liberar los recursos del sistema ocupados por el archivo abierto. Después de llamar a `f.close()`, los intentos de usar el objeto de archivo fallarán automáticamente.**
