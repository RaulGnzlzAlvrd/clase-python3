# Archivos (clase 14)

En esta clase se introduce la idea de programas "persistentes" que mantienen información en el almacenamiento permanente, también se muestra como usar diferentes tipos de almacenamiento permanente, como archivos y bases de datos.

## Temas:

### 1. Persistencia.

1. Los programas que hemos ejecutado producen información en pantalla y cuando finalizan, la información se pierde. Cuando se ejecuta de nuevo está en un estado "limpio".

2. Algunos programas que se ejecutan todo el tiempo sí son persistentes, guardan la información necesaria en almacenamiento permanente (como un disco duro) y si se apaga el sistema, pueden reanudar su ejecución cargando la información desde el disco duro. Algunos ejemplos de estos programas:
  1. Sistemas operativos
  2. Servidores web

3. Se pueden usar archivos de texto o incluso bases de datos para persistir información (ya se vio como leer de un archivo pero no como escribir en uno).

### 2. Leer y escribir.

1. Un archivo de texto es una secuencia de caracteres almacenados en un medio de almacenamiento permanente.

2. Para escribir sobre un archivo se abre con `open` en modo write:

```python
fout = open('output.txt', 'w')
```

  1. Si el archivo ya existía se va a eliminar todo su contenido y empieza como si estuviera vacío.
  2. Si el archivo no existe, se crea uno nuevo.

3. La función `open` no regresa un objeto que nos provee métodos para trabajar con el archivo:

```python
>>> line1 = "This here's the wattle,\n"
>>> fout.write(line1)
24
```

4. El objeto sabe donde se quedó, así que sigue escribiendo al final del archivo.

```python
>>> line2 = "the emblem of our land.\n"
>>> fout.write(line2)
24
```

5. Cuando se termina de trabajar se tiene que cerrar el archivo

```python
>>> fout.close()
```

### 3. El operador format

1. Los argumentos de `write` deben ser de tipo string.

```python
x = 52
fout.write(str(x))
```

2. Alternativa con operador format (`%` operador módulo para integers)

```python
>>> camels = 42
>>> '%d' % camels
'42'

>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'
```

3. Partes involucradas
  1. format string: `'I have spotted %d camels.'`
  2. format sequence: `%d`

> **Nota:** La secuencia de formato `%d` indica que el segundo operando debe ser formateado como entero decimal.

4. Múltiples secuencias de formato, el segundo argumento debe ser un tupla:

```python
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
```

> **Nota:** La secuencia de formato `%g` es para flotantes, y `%s` para strings.

5. El número y el tipo de elemento de la tupla debe coincidir con las secuencias de formato.

```python
>>> '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> '%d' % 'dollars'
TypeError: %d format: a number is required, not str
```

