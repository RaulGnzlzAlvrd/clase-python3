# Clase 06

## Temas

1. Return values
  1. El valor que retorna lo usamos en una expresión o lo asignamos a una variable.
  2. Las funciones que hemos hecho solo imprimen mensajes o mueven las tortugas devolviendo `None`
  3. Ejemplo área de círculo.
  4. Significado de `return` (regresa inmediatamente el valor de la expresión)
  5. Alternativa al ejemplo en 3.
  6. Regresar distintas cosas dependiendo de un condicional
  7. Código después de return es **dead code**
  8. Cubrir cada caso (mal ejemplo de `absolute_value`)
  9. Ejercicio `compare`. Regresa 1 si `x > y` , 0 si `x == y` y -1 si `x < y`
2. Desarrollo incremental
  1. Ejemplo con distancia entre dos puntos. (1,2) (4,6)
  2. Ayuda para escribir el código pero no parte del código final **scaffolding** (andamios)
  3. Procedimiento
    1. Ir haciendo pequeños cambios incrementales y si algo sale mal ya sabes donde falló.
    2. Usar variables temporales para imprimirlas y revisarlas
    3. Quitar todo el scaffolding y reagrupar expresiones.
  4. Ejercicio `hypotenuse`
3. Composición de función.
  1. Ejemplo con area de circulo `circle_area` dados dos puntos (centro y perímetro)
4. Funciones booleanas.
  1. Ejemplo de función `is_divisible`
  2. Remover variables temporales
  3. Uso en condicionales y mal ejemplo
5. Más recursión (turing completo)
  1. Ejemplo `factorial`
  2. Salto de fe. Ejemplo con `factorial`
  3. Ejemplo con `fibonacci`
6. Revisión de tipos
  1. ¿Factorial con flotantes? Opciones:
    1. Generalizar factorial para que acepte flotantes
    2. Revisar el tipo del parámetro
  2. Función `isinstance`
  3. Guardianes en factorial


## Tarea

1. Escribe qué hace e imprime el siguiente programa, luego ejecutalo y comprueba tus resultados:

```python
def b(z):
  prod = a(z, z)
  print(z)
  print(prod)
  return prod

def a(x, y):
  x = x + 1
  return x * y

def c(x, y, z):
  sum = x + y + z
  pow = b(sum) ** 2
  return pow

x = 1
y = x + 1
print(c(x, y + 3, x + y))
```

2. La función de Ackerman se define para enteros positivos, como en la siguiente imagen:

![Ackerman function](https://wikimedia.org/api/rest_v1/media/math/render/svg/6e1707b67f7985e91e02de8fb65ed9d6049558a5)

  - [ ] Escribe una función llamda `ack` que evalue la función de Ackerman.
  - [ ] Usa tu función para evaluar `ack(3, 4)` que debería ser 125.
  - [ ] ¿Qué pasa para valores más grandes de m y n?

3. Un palíndromo es una palabra que que se lee igual de adelante hacia atrás y de atras hacia adelante, un ejemplo es "oso" y "redivider". Recursivamente, una palabra es palíndromo si la primera y ultima letra son iguales y la palabra del medio (sin la primera y la última) es un palíndromo.

Las siguientes funciones toman un string como argumento y regresan, la primera letra, la última y las letras del medio:

```python
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
```

Los detalles de las funciones los veremos más adelante.

- [ ] Escribe estas funciones en un archivo y comprueba su funcionamiento. ¿Qué pasa cuándo llamas `middle` con un string de dos letras? ¿Y con una letra? ¿Qué pasa con la cadena vacía (se escribe con comillas simples o dobles y sin nada más `""`)? ¿Qué pasa con la función `first` si se llama con la cadena vacía?

- [ ] Escribe una función llamada `is_palindrome` que tome un string como argumento y retorne `True` si la cadena es un argumento y `False` en otro caso.

**Consejo:** Puedes usar la función `len` para comprobar si tu string es la cadena vacía.
