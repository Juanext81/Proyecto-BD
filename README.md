# Proyecto BD — Reserva de Hotel

Aplicación web educativa que demuestra la conexión entre Python y MySQL a través de Flask. Permite ejecutar consultas SQL sobre una base de datos de reservas de hotel y visualizar los resultados directamente en el navegador.

---

## Tecnologías utilizadas

| Tecnología | Versión |
|---|---|
| Python | 3.14 (local) / 3.11.9 (desarrollo original) |
| Flask | 3.1.3 |
| mysql-connector-python | 26.7.0 |
| MySQL | 8.x (local) |
| Werkzeug | 3.1.9 |
| Jinja2 | 3.1.6 |

---

## Estructura del proyecto

```
Proyecto BD/
├── app.py                        # Aplicación Flask principal
├── mi_tabla.HTML                 # Interfaz web (formulario de consulta SQL)
├── templates/
│   └── mi_tabla.HTML             # Versión de plantilla (referencia / prototipo PHP)
├── Conexion sql y py.ipynb       # Jupyter Notebook — exploración y prototipado
├── .venv/                        # Entorno virtual de Python
└── README.md
```

---

## Base de datos

- **Motor**: MySQL (servidor local)
- **Base de datos**: `reserva_de_hotel`
- **Tabla principal**: `arrivals` (columnas: `id`, `name`, `value`)
- **Usuario**: `root` (sin contraseña — solo para desarrollo local)

La base de datos debe existir previamente en el servidor MySQL. El proyecto no incluye un script de creación del esquema.

---

## Requisitos previos

- Python 3.11 o superior
- MySQL Server instalado y en ejecución en `localhost`
- La base de datos `reserva_de_hotel` creada con la tabla `arrivals`
- `pip` o acceso al entorno virtual `.venv`

---

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd "Proyecto BD"
```

### 2. Activar el entorno virtual

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Instalar dependencias

Las dependencias ya están instaladas en `.venv`. Si necesitas reinstalarlas:

```bash
pip install flask mysql-connector-python
```

### 4. Configurar la base de datos

Asegúrate de que MySQL esté corriendo y crea la base de datos si no existe:

```sql
CREATE DATABASE reserva_de_hotel;
USE reserva_de_hotel;

CREATE TABLE arrivals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    value FLOAT
);
```

Las credenciales de conexión están definidas en `app.py`:

```python
host="localhost"
database="reserva_de_hotel"
user="root"
password=""
```

Modifica estos valores si tu configuración de MySQL es diferente.

---

## Cómo ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

> **Nota**: El servidor de desarrollo de Flask no debe usarse en producción.

---

## Uso de la interfaz web

1. Abre el navegador en `http://127.0.0.1:5000`
2. Escribe una consulta SQL en el campo de texto (por ejemplo: `SELECT * FROM arrivals`)
3. Haz clic en **Ejecutar Consulta**
4. Los resultados se muestran en formato JSON debajo del formulario

---

## Jupyter Notebook

El archivo `Conexion sql y py.ipynb` documenta el proceso de exploración y prototipado del proyecto. Contiene cuatro celdas que muestran distintas aproximaciones a la conexión Python–MySQL:

1. Conexión con `flask_mysqldb`
2. Conexión con `flask_sqlalchemy` + `pymysql` y modelo `MyTable` para la tabla `arrivals`
3. Versión mejorada con ruta raíz `/`
4. Depuración del error de `debug=True` dentro de Jupyter

Para ejecutar el notebook:

```bash
jupyter notebook "Conexion sql y py.ipynb"
```

> **Aviso**: Ejecutar celdas con `app.run(debug=True)` dentro de Jupyter genera un `SystemExit` conocido por el comportamiento del reloader de Werkzeug. Usa `debug=False` en el contexto del notebook.

---

## Notas importantes

- Este proyecto es de carácter **educativo**. Aceptar consultas SQL arbitrarias desde el navegador sin validación representa un riesgo de seguridad (inyección SQL) y **no debe usarse en producción**.
- Las credenciales de base de datos (`root` sin contraseña) son adecuadas solo para entornos de desarrollo local.
- El archivo `templates/mi_tabla.HTML` contiene código PHP de un prototipo anterior y no es utilizado por Flask.