> **Nota:** No se va a ver a detalle todas las secuencias de formato, se puede encontrar más información en su [documentación](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

> **Nota:** Hay otra forma de dar formato que es el método `format` de strings. Para más detalles en su [documentación](https://docs.python.org/3/library/stdtypes.html#str.format)

### 4. Nombres de archivos y rutas (paths)

1. Los archivos se organizan en **directorios** (también llamados carpetas).

2. Cada programa que se ejecuta tiene un directorio actual, que es el directorio default para muchas operaciones. Por ejemplo cuando se abre un archivo para leer, python lo busca en el directorio actual.

3. Módulo `os` (operating system):

4. Función `getcwd` (get current working directory)

```python
>>> import os
>>> cwd = os.getcwd()
>>> cwd # current working directory
'/home/raul-ga/Documentos/cursos/python/clase14'
```

5. La cadena `'/home/raul-ga/Documentos/cursos/python/clase14'` identifica a un archivo o directorio y se le llama **path** (ruta).

6. Un nombre de archivo simple como `'clase14.md'` también se considera un path, pero es un **path relativo**, por que es relativo al directorio actual (current directory). Ejemplo: Si el directorio actual es `'/home/raul-ga/Documentos/cursos/python/clase14'`, el path relativo `'clase14.md'` hace referencia a `'/home/raul-ga/Documentos/cursos/python/clase14/clase14.md'`

7. Cuando un path empieza con `/` es llamado **path absoluto**, y no depende del directorio actual.
  1. directorio actual: `'/home/raul-ga/Documentos/cursos/python/clase14'`
  2. path relativo: `'clase14.md'`
  3. path absoluto: `'/home/raul-ga/Documentos/cursos/python/clase14/clase14.md'`

8. Para obtener el path absoluto en python:

```python
>>> os.path.abspath("clase14.md")
'/home/raul-ga/Documentos/cursos/python/clase14/clase14.md'
```

9. Funciones de `os.path` para trabajar con nombres de archivos y paths.

```python
>>> os.path.exists('hola.txt')
True

>>> os.path.isdir('hola.txt')
False

>>> os.path.isdir('/home/raul-ga')
True

>>> os.path.isfile('/home/raul-ga/hola.txt')
True
```

10. Lista de archivos y directorios en el directorio actual:

```python
os.listdir(cwd)
['clase14.md', 'ejemplo.py', 'soluciones']
```

11. Ejemplo: "Caminar" en los directorios e imprimir los nombres de archivos, tanto de la carpeta actual como de subcarpetas:

```python
def walk(dirname):
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name) # Toma un directorio y el nombre de un archivo y los junta en un path completo
    if os.path.isfile(path):
      print(path)
  else:
    walk(path)
```

### 5. Cachando excepciones.

1. Pueden pasar muchas cosas mal cuando se escribe o lee de un archivo. Por ejemplo (hay al menos 21 tipos de errores):

```python
# Abrir un archivo que no existe
>>> fin = open('bad_file')
IOError: [Errno 2] No such file or directory: 'bad_file'

# Si no se tiene permisos para abrir un archivo
>>> fout = open('/etc/passwd', 'w')
PermissionError: [Errno 13] Permission denied: '/etc/passwd'

# Si intentas abrir un directorio para leer
>>> fin = open('/home')
IsADirectoryError: [Errno 21] Is a directory: '/home'
```

2. Intentarlo y si falla hacerce cargo de ello

```python
try:
  fin = open('bad_file')
except:
  print('Something went wrong.')
```

3. Cachar una excepción: arreglar el problema, intentar de nuevo, o terminar el programa de forma amigable.

### 6. Bases de datos

1. Son usadas como diccionarios, cambia en que esta se almacena en disco duro

2. Módulo `dbm`

```python
>>> import dbm
# Abrir la base es similar a abrir archivos
>>> db = dbm.open('captions.db', 'c') # La c dice que lo cree si no existe
```

3. Operaciones similares a diccionarios

```python
>>> db['cleese.png'] = 'Photo of John Cleese.'
>>> db['cleese.png']
b'Photo of John Cleese.'
```

4. byte objects. Similares a strings. Comienzan con `b`

5. Reasignar una llave

```python
>>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
>>> db['cleese.png']
b'Photo of John Cleese doing a silly walk.'
```

6. Iterar por un diccionario (no hay métodos `keys` ni `items`)

```python
for key in db:
  print(key, db[key])
```

7. Cerrar la base

```python
>>> db.close()
```

### 7. Pickling

1. Limitación de bases es que solo almacenan strings y bytes

2. Módulo `pickle`: convertir cualquier tipo a string y viceversa

3. Función `dumps`

```python
>>> import pickle
>>> t = [1, 2, 3] # Así podríamos guardar una lista en una base de datos
>>> pickle.dumps(t)
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
```

4. Función `loads`

```python
>>> t1 = [1, 2, 3]
>>> s = pickle.dumps(t1)
>>> t2 = pickle.loads(s)
>>> t2
[1, 2, 3]
```

5. El valor nuevo es igual pero no es el mismo (copiamos el objeto)

```python
>>> t1 == t2
True
>>> t1 is t2
False
```

### 8. Pipes

1. Interfaz para comunicarse con el sistema operativo: **shell**

2. Ejecutar comandos del shell desde python usando pipe objects: `popen`

```python
>>> cmd = "ls -l" # El parámetro debe de ser un comando de shell
>>> fp = os.popen(cmd)
```

3. El objeto que retorna se comporta como un archivo abierto

4. Se puede leer la salida del comando linea a linea con `readline` o todo con `read`

```python
>>> res = fp.read()
```

5. Cerrar al finalizar

```python
>>> stat = fp.close() # Si regresa None es que terminó sin fallos
>>> stat
None
```

6. Ejemplo: `md5sum`

```python
>>> filename = 'book.tex'
>>> cmd = 'md5sum ' + filename
>>> fp = os.popen(cmd)
>>> res = fp.read()
>>> stat = fp.close()
>>> print(res)
1e0033f0ed0656636de0d75144ba32e0 book.tex
>>> print(stat)
None
```

7. Ejercicio: Errores que pueda ocasionar los espacios en nombres de archivos.

### 9. Escribir módulos

1. Cualquier archivo con código de python puede ser usado como un módulo

2. Ejemplo: `linecount`

3. Importarlo como módulo

```python
>>> import ejemplo
7
>>> ejemplo
<module 'ejemplo' from 'ejemplo.py'>
>>> ejemplo.linecount('clase14.md')
400
```

4. Cuando importar un módulo solo quieres las funciones y variables que define, no que haga llamadas a funciones al ejecutar. Se usa el siguiente idiom en modulos:

```python
if __name__ == '__main__':
  print(linecount('ejemplo.py'))
```

> **Nota:** La variable `__name__` es definida en cuando se ejecuta el programa. Si se ejecuta como script, `__name__` toma el valor de `"__main__"`. Cuando es importado como módulo entonces toma como valor el nombre del módulo.

5. Ejercicio: Variable `__name__`.

### 10. Debugging

1. Para detectar los espacios en blanco de un string se puede usar la función `repr`:

```python
>>> s = '1 2\t 3\n 4'
>>> print(s)
1 2   3
 4

>>> print(repr(s))
'1 2\t 3\n 4'
```

2. En modo interactivo no es tan necesario, pero en modo script sí.

---
## Tarea.

### Ej. 1:

Escribe una función llamada `sed` que tome como argumentos un patrón de string, un string de reemplazo, y dos nombres de archivos; el programa debe leer el primer archivo y escribir todo su contenido en el segundo archivo (si no existe lo crea). Si el patrón de string aparece en el archivo debe ser sustituido por el string de reemplazo.

Si un error ocurre mientras se lee, se escribe o se cierran los archivos, tu programa debe cachar la excepción, imprimir un mensaje de error y terminar.

### Ej. 2:

Descarga el siguiente [archivo](http://thinkpython2.com/code/anagram_sets.py), y lee el código para entenderlo. Es una implementación de la solución al ejercicio de los anagramas, este crea un diccionario que mapea de un string de letras ordenadas a una lista de palabras que pueden ser construidas con dichas letras. Por ejemplo: `'opst'` mapea a la lista `['opts', 'post', 'pots', 'spot', 'stop', 'tops']`.

Escribe un módulo que importe `anagram_sets`, e implementa dos funciones adicionales: `store_anagrams` que almacene un diccionario de anagramas en un archivo; y `read_anagrams` que busque una palabra en tu archivo de anagramas y regrese una lista con sus anagramas.

### Ej. 3:

En una colección muy grande de canciones mp3, suele haber mas de una copia de la misma canción almacenada en distintos directorios o con distintos nombres. Debe buscar todos los duplicados.

Consejos:

1. Escribe una función que busque en un directorio y en todos sus subdirectorios de forma recursiva, y regresa una lista con todos los paths absolutos de todos los archivos con extensión mp3.

2. Usa el comando de Unix `md5sum` para identificar duplicados, también usa un diccionario para almacenarlos.

3. Cuidado con los espacios en nombres de canciones. Busca como lidiar con ellos desde la consola y luego implementalo en python.
