# Archivos (clase 14)

En esta clase se introduce la idea de programas "persistentes" que mantienen información en el almacenamiento permanente, también se muestra como usar diferentes tipos de almacenamiento permanente, como archivos y bases de datos.

## Temas:

### Persistencia.

1. Los programas que hemos ejecutado producen información en pantalla y cuando finalizan, la información se pierde. Cuando se ejecuta de nuevo está en un estado "limpio".

2. Algunos programas que se ejecutan todo el tiempo sí son persistentes, guardan la información necesaria en almacenamiento permanente (como un disco duro) y si se apaga el sistema, pueden reanudar su ejecución cargando la información desde el disco duro. Algunos ejemplos de estos programas:
  1. Sistemas operativos
  2. Servidores web

3. Se pueden usar archivos de texto o incluso bases de datos para persistir información (ya se vio como leer de un archivo pero no como escribir en uno).

### Leer y escribir.
