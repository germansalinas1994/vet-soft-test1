# Vetsoft

Aplicación web para veterinarias utilizada en la cursada 2024 de Ingeniería y Calidad de Software. UTN-FRLP

## Dependencias

-   python 3
-   Django
-   sqlite
-   playwright
-   ruff

## Instalar dependencias

`pip install -r requirements.txt`

## Iniciar la Base de Datos

`python manage.py migrate`

## Iniciar app

`python manage.py runserver`

Integrantes:
-Germán Salinas
-Francisco Montirón
-Valentina Díaz
-Bruno Lopez Velazco
-Bravo Diego Federico

## se van a tener que generar variables de entorno en el archivo .env

## Docker Version
La imagen Docker actual es `vetsoft-app:v1.1`.


## Para generar la imagen de docker realizar

` docker build -t vetsoft-app:v1.1 .  `


## Para construir y ejecutar el contendedor de la imagen de la aplicacion realizar
## Se utilizan variables de entorno por eso hay que especificarlas con -e
## En el archivo env-example estan las variables de entorno que se ejecutan, cambiarlas por las de la configuracion del proyecto

` docker run -d -e SECRET_KEY="django-insecure-p)^5i@33c#q)%j(g5d+**-yo%)6l*vge=^_ig" -e DB_ENGINE=django.db.backends.sqlite3 -e DB_NAME=db.sqlite3 -e DEBUG=True --name vetsoft-container -p 4000:8000 vetsoft-app:v1.1 `

## Para correr la aplicacion ` http://localhost:4000 `

## Para detener el contenedor

` docker stop vetsoft-container `

## Para correr el contenedor

` docker start vetsoft-container `


## c. Versionado
## Agrega etiquetas a tu Dockerfile y a las imágenes Docker para un seguimiento adecuado:

` git tag -a v1.1 -m "Version 1.1" `
` git push origin v1.1 `


## hice una prueba para ver si anda en jenkins y hasta ahora anduvo prueba pull request con fede y credenciales armo otroooooo
