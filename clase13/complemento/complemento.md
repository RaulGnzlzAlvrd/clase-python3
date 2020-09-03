# Complemento clase 13.

## Temas:

### 1. Histograma de palabras.

1. Código solución del libro.

```python
import string

def process_file(filename):
  hist = dict()
  fin = open(filename)
  for line in fin:
    process_line(line, hist)
  return hist

def process_line(line, hist):
  line = line.replace('-', ' ')
  for word in line.split():
    word = word.strip(string.punctuation + string.whitespace)
    word = word.lower()
    hist[word] = hist.get(word, 0) + 1

hist = process_file('book.txt')
```

2. Descripción de `process_file` y `hist` como acumulador.

3. Descripción de `process_line`.

4. Saltar headers:

```python
def process_file(filename):
  hist = dict()
  fin = open(filename)

  skip_gutenberg_header(fin)

  for line in fin:
    if "END OF THIS PROJECT GUTENBERG EBOOK" in line:
      break
    process_line(line, hist)

  return hist

def skip_gutenberg_header(fin):
  for line in fin:
    if "START OF THIS PROJECT GUTENBERG EBOOK" in line:
      break
```

5. Contar el número total de palabras.

```python
def total_words(hist):
  return sum(hist.values())
```

6. Contar el número de palabras distintas.

```python
def different_words(hist):
  return len(hist)
```

7. Probando con distintos libros.

```python
books = ["book1.txt", "book2.txt", "book3.txt"]
for book in books:
  hist = process_file(book)
  print('Total number of words:', total_words(hist))
  print('Number of different words:', different_words(hist))
```

---
### 2. 20 palabras más usadas.

1. Ordenar por frecuencia.

```python
def most_common(hist):
  t = []
  for key, value in hist.items():
    t.append((value, key))
  t.sort(reverse=True)
  return t
```

> **Nota:** Cuidado al poner tuplas como parámetros ya que el intérprete lanzaría un error: `t.append(value, key)` se lee como dos parámetros en vez de como una tupla.

---
2. Imprimir solo 10

```python
t = most_common(hist)
print('The 10 most common words are:')
for freq, word in t[:10]:
  print(word, freq, sep='\t')

# The 10 most common words are:
# the   6623
# of    3521
# and   3300
# to    1852
# in    1684
# a	    1671
# is    1473
# be    1045
# or    986
# with  757
```

---
### 3. Parámetros opcionales.

1. Crear funciones con parámetros opcionales.

```python
# El primer parámetro es obligatorio y el segundo opcional
def print_most_frequent(hist, num=10):
  t = most_common(hist)
  print('The', num, 'most common words are:')
  for freq, word in t[:num]:
    print(word, freq, sep='\t')
```

2. Sobreescribir el valor default.

```python
print_most_frequent(hist) # num obtiene el valor default
print_most_frequent(hist, 20) # num obtiene el valor del argumento
```

> **Nota:** Si una función requiere de argumentos obligatorios y opcionales, todos los parámetros obligatorios van antes que los opcionales.

---
### 4. Operación resta en diccionarios.

1. Encontrar todas las palabras de un conjunto que no están en el otro.

```python
def substract(d1, d2):
  res = dict()
  for key in d1:
    if key not in d2:
      res[key] = None
  return res

words = process_file("words.txt")
diff = substract(hist, words)
print("Words in the book that aren't in the word list:")
for word in diff:
  print(word, end=' ')
```

---
### 5. Análisis de Markov.

1. Formar frases aleatorias.

2. **Análisis de Markov:** Caracterizar, dada una secuencia de palabras, la probabilidad de las palabras que le pueden seguir.

> Half a bee, philosophically, </br>
Must, ipso facto, half not be. </br>
But **half the** bee has got to be </br>
Vis a vis, its entity. D’you see? </br>
>
>But can a bee be said to be </br>
Or not to be an entire bee </br>
When **half the** bee is not a bee </br>
Due to some ancient injury? </br>

3. Obtenemos un mapeo.

| Prefijos | Sufijos |
| -------- |---------|
| half the | bee     |
| the bee  | has, is |

4. Generar texto a partir del mapeo.
  1. Elegir cualquier prefijo.
  2. Escoger uno de sus posibles sufijos.
  3. Formar un nuevo prefijo con el final del prefijo anterior y el sufijo.
  4. Repetir.


  > **Nota:** El prefijo puede ser de cualquier tamaño, no solamente 2.

5. Tarea:
  - [ ] Escribe un programa que lea un texto de un archivo y le haga un análisis de Markov. El resultado debería ser un mapeo de los prefijos a una colección de posibles sufijos. El programa debe funcionar con distintas longitudes de prefijos.

  - [ ] Añade una función al programa anterior para que genere texto aleatorio basado en el análisis de Markov. Prueba tu programa usando algún libro. ¿Qué pasa si aumentas el tamaño de los prefijos?

  - [ ] Combina dos o más libros de distintos autores, géneros y épocas para ver resultados más interesantes.

---
### 6. Estructuras de datos.

1. Puntos a considerar:
  1. Cómo representar los prefijos.
  2. Cómo representar la colección de posibles sufijos.
  3. Cómo representar el mapeo de prefijos a sufijos.

---
## Tarea:

Implementar el análisis de Markov con las consideraciones vistas en clase.
