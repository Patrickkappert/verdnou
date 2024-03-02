#!/bin/bash

# Directorio a limpiar
directory="./odoo/custom/src"

# Cambiamos permisos
sudo chown -R $USER:$USER ./*

# Recorre todos los elementos del directorio
for file in $(ls $directory)
do
    # Comprueba si no es el directorio 'private'
    if [ "$file" != "private" ] && [ "$file" != "addons.yaml" ] && [ "$file" != "repos.yaml" ]
    then
        # Si no es 'private', lo elimina
        rm -rf "$directory/$file"
    fi
done

docker-compose -f setup-devel.yaml run --rm odoo

# Cambiamos permisos otra vez
sudo chown -R $USER:$USER ./*

# Eliminamos direcorios .git

find $directory -name ".git" -type d -exec rm -rf {} +

echo "Step 2 Done ! "