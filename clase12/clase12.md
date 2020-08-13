# Tuplas (clase 12)

En esta clase se ve el tipo de dato **tupla**, y como listas, diccionarios y tuplas se puedes usar en conjunto. También se ve una característica para poder construir funciones con cantidad de argumentos variables (operadores **gather** y **scatter**).

---
## Temas:

### 1. Tuplas son inmutables

1. Las tuplas son una secuencia de valores, y estos valores pueden ser de cualquier tipo. Al igual que las listas, se accede a sus elementos con un índice base 0. Son casi como listas pero difieren en que las tuplas son **inmutables**.

2. Tupla: listado de valores separados por comas.

```python
t = 'a', 'b', 'c', 'd', 'e'

# Puede ser encerrado en paréntesis aunque no es necesario
t = ('a', 'b', 'c', 'd', 'e')

# Tuplas de un elemento deben tener una coma al final
t = 'a',

# WRONG!
t = ('a')
print(type(t))
# <class 'str'>

# Goog!
t = ('a',)

# Crear una tupla vacía
t = tuple()
print(t)
# ()
```  

3. Crear una tupla a partir de una **secuencia (string, lista o tupla)**.

```python
t = tuple('lupins')
print(t)
# ('l', 'u', 'p', 'i', 'n', 's')
```

> **Nota:** Como la palabra `tuple` es el nombre de una función en python, no se puede usar como nombre de variable o función (en los ejemplos usamos `t`).

4. Operadores de tuplas.

```python
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
# a
print(t[1:3])
# ('b', 'c')
```

5. Modificar elementos de tuplas.

```python
t[0] = 'A'
# TypeError: object doesn't support item assignment
```

6. Alternativa: Reasignar la variable a una tupla nueva.

```python
t = ('A',) + t[1:]
print(t)
# ('A', 'b', 'c', 'd', 'e')
```

7. Comparación de secuencias.

```python
print((0, 1, 2) < (0, 3, 4))
# True

print((0, 1, 2000000) < (0, 3, 4))
# True
```

---
### 2. Asignaciones en modo tupla

1. Hacer swap en dos variables:

```python
temp = a
a = b
b = temp
```

2. Tuple assignment:

```python
# Las expresiones son evaluadas antes de la asignación
a, b = b, a

# Deben de coincidir en número
a, b = 1, 2, 3
# ValueError: too many values to unpack
```

> **Nota:** Diferencia cuando son tuplas de un elemento:
> ```python
> t, = 1,
> print(t)
> # 1
> ```
>
> ```python
> t = 1,
> print(t)
> # (1,)
> ```

3. El lado derecho puede ser cualquier sequencia.

```python
addr = 'monty@python.org'
uname, domain = addr.split('@') # split() nos da una lista

print(uname)
# monty

print(domain)
# python.org
```

---
### 3. Regresar tuplas desde funciones

1. Regresar una tupla como valor es igual a regresar multiples valores.

2. Calcular el cociente y el residuo de una división:

```python
quot = x // y
rem = x % y
```

3. Alternativa con `divmod`:

```python
t = divmod(7, 3)
print(t)
# (2, 1)

quot, rem = divmod(7, 3)
print(quot)
# 2

print(rem)
# 1
```

4. Ejemplo: Calcular el mayor y el menor elemento en una secuencia:

```python
def min_max(s):
  return min(s), max(s)
```

---
### 4. Funciones con numero de argumentos variables

1. El perador `*`(en los parámetros de la función) recolecta (**gathers**) los argumentos en una tupla.

```python
def print_all(*args):
  print(args)

print_all(1, 2.0, '3')
# (1, 2.0, '3')
```

> **Nota:** Por convención la tupla se le llama `args`, pero puede tener cualquier otro nombre.

2. El complemento de gathers es **scatter** (dispersa).

```python
t = (7, 3)
quot, rem = divmod(t)
# TypeError: divmod expected 2 arguments, got 1

quot, rem = divmod(*t)
```

3. Algunas funciones de python aceptan múltiples argumentos.

```python
print(max(1, 2, 3))
# 3

print(sum(1, 2, 3))
# TypeError: sum expected at most 2 arguments, got 3
```

4. Ejercicio: función `sum_all` que tome cualquier número de argumentos y regrese la suma de estos.

---
### 5. Listas y tuplas

1. Función `zip`: Toma dos o más secuencias y las intercala (como un cierre en la ropa).

