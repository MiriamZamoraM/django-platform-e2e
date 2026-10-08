# Imagen base ligera de Python
FROM python:3.11-slim

# Evita archivos .pyc y habilita salida directa de logs en terminal
ENV PYTHONDONTWRITEBYTECODE=1 \ 
# PYTHONDONTWRITEBYTECODE=1 evita que Python genere archivos .pyc
    PYTHONUNBUFFERED=1
# PYTHONUNBUFFERED=1 asegura que la salida de Python se muestre en tiempo real en la terminal

WORKDIR /app

# Dependencias del sistema para compilar librerías como psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt-get/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . /app/

EXPOSE 8000

# Arrancar el servidor con Gunicorn apuntando al WSGI de tu módulo 'core'
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]