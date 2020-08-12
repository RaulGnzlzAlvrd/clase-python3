# Complemento (clase 10)

## Tarea:

### Ej. 1:

- [ ] Escribe una función que lea el archivo `words.txt` y construya una lista donde cada elemento sea una palabra.

---
### Ej. 2:

Para comprobar si un elemento está en una lista o no, podrías usar el operador `in`, pero sería lento porque busca atraves de las palabras en orden.

Como las palabras están en orden alfabético (**es decir están ordenadas**), podemos acelerar el proceso de búsqueda con una *búsqueda binaria* (también conocida como *búsqueda de bisección*), la cual es similar a cuando buscas una palabra en un diccionario. Empiezas por la mitad y revisas si la palabra que estás buscando está antes que la palabra que está al medio de la lista. Si es el caso, entonces buscas en la primera mitad de la lista de la misma manera. De otro modo, buscas en la segunda mitad.

De este modo, disminuyes el espacio de búsqueda a la mitad. Si la lista tiene 113809 palabras, este método va a tomar aproximadamente 17 pasos en encontrar la palabra o concluir que no está ahí.

- [ ] Escribe una función llamada `in_bisect` que tome una **lista ordenada** y una palabra a buscar, regresa `True` si la palabra está en la lista, `False` si no lo está. O podrías leer la documentación del módulo `bisect` y usar eso.

---
### Ej. 3:

Dos palabras son un **"par reversible"** si cada una es la reversa de la otra. Por ejemplo:

- 'keep' y 'peek'
- 'dog' y 'god'
- 'evil' y 'live'


- [ ] Escribe un programa que encuentre todos los pares reversibles en la lista de palabras.

---
## Ej. 4:

Dos palabras se **"entrecruzan"** si tomando letras alternadas de cada una se forma una nueva palabra. Por ejemplo "shoe" y "cold" se entrecruzan para formar "schooled".

- [ ] Escribe un programa que encuentre todos los pares de palabras que se entrecruzan. Pista: No busques entre todos los posibles pares de palabras.
