# Clase 07

## Temas

1. Asignar valores distintos a una variable (ayuda pero de ser posible evitarlo para facilitar la depuración de cl programa)
```python
bruce = 4
print(bruce)
bruce = 7
print(bruce)
```

---
2. Inicializar y actualizar una variable, comparación con Java
```python
x = x + 1
# x += 1
```

---
3. `while`
  1. Ejemplo y sintaxis

    ```python
    import time
    def countdown(n):
      while n > 0:
        print(n)
        n = n - 1
        print("Kaboom!")
    ```
  2. Ejecución:
    1. Evalúa la condición (con esto obtenemos `True` o `False`)
    2. Si se evalúa a `False`, termina el ciclo y continúa con la ejecución del programa.
    3. Si se evalúa `True`, ejecuta el cuerpo del `with` y regresa al paso 1.
  3. Terminación del ciclo
    1. Actualización de variables (incremental y decremental) para evitar ciclos infinitos
    2. Terminación de `countdown`
    3. Ejemplo (conjetura de Collatz)

      ```python
      def sequence(n):
        while n != 1:
          print(n)
          # Si n es par
          if n % 2 == 0:
            n = n / 2
          # Si n es impar
          else:
            n = n * 3 + 1
      ```
  4. Ejercicio `print_n` con iteración.

---
4. Expresión `break`
  1. Terminar un ciclo dentro del body

    ```python
    while True:
      line = input("> ")
      if line == "exit":
        print("Adios!")
        break
      print(line)
    ```
  2. "Detenerse cuando algo pasa" vs "Sigue ejecutando mientras se cumpla algo"

---
5. Uso común de `with`
  1. Raíz cuadrada (método de Newton)

    Suponiendo que se quiere calcular la raíz cuadrada de `a` y se tiene una aproximación cualquiera `x`, puedes calcular una estimación mejor con la fórmula: `y = (x + a / x) / 2`
  2. Ejemplo:

    ```python
    a = 4
    x = 3
    y = (x + a / x) / 2
    print(y)
    x = y
    ```
  3. Ahora con `with` y optimización en flotantes

    ```python
    a = 4.0
    x = 3.0

    while True:
      print(x)
      y = (x + a / x) / 2
      if y == x:
        break
      x = y
    ```
  4. Ejercicio: encapsular en una función `square_root`

## Tarea

---
1. Para testear la función `square_root` que hicimos se puede comparar con la función `math.sqrt`. Escribe una función llamada `test_square_root` que imprima una tabla como la siguiente:

  ```
  1 1.00000 1.00000 0.0
  2 1.41421 1.41421 1.5947243525715749e-12
  3 1.73205 1.73205 2.44585018904786e-09
  4 2.00000 2.00000 9.2922294747666e-08
  5 2.23607 2.23607 9.18143573613861e-07
  6 2.44949 2.44949 4.373834627813267e-12
  7 2.64575 2.64575 4.6778581008766196e-11
  8 2.82843 2.82843 3.0367397485520087e-10
  9 3.00000 3.00000 1.3969838619232178e-09
  ```

  En la primera columna está el valor de `a`, en la segunda el valor calculado con `square_root`, la tercera el valor calculado con `math.sqrt` y la última el valor absoluto de las diferencias de los valores.
  Tu función debe aceptar un parámetro `n` y hacer el test con `a` desde 1 hasta `n`.

  **Consejo:** Escribe una función exclusiva para obtener el formato requerido en cada línea.

---
2. La función `eval` de Python toma un string y usando el intérprete de Python evalúa la expresión en el string. Por ejemplo usando el intérprete:

  ```python
  >>> eval("1 + 2 + 3")
  7
  >>> import math
  >>> eval("type(math.pi)")
  <type 'float'>
  ```

  Escribe una función llamda `eval_loop` que le muestre constantemente al usuario un prompt, tome el input del usuario, lo evalúe usando la función `eval` e imprima el resultado.

  Se debe seguir ejecutando hasta que el usuario escriba `exit` y finalmente la función retorne el valor de la última expresión evaluada.
