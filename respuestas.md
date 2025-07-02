10 preguntas – 0.5 punto cada una
 (Marca solo una respuesta)
¿Qué método del objeto Array devuelve un nuevo array con los elementos que cumplen una condición dada?

 a) forEach 
    #[] no devuelve un nuevo array, sino que ejecuta una función para cada elemento del array original.
 b) map
    #[] no modifica el array original, sino que devuelve uno nuevo sin filtrar.
 c) filter
    #[X] filtra los elementos según una condición.
 d) reduce
    #[] reduce aplica una función acumulativa a los elementos del array, pero no filtra. Al final, devuelve un único valor. 


El evento del DOM que se dispara cuando el árbol HTML ha sido completamente construido, sin esperar a que se carguen hojas de estilo ni imágenes, es:

 a) load
    #[] El evento load se dispara cuando todos los recursos de la página han sido cargados, incluyendo imágenes y hojas de estilo.
 b) DOMContentLoaded
    #[X] Este evento se dispara cuando el documento HTML ha sido completamente cargado y analizado, sin esperar a que se carguen otros recursos.
 c) beforeunload
    #[] Este evento se dispara cuando el usuario intenta abandonar la página, pero no está relacionado con la carga del DOM.
 d) readystatechange
    #[] Este evento se dispara cuando el estado de carga del documento cambia, pero no es específico para el DOM completo.


¿Cuál de las siguientes sentencias sobre const en JavaScript es verdadera?

 a) Impide modificar las propiedades internas de un objeto.
    #[] const no impide modificar las propiedades internas de un objeto, solo evita la reasignación de la variable.
 b) Declara una referencia que no puede reasignarse.
    #[X] const declara una variable cuyo valor no puede ser reasignado, pero las propiedades de un objeto pueden modificarse.
 c) Obliga a inicializar la variable con un valor numérico.
    #[] const no requiere que el valor sea numérico, puede ser cualquier tipo de dato.
 c) Obliga a inicializar la variable más tarde con let.
    #[] const no requiere que se inicialice más tarde con let, simplemente no permite la reasignación de la variable.
 d) Equivale a usar Object.freeze.
    #[] Object.freeze es un método que impide la modificación de un objeto, pero no está relacionado con const.


¿Qué módulo nativo de Node.js permite leer y escribir en el sistema de archivos?

 a) http
    #[] El módulo http se utiliza para crear servidores web y manejar solicitudes HTTP, no para interactuar con el sistema de archivos.
 b) fs
    #[X] El módulo fs (File System) permite interactuar con el sistema de archivos, incluyendo la lectura y escritura de archivos.
 c) net
    #[] El módulo net se utiliza para crear servidores y clientes TCP, no para interactuar con el sistema de archivos.
 d) stream
    #[] El módulo stream se utiliza para manejar flujos de datos, pero no es específico para la lectura y escritura de archivos.

¿Cuál de las siguientes promesas se completa cuando el primer parámetro de su ejecutor llama a resolve?

 a) La promesa se rechaza.
    #[] La promesa se rechaza cuando se llama a reject, no a resolve.
 b) La promesa entra en estado fulfilled.
    #[X] Cuando se llama a resolve, la promesa entra en estado fulfilled (cumplida).
 c) La promesa permanece pendiente.
    #[] La promesa no permanece pendiente si se llama a resolve, sino que cambia su estado a fulfilled.
 d) La promesa se repite en bucle infinito.
    #[] Las promesas no entran en un bucle infinito, simplemente cambian de estado al ser resueltas o rechazadas.


Para detener la propagación de un evento en la fase burbuja se usa:

 a) event.preventDefault()
    #[] event.preventDefault() se utiliza para prevenir la acción por defecto del evento, pero no detiene la propagación.
 b) event.stopPropagation()
    #[X] event.stopPropagation() detiene la propagación del evento hacia arriba en el DOM, evitando que se dispare en los elementos padres.
 c) event.stopImmediatePropagation()
    #[] event.stopImmediatePropagation() detiene la propagación del evento y también evita que otros manejadores de eventos en el mismo elemento se ejecuten, pero no es necesario para detener la burbuja.
 d) return false
    #[] return false puede detener la propagación en algunos casos, pero no es una práctica recomendada y no funciona en todos los navegadores.


¿Qué característica define a los Web Components?

 a) Se compilan a WebAssembly.
    #[] Los Web Components no se compilan a WebAssembly, son una tecnología basada en HTML, CSS y JavaScript.
 b) Encapsulan marcado, estilo y lógica en Shadow DOM.
    #[X] Los Web Components encapsulan su marcado (HTML), estilo (CSS) y lógica (JavaScript) en un Shadow DOM, lo que permite crear componentes reutilizables y aislados.
 c) Sólo funcionan dentro de frameworks como React.
    #[] Los Web Components son independientes de frameworks y pueden usarse en cualquier aplicación web, aunque también pueden integrarse en frameworks como React.
 d) Requieren Babel obligatoriamente.
    #[] Babel no es obligatorio para usar Web Components, aunque puede ser útil para compatibilidad con navegadores más antiguos.

El fichero package.json en un proyecto Node contiene, entre otros, el campo:

 a) <!DOCTYPE html>
    #[] <!DOCTYPE html> es una declaración que define el tipo de documento HTML, no es parte del package.json.
 b) "dependencies"
    #[X] "dependencies" es un campo del package.json que lista las dependencias del proyecto, pero no es el único campo importante.
 c) <script src="...">
    #[] <script src="..."> es una etiqueta HTML que se utiliza para incluir scripts en una página web, no es parte del package.json.
 d) "manifest_version"
    #[] "manifest_version" es un campo utilizado en archivos de manifiesto de extensiones de navegador, no es parte del package.json.


¿Cuál de las siguientes APIs Web permite acceder al almacenamiento clave–valor del navegador con persistencia entre sesiones?
 
 a) sessionStorage
    #[] sessionStorage es un almacenamiento temporal que se borra al cerrar la pestaña o el navegador, no persiste entre sesiones.
 b) localStorage
    #[X] localStorage es un almacenamiento clave-valor que persiste entre sesiones, permitiendo almacenar datos que no se eliminan al cerrar el navegador.
 c) indexedDB.open()
    #[] indexedDB es una API para bases de datos más complejas, pero no es un almacenamiento clave-valor simple como localStorage.
 d) CacheStorage.match()
    #[] CacheStorage es una API para manejar cachés de recursos, no es un almacenamiento clave-valor persistente entre sesiones.


¿Qué patrón de programación se utiliza al encolar funciones para su ejecución tan pronto como el sub-proceso de E/S de Node indica que hay datos listos?

 a) Observador (Observer)
    #[] El patrón Observador se utiliza para notificar a los suscriptores sobre cambios en el estado de un objeto, no para encolar funciones.
 b) Productor-consumidor
    #[] El patrón Productor-consumidor se utiliza para encolar tareas y procesarlas cuando el sistema está listo, como en el caso de Node.js con su modelo de E/S asíncrono. Casi pero no es correcto.
 c) Event Loop (bucle de eventos)
    #[X] El Event Loop es el mecanismo que permite la ejecución asíncrona en JavaScript, pero no es un patrón de programación en sí mismo. Es el ciclo que maneja la ejecución de funciones encoladas cuando hay datos disponibles.
 d) Singleton
    #[] El patrón Singleton asegura que una clase tenga una única instancia, no está relacionado con la encolación de funciones en Node.js.