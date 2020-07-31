# Clase 10

## Temas:

### 1. Listas
1. Secuencia de `values` llamados elementos
2. Creación de listas

```python
[10, 20, 30, 40]
["hola mundo", "python", "listas"]

# Esta contiene una lista anidada
["spam", 2.0, 5, [10, 20]]

# Lista vacía
[]
```

3. Asignar a variables

```python
cheesses = ['Cheddar', 'Edam', 'Gouda']
numbers = [1, 2, 3]
empty = []
print(cheesses)
# ['Cheddar', 'Edam', 'Gouda']

print(numbers)
# [1, 2, 3]

print(empty)
# []
```

---

### 2. Mutabilidad en listas
1. Acceso a elementos de listas

```python
print(cheesses[0])
# 'Cheddar'
```

2. Mutabilidad

```python
numbers = [42, 123]
numbers[1] = 5
print(numbers)
# [42, 5]
```

3. Reglas de índices (mismas que para strings)
  1. Cualquier expresión puede ser usada como índice.
  2. Si intentas acceder o modificar un elemento que no existe obtienes un error `IndexError`.
  3. Si el índice tiene un valor negativo, cuenta de derecha a izquierda sobre la lista.
4. Operador `in`

```python
cheeses = ['Cheedar', 'Edam', 'Gouda']
print('Edam' in cheeses)
# True

print('Brie' in cheeses)
# False
```

---

### 3. Recorridos en listas
1. Usando `for`

```python
cheeses = ['Cheedar', 'Edam', 'Gouda']

for cheese in cheeses:
  print(cheese)
# 'Cheedar'
# 'Edam'
# 'Gouda'
```

2. Modificar los elementos de la lista

```python
number = [42, 5]

for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

print(numbers)
# [84, 10]
```

3. Listas anidadas cuentan como un solo elemento

```python
t = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(len(t))
# 4

for element in t:
  print(t)

# [spam'
# 1
# ['Brie', 'Roquefort', 'Pol le Veq']
# [1, 2, 3]
```

---

### 4. Operaciones de listas

1. Concatenación

```python
a = [1, 2, 3, 4]
b = [5, 6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]
```

2. Repetición

```python
print([0] * 4)
# [0, 0, 0, 0]

print([1, 2, 3] * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

---

### 5. List slices

1. Notación de string slices: `[n:m]`

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
# ['b', 'c']

print(t[:4])
# ['a', 'b', 'c', 'd']

print(t[3:])
# ['d', 'e', 'f']

print(t[:])
# ['a', 'b', 'c', 'd', 'e', 'f']
```

> **Nota:** Es conveniente hacer una copia antes de realizar operaciones que modifican la lista

2. Asignar a un slice completo

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
# ['a', 'x', 'y', 'd', 'e', 'f']
```

---

### 6. Métodos de listas

1. Añadir al final de la lista: `append`

```python
t = ['a', 'b', 'c']
t.append('d')
print(t)
# ['a', 'b', 'c', 'd']
```

2. Extender una lista con otra: `extend`

```python
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
# ['a', 'b', 'c', 'd', 'e']
```

3. Ordenar la lista: `sort`

```python
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
# ['a', 'b', 'c', 'd', 'e']
```

4. Métodos vacíos

```python
t = t.sort()
print(t)
```

---

### 7. Reduce, map y filter

1. Sumar todos los número en una lista

```python
def add_all(t):
  total = 0 # Acumulador
    for x in t:
      total += x
  return total

nums = [1, 2, 3]
print(add_all(nums))
# 6

# Alternativa:
print(sum(nums))
# 6
```

2. **Reduce:** Operación que combina una secuencia de elementos y lo convierte en un solo valor
3. Capitalizar palabras

```python
def capitalize_all(t):
  res = [] # Acumulador
  for s in t:
    res.append(s.capitalize())
  return res

