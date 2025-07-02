# resumen del ejercicio práctico.
# Solo tenemos que importar los módulos claves de `fs` y de `path` para poder leer el `json` y poder resolver las funciones que nos piden.
# En este caso, tenemos una función para leer `leerArchivoJson` que devuelve una promsa con el contenido del archivo. Nosotros lo recuperamos con un `await`.
# En la función de `calcularNotaMedia`, le enviamos los alumnos que leimos con `leerArchivoJson` y calculamos la nota media de todos los alumnos con un `reduce`.
# En la función de `imprimirResultados`, le enviamos los alumnos y la nota media, y lo que hacemos es imprimir por consola el nombre de cada alumno y su nota, y al final imprimimos la nota media.

**nota**: Pon tu nombre en el `package.json` en la propiedad `author`.
**MotivBot**: Puedes utilizarlo para realizar modificaciones en el código y pedirle explicaciones sobre el mismoo.