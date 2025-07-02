// Fetch a la API de platzi para obtener todas las cadenas de la API de platzi. El swagger supongo...

const URL_API_PLATZI = 'https://api.escuelajs.co/';

const APIS_ENDPOINTS = [
    "api/v1/products", // Productos
    "api/v1/categories", // Categorías
    "api/v1/users", // Usuarios
];

const peticionAPI = async () => {
    const data = [];
    try {
        for (const api of APIS_ENDPOINTS) {
            const response = await fetch(`${URL_API_PLATZI}${api}`);
            if (!response.ok) {
                throw new Error(`Error al obtener datos de ${api}: ${response.statusText}`);
            }
            const result = await response.json();
            data.push({ endpoint: api, data: result });
        }
    } catch (error) {
        console.error(`Error en la petición a la API: ${error.message}`);
    }
    return data;
}

const mostrarAPIs = (all_data) => {
    console.log("Datos obtenidos de las APIs:");
    all_data.forEach(apiData => {
        console.log(`\nEndpoint: ${apiData.endpoint}`);
        console.log("Datos:");
        console.log(JSON.stringify(apiData.data, null, 2)); // Formatea la salida para mejor legibilidad
    });

}

const main = async () => {
    const all_data = await peticionAPI(); // Realiza la petición a las APIs
    if (all_data.length === 0) {
        console.log("No se obtuvieron datos de las APIs.");
        return;
    }
    mostrarAPIs(all_data);
}

main().catch(error => {
    console.error(`Error en la ejecución del programa: ${error.message}`);
});