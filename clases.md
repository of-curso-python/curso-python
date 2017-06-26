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

En la práctica, las declaraciones dentro de una clase son definiciones de funciones, pero otras declaraciones son permitidas, y a veces resultan útiles; veremos esto más adelante. Las definiciones de funciones dentro de una clase normalmente tienen una lista de argumentos peculiar,
dictada por las convenciones de invocación de métodos;


Los objetos clase soportan dos tipos de operaciones: hacer referencia a atributos e instanciación.

Para hacer referencia a atributos se usa la sintaxis estándar de todas las referencias a atributos en Python: `objeto.nombre`.
Los nombres de atributo válidos son todos los nombres que estaban en el espacio de nombres de la clase cuando ésta se creó.
Por lo tanto, si la definición de la clase es así:

