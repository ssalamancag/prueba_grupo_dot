# Como correr el proyecto
Esta es una API REST desarrollada en python con Flask [aca](https://flask.palletsprojects.com/en/2.0.x/installation/#) se encuentra la informacion sobre los requisitos para usar Flask  
Se deben configurar las siguientes variables para la conexion a la base de datos en el archivo `app.py`

`USER_DB = 'testuser'`  
`PASS_DB = 'testpass'`  
`URL_DB = 'localhost'`  
`NAME_DB = 'development_database'`  

Alternativamente se puede usar la base de datos en el contenedor que ya esta configurado ejecutando `docker-compose up` sobre la carpeta del proyecto

Una vez se tiene la base de datos ejecutar   
`flask db init`  
`flask db migrate`  
`flask db upgrade`  

Despues de esto ya podemos agregar los registros a la tabla  `quotation` 