words = ["raúl", "gonzález", "alvarado"]
print(capitalize_all(words))
# ["Raúl", "González", "Alvarado"]
```

4. **Map:** Operación que mapea una función sobre cada elemento de una secuencia.
5. Solo mayúsculas

```python
def only_upper(t):
  res = []
  for s in t:
    if s.isupper():
      res.append(s)
  return res

words = ["HOLA", "mundo", "PYTHON", "WoRdS", "UPPER"]
print(only_upper(words))
# ["HOLA", "PYTHON", "UPPER"]
```

6. **Filter:** Operación que selecciona algunos elementos y filtra los otros.

---

### 8. Eliminar elementos

1. Eliminación con índice: `pop`

```python
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
# ['a', 'c']

print(x)
# 'b'

# Elimina el último elemento y lo regresa
last = t.pop()
```

2. Si no se necesita el valor: `del`

```python
t = ['a', 'b', 'c']
del t[1]
print(t)
# ['a', 'c']
```

3. Conociendo el elemento: `remove`

```python
t = ['a', 'b', 'c']
t.remove('b') # Regresa None
print(t)
# ['a', 'c']
```

4. Eliminar más de un elemento

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
# ['a', 'f']
```

---

### 9. Listas y Strings

> **String:** Secuencia de caracteres.
>
> **List:** Secuencia de valores.

1. Convertir a lista: `list`

```python
s = "spam"
t = list(s)
print(t)
# ["s", "p", "a", "m"]
```

2. Separar por palabras: `split`

```python
s = "I'm learning python"
t = s.split()
print(t)
# ["I'm", "learning", "python"]

# Parámetro opcional delimiter
s = "spam-spam-spam"
delimiter = "-"
t = s.slpit(delimiter)
print(t)
# ["spam", "spam", "spam"]
```

3. Convertir a string: `join`

```python
t = ["I'm", "learning", "python"]
delimiter = " " # Puede ser la cadena vacía
s = delimiter.join(t)
print(s)
# "I'm learning python"
```

---

### 10. Objetos y values

1. ¿Son referencias al mismo objeto?

```python
a = "banana"
b = "banana"
```

2. Operador `is`

```python
print(a is b)
# True
```

3. ¿Qué pasa con las listas?

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# False
```

> **Nota:** Las dos listas son *equivalentes* por que tienen los mismos elementos, pero no son *identicos* por que no son el mismo objeto.

4. Diferencia entre objetos y valores

---

### 11. Multiples referencias a objetos

1. Referencia al mismo objeto

```python
a = [1, 2, 3]
b = a # Son referencias al mismo objeto
print(a is b)
# True
```

2. Objetos mutables

```python
b[0] = 42
print(a)
# [42, 2, 3]
```

3. Evitar errores

```python
a = [1, 2, 3]
b = a[:]
b[0] = 42
print(a)
# [1, 2, 3]

print(b)
# [42, 2, 3]

# En objetos inmutables no hay problema con eso
a = "banana"
b = a
```

---

### 12. Listas como argumentos

1. Ejemplo: modificación de lista en una función

```python
def delete_head(t):
  del t[0]

letters = ['a', 'b', 'c']
del_head(letters)
print(letters)
# ['b', 'c']
```

2. Operaciones de modificación y de creación

```python
# append modifica la lista:
t1 = [1, 2]
t2 = t1.append(3)
print(t1)
# [1, 2, 3]
print(t2)
# None

# + crea una lista nueva:
t3 = t1 + [4]
print(t1)
# [1, 2, 3]

print(t3)
# [1, 2, 3, 4]
```

3. Ejemplos:

```python
# Mal ejemplo de delete_head
def bad_delete_head(t):
  t = t[1:]

t4 = [1, 2, 3]
bad_delete_head(t4)
print(t4)
# [1, 2, 3]
```

```python
# Alternativa creando una copia
def tail(t):
  return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)
# ['b', 'c']
```

---

## Tarea:
