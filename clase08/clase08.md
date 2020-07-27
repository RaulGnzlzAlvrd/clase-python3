# Clase 08

## Temas

1. Strings (secuencia de caracteres)
  1. Se accede a cada caracter con índices en base `0`:
  ```python
  fruit = "banana"
  letter = fruit[1]
  ```
  2. ¿Cuál es el tipo al que se evalúa la expresión `fruit[0]`?

  3. Se pueden utilizar expresiones o variables como índices pero el tipo debe ser `int`
  ```python
  letter = fruit[1.5]
  ###
  index = 2
  letter = fruit[index]
  ```
  4. Acceso al último caracter de una cadena
  ```python
  length = len(fruit)
  print(length)
  last = fruit[length - 1]
  last = fruit[-1]
  print(fruit[-2])
  ```

---
2. Recorridos

  1. Ejemplo con `while`

```python
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1
```

  2. **Definición:** Un recorrido es un procesamiento de los elementos de una estructura tomados de uno a uno.

  3. Ejemplo con `for`

```python
for char in fruit:
  print(char)
```

  4. Ejemplo (concatenación)

    1. Imprimir el nombre de los patos: Jack, Kack, Lack, Mack, Nack, Ouack, Pack, an Quack.

```python
prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
  print(letter + suffix)
```
    2. Ejercicio: corregir el ejemplo

---
3. Slices

  1. Es un segmento de una cadena

    ```python
s = "Hola Mundo!"
print(s[0:5])
```

  2. Sintaxis `s[n:m]`

  3. Omitir los índices:

    ```python
print(s[:3])
print(s[3:])
```

  4. ¿Qué pasa si `n >= m`?

    ```python
print(s[3:1])
print(s[4:4])
```

  5. ¿Qué pasa si omites ambas?

    ```python
print(s[:])
```

---
4. Inmutabilidad en strings

  1. No se puede modificar un caracter de una cadena

    ```python
greeting = "Hello world!"
greeting[0] = "J"
print(greeting)
```

  2. Alternativa: crear un string nuevo

    ```python
greeting = "Hello world!"
new_greeting = "J" + greeting[1:]
print(new_greeting)
```

---
5. Búsquedas

  1. ¿Qué hace la siguiente función?

```python
def find(word, letter):
  index = 0
  while index < len(word):
    if word[index] == letter:
      return index
    index += 1
  return -1
```

  2. Es el opuesto a `s[n]`

  3. **Definición:** Recorrer una estructura y regresar algo cuando se encuentre lo que se está buscando.

  4. Ejercicio: Modificar `find` para que acepte un tercer parámetro que indique desde qué índice se comienza a buscar.

---
6. Conteo

  1. ¿Qué hace el siguiente código?

```python
word = "banana"
count = 0
for letter in word:
  if letter == 'a':
    count = count + 1
print(count)
```
  2. **Definición:** Inicializa una variable *contador* en 0, hace un recorrido en la estructura, y aumenta el contador cada que una condición se cumple.

  3. Ejercicio: Meter el código en una función y generalizarla para que busque una letra cualquiera.

---
7. Métodos de strings

  1. Ocupa sintaxis distinta a la de función. Pero funciona igual.
```python
word = "banana"
new_word = word.upper()
print(new_word)
```
  2. `find`
```python
word.find("a")
word.find("na")
word.find("na", 2)
word.find("na", 2, 5)
```
  3. Ejercicio: Leer la documentación de `count` y contar el número de `"a"` en `"bananas"`

---
8. Operadores booleanos

  1. `in`

```python
print("an" in "bananas")
print("z" in "bananas")
```
  2. Ejemplo: Imprime todas las letras de `word1` que están en `word2`

```python
def in_both(word1, word2):
  for letter in word1:
    if letter in word2:
      print(letter)
```
  3. Igualdad entre strings `==`

```python
if word == "bananas":
  print("La palabra es 'bananas'")
```
  4. Orden alfabético `<`, `>`

```python
if word < "banana":
  print("Tu palabra %s, va antes que 'banana'" % (word))
elif word > "banana":
  print("Tu palabra %s, va después que 'banana'" % (word))
else:
  print("Tu palabra es 'bananas'")
```
  4. MAYÚSCULAS > minúsculas

  5. Ejercicio: Función `alphabetical_order` que retorna la palabra que va antes sin importar mayúsculas.

---
9. Debugging

  1. Errores difíciles de identificar

```python
def is_reverse(word1, word2):
  '''
  Revisa si dos palabras son la misma palabra pero en reversa.

  word1: String
  word2: String
  '''
  if len(word1) != len(word2):
    return False
  i = 0
  j = len(word2)
  while j > 0:
    if word1[i] != word2[j]:
      return False
    i += 1
    j -= 1
  return True
```

  2. Ayuda: Imprimir los valores.

  3. Identificar errores (out of bound, última comparación)

## Tarea

1. Un slice puede tomar un tercer índice que especifique el "step size", que significa el número de espacios entre caracteres sucesivo. Ejemplo:
```python
fruit = "banana"
print(fruit[0:5:2])
# "bnn"
```

Un step size de -1 va desde atrás hacia adelante, así el slice [::-1] genera la cadena en reversa.

- [ ] Usa esta característica para escribir una versión de la función `is_palindrome` pero de una línea.

---
2. Lee la documentación de los métodos de str: `strip` y `replace` desde el intérprete o desde la documentación de Python en línea. Puedes consultar la documentación con `help`:
```python
help(str.strip)
```

- [ ] Experimenta con los métodos y luego describe qué hace cada uno.

**Consejo:** La documentación usa una sintaxis que puede confundir. Por ejemplo `find(sub[, start[, end]])`, los corchetes indican que es un argumento opcional. Por lo tanto `sub` es requerido, pero `start` es opcional, y si `start` es proporcionado, entonces `end` es opcional.

---
3. Las siguientes funciones están pensadas para revisar si un string contiene alguna letra en minúscula, pero algunas de estas funciones son incorrectas.

- [ ] Para cada una de las funciones, describe qué hace realmente la función (asumiendo que el parámetro es de tipo string).

```python
# 1.
def any_lowercase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False

#2
def any_lowercase2(s):
  for c in s:
    if 'c'.islower():
      return 'True'
    else:
      return 'False'

#3
def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag

#4
def any_lowercase4(s):
  flag = False
  for c in s:
    flag = flag or c.islower()
  return flag

#5
def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True
```

---
4. ROT13 es una forma debil de cifrado que requiere "rotar" cada letra en una palabra 13 lugares. Rotar una letra significa desplazarla por el alfabeto, volviendo al inicio si es necesario. Así la 'A' desplazada por 3 es 'D', y 'Z' desplazada por 1 es 'A'.

- [ ] Escribe una función llamada `rotate_word` que tome un string y un entero como parámetros, y que retorne una nueva string que contenga las letras de la cadena original "rotadas" por el entero proporcionado.

Por ejemplo `"cheer"` rotada por `7` es `"jolly"`, y `"melon"` rotado por `-10` es `"cubed"`.

**Consejo:** Puedes usar las funciones `ord` que convierte un caracter a su código numérico y `chr` que convierte códigos numéricos a caracteres. **No es necesario manejar acentos ni la letra 'ñ'**
