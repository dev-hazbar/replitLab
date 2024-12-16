import json

# Lee el contenido del archivo JSON
with open('data.json', 'r') as file:
    json_content = file.read()

# Convierte el contenido a un objeto de Python
python_obj = json.loads(json_content)

# Ahora `python_obj` contiene el objeto convertido
print(type(json_content))
print(python_obj)