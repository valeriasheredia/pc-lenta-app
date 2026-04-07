const API_URL = "http://127.0.0.1:5000";

async function ejecutarAccion(ruta) {
  const resultado = document.getElementById("resultado");
  resultado.textContent = "Ejecutando acción...";

  try {
    const respuesta = await fetch(`${API_URL}${ruta}`, {
      method: "POST"
    });

    const data = await respuesta.json();
    resultado.textContent = data.mensaje;
  } catch (error) {
    resultado.textContent = "Hubo un error al conectar con el backend. Revisá si Flask está corriendo.";
  }
}

function mostrarMensajeDiagnostico() {
  const resultado = document.getElementById("resultado-diagnostico");
  resultado.textContent = "Si marcaste una o más opciones, seguí con los pasos de abajo para hacer una mejora básica.";
}
