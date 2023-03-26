# doco

#REQUISITOS: 
tener instalado Python (link de descarga: https://www.python.org/downloads/)
tener instalado Django (comando de instalacion: pip install django)

#PASOS PARA COMPILAR LA APP

utilizar el comando "python manage.py runserver" (este comando compila la aplicacion y lo levanta en el puerto http://127.0.0.1:8000/ por defecto

#SUPERUSUARIO
La app cuenta con un SUPERUSUARIO que nos permite ingresar a la base de datos desde el directorio "http://127.0.0.1:8000/admin"

#NUEVO SUEPERUSUARIO

ejecuta el comando python manage.py createsuperuser

El comando createsuperuser te pedirá que ingreses el nombre de usuario para el superusuario, su dirección de correo electrónico y su contraseña. Ingresa la información solicitada y presiona Enter.
Si la información ingresada es correcta, se creará el superusuario y se mostrará un mensaje de confirmación en la terminal

