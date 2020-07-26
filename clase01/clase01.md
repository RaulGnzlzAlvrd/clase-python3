# Primera clase

## Puntos a cubrir
1. Resolución de problemas.
Resolución de problemas es la herramienta más importante de un científico de la computación. Consiste en la habilidad de formular problemas, pensar de forma creativa en soluciones y expresar una solución de manera clara y concisa

2. Lenguajes de alto y bajo nivel.
Los lenguajes de bajo nivel que son los que entienden directamente las computadoras, y para que un lenguaje de alto nivel pueda ser entendido por la computadora, debe pasar por un proceso para ser procesado antes de que pueda ser ejecutado por la computadora lo cual toma tiempo adicional. La ventaja es que es más entendible son más cortos y fáciles de escribir y leer. Otra ventaja es que son portables, es decir que pueden ser ejecutados en diferentes tipos de computadoras sin necesidad de modificarlos o solo modificandolos muy poco. Los de bajo nivel solo se pueden ejecutar en una sola computadora y deben ser creados de nuevo para ser ejecutados en otra.
Los lenguajes de bajo nivel se usan en situaciones muy específicas, como en microcontroladores.

3. Compiladores e intérpretes
Se usan para procesar los programas de lenguajes en alto nivel en un programa de un lenguaje en bajo nivel.
El intérprete ejecuta poco a poco el programa en alto nivel
El compilador primero traduce el programa completo en código ejecutable de bajo nivel (object code o ejecutable), luego puede ejecutarse este código en la computadora múltiples veces sin volver a compilar.
Python ocupa intérprete

4. Modos de python
Puede usarse en modo interactivo o modo script, el modo interactivo es más conveniente cuando se quieren probar fragmentos pequeños de código. El scrip es mejor cuando se tienen programas grandes y es en su mayoría codigo reutilizable o se quiere guardar.
El modo de usar python en modo interactivo es desde el prompt, se sale con `exit()`
El modo de usar el modo script es con el comando `python3 file.py` (depende de la versión instalada, se verifica con python), los archivos python tienen extensión `.py`

5. Un programa
Un programa es una serie de instrucciones específicas que indican cómo computar una acción.
Los detalles de cada lenguaje dependen de lenguaje a lenguaje pero en general todos los lenguajes tiene lo siguiente: input, output, operaciones aritméticas, condicionales y ciclos.

> Se puede pensar que programar es descomponer una tarea grande y compleja en pequeñas sub-tareas hasta que las sub-tareas sena tan pequeñas que pueden resolverse con alguna de las características básicas antes mencionadas.

6. Tipos de errores
Pueden suceder tres tipos de errores al programar: de sintaxis, de tiempo de ejecución y semánticos.
En los de sintaxis el interprete va a devolver un error y no va a ejecutar nada.
Los de tiempo de ejecución no aparecen hasta que se está ejecutando el programa y se llaman excepciones (indican que algo inusual ocurrió)
Los errores de semántica no se va a mostrar ningún error por el interprete. Ahí pasa que el programa que escribiste no es el programa que querías escribir.

7. Debugging
Puede verse como experimentos, después de que sabes qué es lo que podría estar fallando formulas una hipótesis y compruebas si es cierta.

8. Primer programa
Hacer ejemplos de `Hola mundo!` en script y en modo interactivo.





## Tarea

Experimentar con `print()` en el modo interactivo:
1. ¿Qué pasa si se escribe mal print? ¿Qué error lanza y qué significa ese error?
2. ¿Qué pasa si se pone el mensaje entre comillas simples en vez de comillas dobles?
3. ¿Qué pasa si se pone un tabulador antes de print? ¿Que significa el error que lanza?
