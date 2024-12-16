import csv

# Ruta al archivo CSV
csv_file = 'data2.csv'

# Abrir y leer el archivo CSV
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    # Iterar sobre las filas del archivo CSV
    for row in csv_reader:
        print(row)  # Cada 'row' es una lista que contiene los valores de la fila



print("\n")
'''
    Usando csv.DictReader
    ****************************
'''
# Ruta al archivo CSV
csv_file = 'data2.csv'

# Abrir y leer el archivo CSV
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    # Iterar sobre las filas del archivo CSV
    for row in csv_reader:
        print(row)  # Cada 'row' es un diccionario


print("\n")

'''
    Usando Pandas
    ****************************
'''

import pandas as pd

# Leer el archivo CSV usando pandas
df = pd.read_csv(csv_file)

# Mostrar el DataFrame
print(df)