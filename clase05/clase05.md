# Clase 05

**Recordatorio:** Mencionar los keywords en las llamadas a funciones antes de que empiece la clase.

## Temas

1. Módulo `%` y ejemplo con dígitos
2. Booleanos:
  1. Expresiones booleanas
  2. Type de True y False
  3. Operadores relacionales
  4. Operadores lógicos
  5. Números mayores a cero == True
3. Ejecución condicional `if`, ejecución alternativa `else` y condicional encadenado `elif`
4. Recursión
  1. Ejemplos (diferencia con `for`)
  2. Retornar valores en funciones `return`
  3. Ejercicio `do_n`
  4. Ejemplo recursión infinita
5. Keyboard input
  1. Uso de `input`
  2. Imprimir un mensaje y salto de línea
  3. Ejemplo con nombre y saludo dentro de funciones
  4. Conversión a `int`
6. Consejo al leer errores

## Tarea

1. El Teorema de Fermat dice que no hay enteros a, b y c tal que `a^n + b^n = c^n` para cualquier valor de n mayor que 2.

  - [ ] Escribe una función llamada `check_fermat` que tome cuatro parámetros (a, b, c y n) y que revise si se cumple el Teorema de Fermat. Si n es mayor que 2 y resulta que `a^n + b^n = c^n` el programa debe imprimir en pantalla: `"¡Madre mía, Fermat se equivocó!"`. En otro caso debe imprimir: `"No, eso no funciona..."`.
  - [ ] Escribe una función que le pida al usuario valores para a, b, c y n, los convierta a int y usa la función `check_fermat` para revisar si dichos valores cumplen con el Teorema.

---

2. Si te dan tres varas, podrías o no podrías acomodarlos formando un triángulo con ellas. Por ejemplo, si una mide 12cm y las otras dos miden 1cm cada una, entonces no se podrían acomodar de ninguna forma para que los extremos de las varas sean las aristas de algún triángulo.
Con la siguiente regla se puede determinar lo anterior:
> Si alguna de las tres longitudes es mayor que la suma de las otras dos, entonces no puedes formar un triángulo. Si no se cumple entonces sí se puede formar.

  - [ ] Escribe una función llamada `is_triangle` que tome tres enteros como parámetros e imprima `"Sí"` o `"No"` dependiendo si puedes o no formar un triángulo con varas con las longitudes dadas.
  - [ ] Escribe una función que pida al usuario tres longitudes de varas, conviértelas a int y usa la función `is_triangle` para determinar si se puede formar un triángulo con las longitudes proporcionadas.

---

**Los siguientes ejercicios (3 y 4) deben ser usando swampy.TurtleWorld**

3. Lee la siguiente función e intenta describir qué hace, luego ejecutala (crea el mundo y la tortuga para luego llamar a la función):

```python
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length * n)
    lt(t, angle)
    draw(t, length, n - 1)
    rt(t, 2 * angle)
    draw(t, length, n - 1)
    lt(t, angle)
    bk(t, length * n)
```
**Consejo:** Para averiguar qué hace intenta con `legth = 10` y `n = 1`, luego ve aumentando el tamaño de la n en una unidad.

---

4. La curva de Koch es un fractal y se ve así:

![Construcción de la curva de Koch](https://www.researchgate.net/profile/Marcelo_Ribeiro20/publication/26365833/figure/fig5/AS:310046622797835@1450932283682/Construction-of-the-von-Koch-curve-F-At-each-stage-the-middle-third-of-each-interval.png)

Para dibujar una curva de Koch de longitud `x` se tiene que hacer lo siguiente:
  1. Dibuja una curva de Koch con longitud `x / 3`
  2. Gira a la izquierda 60 grados
  3. Dibuja una curva de Koch con longitud `x / 3`
  4. Gira a la derecha 120 grados
  5. Dibuja una curva de Koch con longitud `x / 3`
  6. Gira a la izquierda 60 grados
  7. Dibuja una curva de Koch con longitud `x / 3`

La única excepción es si x menor que 3. En ese caso solo tienes que dibujar una línea recta con longitud x.

  - [ ] Escribe una función llamada `koch` que tome una tortuga y una longitud como parámetros y use la tortuga para dibujar una curva de Koch con la longitud proporcionada.
  - [ ] Escribe una función llamada `snowflake` que dibuje tres curvas de Koch para hacer la silueta de un copo de nieve.
