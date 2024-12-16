import re
import os

# CONSTANTS_DATA_TYPE
ENTERO = 'entero' # int
DECIMAL = 'decimal' # float
BOOLEAN = 'bool'    #
CHARACTER = 'char'  #
CADENA = 'cadena'    # string

# CONSTANTS_INPUT_TYPE
DATA_HORIZONTAL = 'data_horizontal'
DATA_VERTICAL = 'data_vertical'
DATA_HORIZONTAL_LIST = 'data_horizontal_list'
DATA_VERTICAL_LIST = 'data_vertical_list'
DATA_MATRIZ = 'data_matriz'
DATA_MATRIZ_LIST = 'data_matriz_list'

def leer_datos(archivo, tipo_dato, data_input):
    with open(archivo, 'r') as f:
        lineas = [linea.strip() for linea in f.readlines()]

        # Procesar las líneas según el tipo de dato y formato de entrada
        datos = []
        if data_input == 'data_horizontal':
            # Convertir a una lista de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [parse_int(numero) for linea in lineas for numero in linea.split()]
            elif tipo_dato == 'decimal':
                datos = [parse_float(numero) for linea in lineas for numero in linea.split()]
            elif tipo_dato == 'cadena':
                datos = []
                for linea in lineas:
                    matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                    fila = [next(group for group in match if group) for match in matches]
                    datos.extend(fila)
            elif tipo_dato == BOOLEAN:
                datos = [linea.strip().lower() == 'true' for linea in lineas for linea in linea.split()]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)

        elif data_input == 'data_vertical':
            # Convertir a una lista de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [parse_int(numero) for linea in lineas for numero in linea.split()]
            elif tipo_dato == 'decimal':
                datos = [parse_float(numero) for linea in lineas for numero in linea.split()]
            elif tipo_dato == 'cadena':
                datos = []
                for linea in lineas:
                    matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                    fila = [next(group for group in match if group) for match in matches]
                    datos.extend(fila)
            elif tipo_dato == 'boolean':
                datos = [numero.strip().lower() == 'true' for linea in lineas for numero in linea.split()]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)

        elif data_input == 'data_horizontal_list':
            # Convertir a una lista de listas de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [[parse_int(numero) for numero in linea.split()] for linea in lineas]
            elif tipo_dato == 'decimal':
                datos = [[parse_float(numero) for numero in linea.split()] for linea in lineas]
            elif tipo_dato == 'cadena':
                datos = []
                for linea in lineas:
                    matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                    fila = [next(group for group in match if group) for match in matches]
                    datos.append(fila)
            elif tipo_dato == BOOLEAN:
                datos = [[numero.strip().lower() == 'true' for numero in linea.split()] for linea in lineas]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)


        elif data_input == 'data_vertical_list':
            # Convertir a una lista de listas de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [[parse_int(numero) for numero in linea.split()] for linea in '\n'.join(lineas).split('\n\n') if linea.strip()]
            elif tipo_dato == 'decimal':
                datos = [[parse_float(numero) for numero in linea.split()] for linea in '\n'.join(lineas).split('\n\n') if linea.strip()]
            elif tipo_dato == 'cadena':
                datos = []
                for bloque in '\n\n'.join(lineas).split('\n\n'):
                    bloque_datos = []
                    for linea in bloque.split('\n'):
                        matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                        fila = [group for match in matches for group in match if group]
                        bloque_datos.extend(fila)
                    datos.append(bloque_datos)
                datos = agrupar_lista(datos)
            elif tipo_dato == BOOLEAN:
                datos = [[numero.strip().lower() == 'true' for numero in linea.split()] for linea in '\n'.join(lineas).split('\n\n') if linea.strip()]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)





        elif data_input == 'data_matriz':
            # Convertir a una lista de listas de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [[parse_int(numero) for numero in linea.split()] for linea in lineas]
            elif tipo_dato == 'decimal':
                datos = [[parse_float(numero) for numero in linea.split()] for linea in lineas]
            elif tipo_dato == 'cadena':
                datos = []
                for linea in lineas:
                    matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                    fila = [next(group for group in match if group) for match in matches]
                    datos.append(fila)
            elif tipo_dato == BOOLEAN:
                datos = [[numero.strip().lower() == 'true' for numero in linea.split()] for linea in lineas]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)

        elif data_input == 'data_matriz_list':
            # Convertir a una lista de listas de listas de datos según el tipo especificado
            if tipo_dato == 'entero':
                datos = [[[parse_int(numero) for numero in linea.split()] for linea in bloque.split('\n') if linea.strip()] for bloque in '\n\n'.join(lineas).split('\n\n')]
            elif tipo_dato == 'decimal':
                datos = [[[parse_float(numero) for numero in linea.split()] for linea in bloque.split('\n') if linea.strip()] for bloque in '\n\n'.join(lineas).split('\n\n')]
            elif tipo_dato == 'cadena':
                datos = []
                for bloque in '\n\n'.join(lineas).split('\n\n'):
                    bloque_datos = []
                    for linea in bloque.split('\n'):
                        matches = re.findall(r'\'(.*?)\'|"(.*?)"|(\S+)', linea)
                        fila = [next(group for group in match if group) for match in matches]
                        bloque_datos.append(fila)
                    datos.append(bloque_datos)
            elif tipo_dato == BOOLEAN:
                datos = [[[numero.strip().lower() == 'true' for numero in linea.split()] for linea in bloque.split('\n') if linea.strip()] for bloque in '\n\n'.join(lineas).split('\n\n')]
            else:
                raise ValueError("Tipo de dato no soportado: ", tipo_dato)

            if len(datos):
                datos = agrupar_lista(datos)


        else:
            raise ValueError("Formato de entrada no soportado: ", data_input)



    return datos