```python
s = 'abc'
t = [0, 1, 2]
z = zip(s, t)
print(z)
# <zip object at 0x7f7d0a9e7c48>
```

2. El objeto sabe como *iterar*, su uso más común es en un ciclo `for`:

```python
for pair in zip(s, t):
  print(pair)
```

3. Un objeto zip, es una clase de **iterador**, este va iterando sobre una secuencia. Son similares a las listas pero no se puede acceder a sus elementos por su índice.

4. Convertir objeto zip a lista:

```python
l = list(zip(s, t))
print(l)
# [('a', 0), ('b', 1), ('c', 2)]
```

5. Hacer zip a secuencias de distinto tamaño.

```python
l = list(zip('Anne', 'Elk'))
print(l)
# [('A', 'E'), ('n', 'l'), ('n', 'k')]
```

6. Asignación estilo tupla en `for`.

```python
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
  print(number, letter)

# 0 a
# 1 b
# 2 c
```

7. Atravesar dos secuencias al mismo tiempo (`for`, `zip`, `tuple assigment`).

```python
def has_match(t1, t2):
  """
  Toma dos secuencias t1 y t2, regresa True si hay algún índice i tal que t1[i] == t2[i]
  """
  for x, y in zip(t1, t2):
    if x == y:
      return True
  return False
```

8. Función `enumerate`: crea un objeto enumerate, que tiene tuplas con índices y elementos.

```python
for index, element in enumerate('abc'):
  print(index, element)
# 0 a
# 1 b
# 2 c
```

---
### 6. Diccionarios y tuplas

1. Método de diccionario: `items`. Regresa una secuencia de tuplas, con pares llave-valor.

```python
d = {'a':0, 'b':1, 'c':2}
t = d.items()


print(t)
# dict_items([('c', 2), ('a', 0), ('b', 1)])
```

2. Usado en un `for`:

```python
for key, value in d.items():
  print(key, value)

# c 2
# a 0
# b 1
```

3. Construir un diccionario a partir de una secuencia de tuplas.

```python
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)
# {'a': 0, 'c': 2, 'b': 1}
```

4. Ayudandonos de `zip`

```python
d = dict(zip('abc', range(3)))
print(d)
# {'a': 0, 'c': 2, 'b': 1}
```

5. Método de diccionarios `update`. Acepta mismos parámetros que `dict`.

6. Usar tuplas como llaves.

```python
directory = dict()
fname = "John"
lname = "Doe"
number = "5566778899"
directory[lname, fname] = number

for last, name in directory:
  print(name, last, directory[last, name])
```

---
### 7. Secuencias de secuencias

1. En muchos de los ejemplos se puede usar listas de listas o tuplas de tuplas.

2. Strings:
  - Limitadas a que sus elementos sean caracteres.
  - Son inmutables-
  - Si se quieren modificar sus caracteres lo mejor es usar una lista de caracteres.

3. Listas:
  - Son mutables.
  - No pueden ser usadas como llaves en diccionarios.

4. Tuplas:
  - Se pueden usar en una expresión `return` de una forma más sencilla que las listas.
  - Pueden ser usadas como llaves en diccionarios.
  - Pueden usarse para pasar múltiples argumentos a una función.
  - Son inmutables y por lo tanto no tienen metodos `sort` y `reverse` (que las modifica).

> **Nota:** Python tiene funciones `sorted` y `reversed` que acepta como parámetro cualquier tipo de secuencia y regresa una copia ordenada o un iterador que recorre la secuencia en reversa, respectivamente.

---
### 8. Debugging

1. Estructuras de datos compuestas.

2. Errores de forma en estructuras de datos.

3. [Módulo](http://thinkpython2.com/code/structshape.py) `structshape`.

```python
from structshape import structshape

t = [1, 2, 3]
structshape(t)
# 'list of 3 int'

t2 = [[1,2], [3,4], [5,6]]
structshape(t2)
# 'list of 3 list of 2 int'

t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
structshape(t3)
# 'list of (3 int, float, 2 str, 2 list of int, int)'

s = 'abc'
lt = list(zip(t, s))
structshape(lt)
# 'list of 3 tuple of (int, str)'

d = dict(enumerate(s))
structshape(d)
# 'dict of 3 int->str'
```
---
## Tarea:

### Ej. 1:
Escribe una función llamada `most_frequent` que tome un string e imprima las letras en orden decreciente de frecuencia.
