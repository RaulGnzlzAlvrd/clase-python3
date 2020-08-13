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
