// Resolución del ejercicio de la parte 2
// declaración de variables necesarias
// File: ejercicios_practicos/parte_2/clasificar.js
import fs from 'fs/promises'; // se importa el módulo fs para manejar archivos
import path from 'path'; // se importa el módulo path para manejar rutas de archivos

const __dirname = path.resolve(); // se obtiene el directorio actual
const archivoJson = path.join(__dirname, 'alumnos.json');


// función para leer el archivo JSON
const leerArchivoJson = async (archivoJson) => {
    try{
        const data = await fs.readFile(archivoJson, 'utf8'); // se lee el archivo JSON
        return JSON.parse(data); // se convierte el contenido a un array de objetos
    }catch (error) {
        throw error; // se lanza un error si ocurre algún problema al leer el archivo
    }
};

// función reduce para procesar la nota media

const calcularNotaMedia = (alumnos) => {
    if (alumnos.length === 0) {
        return 0; // si no hay alumnos, la nota media es 0
    }
    if (!Array.isArray(alumnos)) {
        throw new Error('El parámetro debe ser un array'); // se lanza un error
    }
  return alumnos.reduce((acumulador, alumno) => {
    return acumulador + alumno.nota;
  }, 0) / alumnos.length;
}


// función para poder filtrar alumnos igual a la nota media o superior a la nota media
const filtrarAlumnos = (alumnos, notaMedia) => {
    if (!Array.isArray(alumnos)) {
        throw new Error('El parámetro debe ser un array'); // se lanza un error si no es un array
    }
    if (typeof notaMedia !== 'number') {
        throw new Error('La nota media debe ser un número'); // se lanza un error si la nota media no es un número
    }
    if (alumnos.length === 0) {
        return []; // si no hay alumnos, se retorna un array vacío
    }
    return alumnos.filter(alumno => alumno.nota >= notaMedia);
}

// función que imprime los resultados
const imprimirResultados = (alumnos, notaMedia) => {
  console.log(`Nota media: ${notaMedia.toFixed(2)}`);
  console.log('Alumnos aprobados:');
  alumnos.forEach(alumno => {
    console.log(`${alumno.nombre}: ${alumno.nota}`);
  });
};

// lectura del archivo JSON y conversión a un array de objetos
// se utiliza una promesa para manejar la lectura asíncrona del archivo
const alumnos = await leerArchivoJson(archivoJson);


const notaMedia = calcularNotaMedia(alumnos);
const alumnosAprobados = filtrarAlumnos(alumnos, notaMedia);
imprimirResultados(alumnosAprobados, notaMedia);