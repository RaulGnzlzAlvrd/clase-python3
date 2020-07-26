# Clase 03

## Temas

1. ¿Qué es una función? Una secuencias de expresiones que realizan un cómputo. Debes especificar su nombre y la secuencia de expresiones. Luego puedes llamarla.
2. Funciones de conversion de tipos
3. Funciónes con el módulo math
4. Composición de funciones
5. Definir funciones.
  1. Tienen las mismas reglas al ser nombradas que las variables  
  2. Identación y como se usa el modo interactivo
  3. Ver el tipo de la función
  4. El cuerpo de las funciones no se ejecutan cuando se crean, solo cuando se llaman
  5. Las funciones se deben crear antes de llamarlas
  6. Hacer el ejemplo de cambiar las llamadas

6. Flujo de ejecución y jumps (leer según el flujo)
7. Parámetros y argumentos de funciones y se evaluan antes de ejecutar el cuerpo de la función
8. Alcance de las variables y excepción
9. Funciones void, y type de None
10. ¿Por qué funciones?






## Tarea

1. Python tiene una función llamada `len` que regresa la longitud de un string. Así el valor de `len("Hola")` es 4.
Escribe una función llamada `right_justify` que tome un string `s` como parametro e imprima antes de `s` suficientes espacios tal que la última letra de `s` esté en la columna 70.

>>> right_justify("Hola")
aquí 66 espacios y luego Hola

2. Una función es un valor que puedes asignar a una variable o pasar como argumento. Por ejemplo `do_twice` es una función que toma una función como argumento y la llama dos veces:

```python
def do_twice(f):
  f()
  f()
```

Aquí hay un ejemplo que usa `do_twice` para llamar a una función llamada `print_spam` dos veces:

```python
def print_spam():
  print("spam")

do_twice(print_spam)
```

  - Escribe el ejemplo en un script y ejecutalo
  - Modifica `do_twice` para que tome dos argumentos (una función `f` y un valor `v`), y llama a la función dos veces (en el cuerpo de `do_twice`) pasando el valor `v` como argumento a `f`.
  - Escribe otra función llamada `print_twice` que tome un string como argumento y lo imprima dos veces
  - Llama la función `do_twice` (ya modificada) pasando `print_twice` y `"spam"` como argumentos.
  - Define una nueva función llamada `do_four` que tome una función `f` y un valor `v` como parámetros. Esta función debe ejecutar `f` con `v` 4 veces. Pero solo debe haber dos líneas en el cuerpo de la función `do_four`.

3. Escribe una función que imprima un dibujo como el siguiente:

+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+

Luego modifica tu función para que dibuje una figura similar pero con cuatro columnas y cuatro renglones.
