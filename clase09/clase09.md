# Clase 09

## Temas

0. [Moby project](https://github.com/Hyneman/moby-project/blob/master/moby/mwords/113809of.fic)

1. Abrir archivos con `open(file_name)`
```python
fin = open("words.txt")
print(fin)
```

2. Descripción con `print`

3. Leer el archivo `readline()`
```python
fin.readline()
```

4. Quitar los espacios y saltos de linea
```python
line = fin.readline()
word = line.strip()
print(word)
```

5. Ejemplo: [Imprimir todas las lineas](print_all.py)

6. Ejercicio: Imprimir todas las palabras con mas de 20 caracteres (sin contar saltos de línea).

---

## Tarea

1. Escribe una función llamada `has_no_e` que regrese `True` si la palabra proporcionada como argumento no contiene la letra `'e'`.
Usa esa función para imprimir las palabras en `words.txt` que no contengan la letra `'e'`, y calcula el porcentaje de estas.

2. Escribe una función llamada `avoids` que tome una palabra y un string con letras prohibidas, que regrese `True` si la palabra no usa ninguna de las letras prohibidas. Solicita al usuario una lista de caracteres prohibidos y luego imprime el número de palabras en `words.txt` que no contengan esas letras.

3. Escribe una función llamada `uses_only` que tome una palabra y un string de letras, y que regrese `True` si la palabra solamente contiene letras del string. Imprime todas las palabras que solo usan las letras `acefhlo`.

4. Escribe una función llamada `uses_all` que tome una palabra y un string de letras, y que regrese `True` si la palabra usa todas las letras del string al menos una vez. ¿Cuántas palabras en `words.txt` hay que use todas las vocales `"aeiou"`? ¿Y cuántas `"aeiouy"`?

5. Escribe una función llamada `is_abecedarian` que regrese `True` si las letras en la palabra proporcionada están en orden alfabético. ¿Cuántas palabras que cumplen esta condición hay?
