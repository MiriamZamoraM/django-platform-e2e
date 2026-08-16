# 🐍 Backend Service — Django REST Framework

Servicio core de la API desarrollado en Python/Django. Proporciona los endpoints de la aplicación y la validación de salud (*healthcheck*) para la infraestructura de contenedores y Kubernetes.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.11
* **Framework:** Django 5.x + Django REST Framework
* **Database Driver:** `psycopg2-binary` (PostgreSQL)
* **WSGI Application Server:** Gunicorn 21.x
* **Healthcheck:** Custom view con verificación activa de DB

---

## ⚙️ Variables de Entorno

El servicio lee la configuración del sistema operativo mediante `os.getenv()`. Se pueden definir en un archivo `.env` o inyectar mediante el runtime de contenedores:

| Variable | Descripción | Valor por defecto |
| :--- | :--- | :--- |
| `DB_NAME` | Nombre de la base de datos | `""` (fallback a SQLite) |
| `DB_USER` | Usuario de PostgreSQL | `""` |
| `DB_PASSWORD` | Contraseña de PostgreSQL | `""` |
| `DB_HOST` | Host de la base de datos | `127.0.0.1` |
| `DB_PORT` | Puerto de conexión a DB | `5432` |
| `SECRET_KEY` | Clave secreta de Django | Local dev key |
| `DEBUG` | Modo depuración (`True`/`False`) | `False` |

---

## 🚀 Endpoints Principales

### `GET /health/`
Verifica el estado de la aplicación y la conexión activa con la base de datos.

**Respuesta exitosa (`200 OK`):**
```json
{
  "status": "healthy",
  "database": "connected"
}