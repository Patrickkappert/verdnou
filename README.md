# README  Imagen Base Contabilidad PRO QubiQ#



### Configuración Inicial del proyecto  ###

Basada en : https://github.com/Tecnativa/docker-odoo-base/tree/scaffolding

	Configurar ./src/repos.yaml
	Configurar .src/addons.yml

##Montar el proyecto en local ##

      1. docker-compose build --pull

      2. docker-compose up


##En el caso de querer actualizar los repositorios:

	- Ejecutar el script ./second_step.sh


	Este script descargará los nuevos cambios de los repositorios
	Hacer commit de esos nuevos cambios y preparar el PR contra la rama donde queremos mergear los cambios

	###  Producción --> Arrancar el contenedor final: ###
		- ./production_up.sh

### Acceso a la instancia  ###

	El puerto, en entornos de desarrollo, se define según la versión de odoo:
		- v8: http://localhost:08069
		- v9: http://localhost:09069
		- v10: http://localhost:10069
		- v11: http://localhost:11069
		- v12: http://localhost:12069

	La opción PGDATABASE (que aparece tanto en prod.yaml como en docker-compose.yml) 
	define la base de datos que cargará el docker.

	Una vez restoreada la nueva BBDD hay que parar el docker y cambiar el valor de PGDATABASE

### Configuración de la instancia ###

Cambios y configuraciones a tener en cuenta cuando se crea una nueva instancia (GET OUT DEVELOPERS!)

	Realizar, mediante command en docker, un actualización de todos los módulos del sistema:
		command:
            - odoo
            - --update=all
