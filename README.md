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
