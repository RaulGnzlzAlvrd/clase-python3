# Clase 11

## Temas:

### 1. Diccionarios como mapeos

1. Son más generales que una lista.
2. Sus índices pueden ser casi de cualquier tipo
3. Pares llave-valor (key-value)
4. Representa un mapeo donde cada llave tiene un solo valor
5. Ejemplo: creación de un diccionario

```python
# Creamos un diccionario vacío, representado por corchetes
eng2esp = dict()
print(eng2esp)
# {}

eng2esp['one'] = 'uno'
print(eng2esp)
# {'one': 'uno'}
```

6. Forma alternativa de creación (de diccionarios)

```python
eng2esp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2esp)
# {'one': 'uno', 'two': 'dos', 'three': 'tres'}
```

7. Acceder a elementos en diccionarios

```python
print(eng2esp['two'])
# dos

print(eng2esp['four'])
# KeyError: 'four'
```

8. Tamaño del diccionario

```python
size = len(eng2esp)
print(size)
# 3
```

9. Operador `in` (solo para **keys**)

```python
'one' in eng2esp
# True

'uno' in eng2esp
# False
```

10. Alternativa de `in` para **values**

```python
vals = eng2esp.values()
'uno' in vals
# True
```

11. Algoritmos de búsqueda (para `in`) en diccionarios (hashtable) y listas (recorridos).

---
### 2. Colección de contadores

1. Problema: Saber cuántas veces aparece cada letra de una cadena
  1. Podríamos crear 26 variables, una por cada letra del alfabeto. Luego podemos recorrer el string y, por cada caracter, incrementar su contador correspondiente, probablemente usando condicionales encadenados (`if` y `elif`).
  2. Podríamos crear una lista con 26 elementos. Luego convertir cada caracter a un número (tal vez usando la función `ord`), usar ese número como índice para la lista e incrementar el contador correspondiente a cada letra.
  3. Podrías crear un diccionario con caracteres como llaves, y contadores como sus correspondientes valores. La primera vez que vemos un caracter, lo añades al diccionario. Después incrementaríamos en uno el contador correspondiente.
2. Implementaciones.

```python
def histograma(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d


h = histograma('brontosaurus')
print(h)
# {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
```

3. Método `get`

```python
h = histograma("a")
print(h)
# {'a': 1}

value = h.get('a', 0)
print(value)
# 1

value = h.get('c', 0)
print(value)
# 0
```

4. Ejercicio: Modificar la función `histograma` usando el método `get`.

---
### 3. Ciclos y diccionarios

1. Usando `for`

```python
def print_hist(h):
  for key in h:
    print(key, h[key])

h = histograma("parrot")
print_hist(h)
# p 1
# a 1
# r 2
# o 1
# t 1
```

2. Imprimirlos de forma ordenada: función `sorted`

```python
def print_hist(h):
  for key in sorted(h):
    print(key, h[key])

h = histograma("parrot")
print_hist(h)
# a 1
# o 1
# p 1
# r 2
# t 1
```

---
### 4. Reverse lookup

1. Lookup: Dado un diccionario `d` y una llave `key`, es facil obtener el valor `value` correspondiente a `key`

```python
value = d[key]
```

2. ¿Y si tenemos `d` y `value` y queremos encontrar `key`? Hay dos posibilidades:
  1. Puede haber más de una llave `k` que le corresponda el valor `value`.
  2. No hay una forma simple de hacer esta operación
3. Ejemplo:

```python
def reverse_lookup(d, value):
  '''
  Toma un diccionario y un valor y devuelve la primera llave que
  le corresponde ese valor
  '''
  for key in d:
    if d[key] == value:
      return key
  # El parámetro es opcional
  raise LookupError("No se encontró el valor en el diccionario.")
```

4. Expresión `raise`

```python
h = histogram('parrot')
key = reverse_lookup(h, 2)
print(key)
# 'r'

key = reverse_lookup(h, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 5, in reverse_lookup
# LookupError
```

> **Nota:** Hacer este tipo de búsquedas es muy lento.

---
### 5. Diccionarios y listas

1. Invertir un diccionario

```python
def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse

hist = histograma('parrot')
print(hist)
# {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}

inverse = invert_dict(hist)
print(inverse)
# {1: ['p', 'a', 'o', 't'], 2: ['r']}
```

2. Listas como valores y como llaves

```python
t = [1, 2, 3]
d = dict()
d[t] = 'oops'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# TypeError: list objects are unhashable
```

3. Funciones hash y tipos mutables

### 6. Memorización

1. Ejemplo: fibonacci

```python
known = {0: 0, 1: 1}

def fibonacci(n):
  if n in known:
    return known[n]
  res = fibonacci(n - 1) + fibonacci(n - 2)
  known[n] = res
  return res
```

### 7. Variables globales

1. **Variables globales**: Declaración de variables fuera de funciones, se puede acceder a ellas desde cualquier función.

2. **Flags:** Variables globales y booleanas que indican si una condición es verdadera.

```python
verbose = True

def example1():
  if verbose:
    print('Running example1')
```

3. Reasignar variables globales

```python
been_called = False

def example2():
  been_called = True # WRONG

def example2():
  global been_called
  been_called = True
```
