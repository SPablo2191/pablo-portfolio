# Mi Portfolio 👨‍💻

## Introducción:

Bievenido al backend de mi portfolio desarrollado con Django.

## Tabla de contenidos:

- [Autor](#autor👀)
- [Tecnologias](#tecnologias-👨‍💻)
- [Entornos Compatibles](#entornos-compatibles-💻)
- [Instalación](#instalación🤖)
- [Modulos](#modulos-🚨)

## Autor👀

- [Pablo Sandoval](https://github.com/SPablo2191)

## Tecnologias 👨‍💻

![Python](https://img.shields.io/badge/Python-3.11.2-brightgreen.svg)
![Django](https://img.shields.io/badge/Django-4.2.2-green.svg)
![Django REST Framework](https://img.shields.io/badge/djangorestframework-3.14.0-success.svg)
![Postgres](https://img.shields.io/badge/PostgreSQL-15.2-blue.svg)
![Dot env](https://img.shields.io/badge/dotenv-1.0-orange.svg)

## Entornos Compatibles
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

## Instalación🤖

Para hacer uso del proyecto de manera local es necesario realizar los siguientes pasos:

1. Ingresar los siguiente comandos en consola:

```cmd
python3 -m venv [nombreDelEntornoVirtual]
```

este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```cmd
source nombreDelEntornoVirtual/bin/activate
```

NOTA: en caso de trabajar con windows el entorno virtual se genera con scripts para activar el entorno virtual por ende se tiene que acceder de la siguiente forma:

```cmd
nombreDelEntornoVirtual\Scripts\activate.bat
```

y para apagarlo (en ambos casos) es:

```cmd
deactivate
```

2. despues correr el siguiente comando para obtener los paquetes empleados en la API:

```cmd
pip install -r requirements.txt
```

3. Una vez los paquetes fueron instalados con exito, se debe realizar las migraciones:

```cmd
python manage.py migrate
```

4. Crear un superusuario para acceder al modulo admin:

```cmd
python manage.py createsuperuser
```

5. Levantar el servidor:

```cmd
python manage.py runserver
```

6. ¡Listo! ya puede visitar la pagina web en este [enlace](http://127.0.0.1:8000/).

## Modulos 🚨
- [Logros](#Logros)
- [Empresas o Instituciones](#empresas-e-instituciones)
- [Hechos](#hechos)
## Logros
| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | achievements | Registrar un nuevo logro |
| GET   | achievements | Recuperar el listado de logros |
| PUT    | achievements/<int:id> | Editar un logro por su id |
| PATCH    | achievements/<int:id> | Editar un logro por su id (parcialmente) |
| GET    | achievements/<int:id> | Recuperar un logro por su id |
| DELETE    | achievements/<int:id> | Eliminar un logro |

## Empresas e Instituciones
| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | companies | Registrar una nueva empresa |
| GET   | companies | Recuperar el listado de empresas |
| PUT    | companies/<int:id> | Editar una empresa por su id |
| PATCH    | companies/<int:id> | Editar una empresa por su id (parcialmente) |
| GET    | companies/<int:id> | Recuperar una empresa por su id |
| DELETE    | companies/<int:id> | Eliminar una empresa por su id |

## Hechos
| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | facts | Registrar un nuevo hecho |
| GET   | facts | Recuperar el listado de hechos |
| PUT    | facts/<int:id> | Editar un hecho a por su id |
| PATCH    | facts/<int:id> | Editar un hecho por su id (parcialmente) |
| GET    | facts/<int:id> | Recuperar un hecho por su id |
| DELETE    | facts/<int:id> | Eliminar un hecho por su id |

## Technologias
| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | technologies | Registrar una nueva tecnologia |
| GET   | technologies | Recuperar el listado de tecnologias |
| PUT    | technologies/<int:id> | Editar una tecnologia por su id |
| PATCH    | technologies/<int:id> | Editar una tecnologia por su id (parcialmente) |
| GET    | technologies/<int:id> | Recuperar una tecnologia por su id |
| DELETE    | technologies/<int:id> | Eliminar una tecnologia por su id |

## Proyectos
| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | projects | Registrar un nuevo proyecto |
| GET   | projects | Recuperar el listado de proyectos |
| PUT    | projects/<int:id> | Editar un proyecto  por su id |
| PATCH    | projects/<int:id> | Editar un proyecto por su id (parcialmente) |
| GET    | projects/<int:id> | Recuperar un proyecto por su id |
| DELETE    | projects/<int:id> | Eliminar un proyecto por su id |

