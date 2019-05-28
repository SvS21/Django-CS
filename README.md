# Django-CS
## Comenzando 🚀
Para descargar una copia del proyecto necesitas tener instalado git en tu equipo lo puedes descargar en la siguiente liga:
https://git-scm.com/downloads

despues de haber instalado git en tu ordenador, abres una terminal de comandos
navegas hacia la direccion donde quieres que se guarde el proyecto y escribes el siguiente codigo:
```
git clone https://github.com/SvS21/Django-CS.git
```
Y listo.
### Pre-requisitos 📋
```
Python >= 3.6
Django > 2.1
Editor de código preferido
```
### Instalación 🔧
Necesitas instalar todas las librerias con el comando:
```
pip install -r requirements.txt
```
Crear base de datos en postgresql y
modificar datos de acceso a la base de datos en:
```
django-cs/csaplication/settings.py
```
Preparar las migraciones con el comando:
```
python manage.py makemigrations
```
Realizar migraciones con el comando:
```
python manage.py migrate
```
## Construido con 🛠️
Python
Django

## Contribuyendo 🖇️
Siga paso por paso para contribuir en el proyecto
Accede a la carpeta del proyecto a traves del una ventana del cmd
```
git add -A
```
Al ejecutar el comando git add -A, se añadirán al índice los ficheros borrados, los modificados y los nuevos.
```
git commit -m "tú comentario"
```
Preparar el commit para subirlo
```
git pull
```
Descargar los cambios de los demas
```
git push origin master
```
Subir cambios a este repositorio.
