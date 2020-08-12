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
