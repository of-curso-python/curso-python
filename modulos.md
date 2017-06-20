# Módulos

https://docs.python.org/2.7/tutorial/modules.html

Un módulo es un archivo que contiene definiciones y declaraciones de Python.
El nombre del archivo es el nombre del módulo con el sufijo `.py` añadido.
Dentro de un módulo, el nombre del módulo (como una cadena) está disponible como el valor de la variable global `__name__`.

**Por Ejemplo:**

El archivo `ejemplo.py` en este repositorio es un módulo de python.
Para poder usar una función definida en ese módulo desde otro módulo podemos hacer:

`from ejemplo import mi_funcion`

El valor de la variable `__name__` en el módulo `ejemplo.py` en este caso es la cadena `"ejemplo"`.

Pero si usamos el módulo `ejemplo.py` como un script:

`python3 ejemplo.py`

El valor de la variable `__name__` en el módulo `ejemplo.py` en este caso es la cadena `"__main__"`
