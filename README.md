# 🚀 Django REST API & Infrastructure

Un entorno de desarrollo moderno y contenedorizado para aplicaciones web con Django, respaldado por PostgreSQL y automatizado con integraciones CI mediante GitHub Actions.

![Django CI Status](https://github.com/MiriamZamoraM/django-platform-e2e/actions/workflows/django-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Backend** | Python 3.11 + Django 5.2 |
| **Base de Datos** | PostgreSQL |
| **Contenedores** | Docker & Docker Compose |
| **Linter / Estilo** | Flake8 |
| **CI/CD** | GitHub Actions (`django-ci.yml`) |

---

## 📁 Estructura del Proyecto

```text
.
├── .github/
│   └── workflows/
│       └── django-ci.yml       # Pipeline de integración continua
├── backend/
│   ├── core/                  # Configuración principal de Django
│   ├── manage.py
│   ├── Dockerfile             # Imagen optimizada de Python 3.11
│   └── requirements.txt
├── .file.env.example               # Plantilla de variables de entorno
├── docker-compose.yml         # Orquestación de servicios (web + db)
└── README.md