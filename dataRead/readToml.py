import toml

# Lee el contenido del archivo TOML
with open('./data.toml', 'r') as file:
    toml_content = file.read()

# Convierte el contenido a un objeto de Python
python_obj = toml.loads(toml_content)

# Ahora `python_obj` contiene el objeto convertido
print(python_obj)


