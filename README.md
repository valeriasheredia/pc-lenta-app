# Asistente para PC lenta

Proyecto MVP para guiar al usuario en mejoras básicas de rendimiento y ejecutar algunas acciones reales en Windows desde Python.

## Estructura

- `backend/app.py`: servidor Flask con las rutas
- `backend/actions.py`: acciones reales de Windows
- `frontend/index.html`: interfaz principal
- `frontend/style.css`: estilos
- `frontend/script.js`: conexión con el backend

## Requisitos

- Windows
- Python 3 instalado y agregado al PATH

## Instalación

### 1. Instalar dependencias

Abrí una terminal dentro de la carpeta del proyecto y ejecutá:

```bash
pip install -r requirements.txt
```

### 2. Levantar el backend

Entrá a la carpeta `backend`:

```bash
cd backend
python app.py
```

Si sale bien, vas a ver algo como esto:

```bash
Running on http://127.0.0.1:5000
```

### 3. Levantar el frontend

Abrí otra terminal y entrá a la carpeta `frontend`:

```bash
cd frontend
python -m http.server 5500
```

Después abrí en tu navegador:

```bash
http://127.0.0.1:5500
```

## Qué hace hoy

- Vacía la papelera
- Abre limpieza de disco
- Abre el Administrador de tareas
- Abre la configuración de programas de inicio

## Qué tenés que cambiar

En `frontend/index.html` reemplazá este enlace:

```html
https://wa.me/5490000000000
```

por tu número real de WhatsApp.

## Límite importante

Esto funciona en una PC donde el backend Python está instalado y corriendo. No es todavía una web pública que ejecute acciones en cualquier computadora por internet.

## Próximo paso recomendado

Cuando esto funcione, recién ahí conviene mejorar:
- textos
- diseño
- más pasos guiados
- empaquetado como app instalable
