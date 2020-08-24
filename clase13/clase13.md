# Caso de estudio: Elección de estructuras de datos (clase 13)

## Temas:

### 1. Módulo `string`

1. Cadenas especiales:

```python
>>> import string
>>> string.whitespace
' \t\n\r\x0b\x0c'
>>>
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>>
>>>string.digits
'0123456789'
```

2. Método `translate`

```python
def get_table():
  table = dict()
  for c in string.punctuation:
    table[ord(c)] = ord(' ')
  return table

s = "¿Cómo has estado, amigo?\nEspero que bien."
a = s.translate(get_table())
print(a)
# ¿Cómo has estado  amigo
# Espero que bien
```

3. Ejercicio: Alternativas con `strip` y `replace`.

---
### 2. Números aleatorios

1. Determinismo y no determinismo.

2. Números pseudoaleatorios.

3. Módulo `random` y función `random`:

```python
import random

for i in range(10):
  x = random.random()
  print(x)
```

4. Función `randint`:

```python
>>> random.randint(5, 10)
5
>>> random.randint(5, 10)
4
>>> random.randint(5, 10)
10
```

4. Función `choice`:

```python
>>> t = [1, 2, 3]
>>> random.choice(t)
2
>>> random.choice(t)
3
```

5. Ejercicio: Escribe una función llamada `choose_from_hist` que tome un histograma (como los que ya hemos definido antes), y regrese una llave aleatoria del histograma, escogida con probabilidad en proporción a la frecuencia. Por ejemplo:

```python
t = ['a', 'a', 'b']
hist = histograma(t)
print(hist)
# {'a': 2, 'b': 1}

# Debe elegir 'a' con probabilidad 2/3 y 'b' con probabilidad 1/3
choosen = choose_from_hist(hist)
```

---
## Tarea:

### Ej. 1:
Escribe un programa que lea un archivo, descomponga cada línea en palabras, quite los espacios en blanco y signos de puntuación de las palabras y las convierta a minúsculas. Guarda las palabras en la estructura que consideres más adecuada.

**Pista:** Algunos métodos que tal vez te puedan ayudar son: `strip`, `replace` y `translate`. También te puedes ayudar del módulo `string`.

---
### Ej. 2:
Ve al [Porjecto Gutenberg](http://gutenberg.org) y descarga algún libro en formato txt.

Modifica tu programa del ejercicio anterior para que lea el libro que descargaste, que se salte los headers y que procese el demás texto como antes.

Luego modifica tu programa para contar el número total de palabras en el libro y el número de veces que es usada cada palabra.

Modifica el programa para que ahora imprima el número de palabras diferentes usadas en el libro. Compara esto con otros dos libros distintos. ¿En qué libro se ocupa un vocabulario más extenso?

---
### Ej. 3:
Modifica el programa anterior para imprimir las 20 palabras más usadas en el libro.

Vuelve a modificar el programa para que lea el archivo `words.txt` e imprima todas las palabras en el libro que no están en la lista de palabras.
