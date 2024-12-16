import os
import configparser


file_name = 'data.ini'

if os.path.exists(file_name):
    # Crear un objeto configparser
    config = configparser.ConfigParser()
    # Leer el archivo datos.ini
    config.read(file_name)

else:
    print("El archivo dataIni.ini no existe.")
    exit(0)

# Crear un diccionario para almacenar los datos
data = {}

# Iterar sobre todas las secciones y opciones en el archivo .ini
'''for section in config.sections():
    section_data = {}
    for key, value in config.items(section):
        section_data[key] = value
    data[section] = section_data'''

data = {section: dict(config.items(section)) for section in config.sections()}

# Imprimir el objeto convertido
print(data)