def agrupar_lista(lista):
    #lista = flatten(lista)
    flattenList = []
    for element in lista:
        flattenList.append(flatten(element))

    sublistas = []
    sublista_actual = []

    for elemento in flattenList:
        if len(elemento):
            sublista_actual.append(elemento)
        else:
            sublistas.append(sublista_actual)
            sublista_actual = []

    if len(sublista_actual):
        sublistas.append(sublista_actual)

    return sublistas

def flatten(nested_list):
    flat_list = []
    stack = [nested_list]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])  # Agregar los elementos en orden inverso para mantener el orden original
        else:
            flat_list.append(current)

    return flat_list
    #TODO : - REVISAR SI EL CODIGO INFERIOR FUNCIONA
    if not nested_list or nested_list == [[]]:
        return []

    flat_list = []
    stack = [nested_list]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in current:
                if isinstance(item, list):
                    flat_list.extend(item)
                else:
                    flat_list.append(item)
        else:
            flat_list.append(current)

    return flat_list

def parse_int(value):
    if value.lower() == 'nan':
        return float('nan')
    elif value.lower() == 'inf':
        return float('inf')
    elif value.lower() == '-inf':
        return float('-inf')
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Valor no convertible a entero: {value}")

def parse_float(value):
    if value.lower() == 'nan':
        return float('nan')
    elif value.lower() == 'inf':
        return float('inf')
    elif value.lower() == '-inf':
        return float('-inf')
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Valor no convertible a decimal: {value}")

def get_Test_Object(list, path, input_type):
    outList = []
    fileName = ''

    for name in list:
        tipo = name.split('_')[0]

        if tipo in (ENTERO, DECIMAL, CADENA, BOOLEAN):
            fileName = path + name + '.txt'
        else:
            print('[!] tipo no soportado en: ' + name)
            continue

        if os.path.exists(fileName):
            obj = {
                "file_name":fileName,
                "data_type":tipo,
                "input_type":input_type
            }
            outList.append(obj)
        else:
            print(f"\t[!] El archivo {fileName} no existe.")

    return outList

def DoTest(listFileTest):
    for file in listFileTest:
        datos = leer_datos(file['file_name'], file['data_type'], file['input_type'])
        print('\t', datos)

def elorion():
    print("Elorion, Beto!!! from cpDataRead.cpDataGeneral.inputReader.py")

if __name__ == "__main__":

    # TEST
    h_simple_files = ['entero', 'decimal', 'bool', 'cadena', 'cadena_comilla']
    h_path = './h_simple/'
    v_simple_files = ['entero', 'decimal', 'bool', 'cadena', 'cadena_comilla']
    v_path = './v_simple/'
    h_list_files = ['entero', 'decimal', 'bool', 'cadena', 'cadena_comilla']
    h_list_path = './h_list/'
    v_list_files = ['entero', 'decimal', 'bool', 'cadena']
    v_list_path = './v_list/'
    matriz = ['entero', 'decimal', 'bool', 'cadena']
    matriz_path = './matriz/'
    matriz_list = ['entero', 'decimal', 'bool', 'cadena']
    matriz_list_path = './matriz_list/'
    
    print('\n[*] DATA_HORIZONTAL_TEST ')
    h_test_object = get_Test_Object(h_simple_files, h_path, DATA_HORIZONTAL)
    DoTest(h_test_object)
    
    print('\n[*] DATA_VERTICAL_TEST ')
    v_test_object = get_Test_Object(v_simple_files, v_path, DATA_VERTICAL)
    DoTest(v_test_object)
    
    print('\n[*] DATA_HORIZONTAL_LIST_TEST ')
    h_list_test_object = get_Test_Object(h_list_files, h_list_path, DATA_HORIZONTAL_LIST)
    DoTest(h_list_test_object)
    
    print(f'\n[*] DATA_VERTICAL_LIST_TEST ')
    v_list_test_object = get_Test_Object(v_list_files, v_list_path, DATA_VERTICAL_LIST)
    DoTest(v_list_test_object)
    
    print(f'\n[*] DATA_MATRIZ_TEST ')
    matriz_test_object = get_Test_Object(matriz, matriz_path, DATA_MATRIZ)
    DoTest(matriz_test_object) 
    
    print(f'\n[*] DATA_MATRIZ_LIST_TEST ')
    matriz_list_test_object = get_Test_Object(matriz_list, matriz_list_path, DATA_MATRIZ_LIST)
    DoTest(matriz_list_test_object)
    