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

def leer_data_withFormatter(fileName, formatter):
	"""
		list_int:0, list_str:1, list_float:2, list_bool:3,list_str:4>{int:0, float:2}, int:5, float:6, bool:7, str:8
	"""
	try:
		listas = []
		lista_actual = []

		with open(fileName, 'r') as archivo:
			for linea in archivo:
				linea = linea.strip()  # Elimina espacios en blanco al inicio y al final

				if linea == "":  # Si la línea está vacía (es una línea en blanco)
					if lista_actual:  # Si la lista actual tiene elementos
						listas.append(lista_actual)  # Agregar la lista actual a la lista principal
						lista_actual = []  # Reiniciar la lista actual para los próximos elementos
				else:
					# Agregar la línea a la lista actual
					lista_actual.append(linea)

			# Si la última lista no se ha agregado (en caso de que no haya una línea en blanco al final)
			if lista_actual:
				listas.append(lista_actual)

		return convertir_lista(listas, formatter)

	except Exception as e:
		print(f"{e}")
		print(f"[!] ERROR el archivo no existe: {fileName}")
		exit()


def convertir_lista(listDatos, formatter):

	# Dividir la cadena de conversiones por comas
	conversiones = formatter.replace(" ", "")
	patron = r'(list_str:\d+>{[^}]*})|([^,]+)'
	conversiones = [x[0] if x[0] else x[1] for x in re.findall(patron, conversiones)]

	for datos in listDatos:
		# Iterar sobre las conversiones
		for conversion in conversiones:
			# Si encontramos una conversión compleja como list_str:4>{int:0, float:2}
			if ">" in conversion:
				tipo_y_subconversion = conversion.split(">")
				tipo_conversion = tipo_y_subconversion[0]
				subconversiones = tipo_y_subconversion[1]

				# Si no es una conversión compleja, procesamos como antes
				tipo, indice = tipo_conversion.split(":")
				indice = int(indice)  # Convertir el índice a entero

				tempData = datos[indice]
				tempData = DataParser(tempData, tipo)
				#datos[indice] = tempData

				cadena = subconversiones
				cadena_sin_llaves = cadena.strip("{}")
				elementos = cadena_sin_llaves.split(",")

				for item in elementos:
					t, i = item.split(":")
					i = int(i)  # Convertir el índice a entero
					tempData[i] = DataParser(tempData[i], t)

				datos[indice] = tempData
			else:
				# Si no es una conversión compleja, procesamos como antes
				tipo, indice = conversion.split(":")
				indice = int(indice)  # Convertir el índice a entero

				tempData = datos[indice]
				tempData = DataParser(tempData, tipo)
				datos[indice] = tempData

	return listDatos


def DataParser(dataStr, convertTo):

	try:
		if convertTo == "list_int":
			# Convertir a lista de enteros
			return list(map(int, dataStr.split()))
		elif convertTo == "list_str":
			# Convertir a lista de cadenas
			return dataStr.split()
		elif convertTo == "list_float":
			# Convertir a lista de flotantes
			return list(map(float, dataStr.split()))
		elif convertTo == "list_bool":
			# Convertir a lista de booleanos
			return [item.lower() == 'true' for item in dataStr.split()]
		elif convertTo == "int":
			# Convertir a entero
			return int(dataStr)
		elif convertTo == "float":
			# Convertir a entero
			return float(dataStr)
		elif convertTo == "bool":
			# Convertir a booleano
			return dataStr.lower() == 'true'
		elif convertTo == "str":
			# Convertir a cadena
			return dataStr

		return dataStr

	except Exception as e:
		print(f"{e}")
		print(f"[!] ERROR en DataParser convert: {dataStr} to-> {convertTo}")
		exit()



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


	#TEST: LEER_DATA _WITH_FORMATTER
	print(f'\n[*] LEER_DATA _WITH_FORMATTER ')
	input_data = "./multiData/multiData.txt"
	formatter = "list_int:0, list_str:1, list_float:2, list_bool:3,list_str:4>{int:0, float:2}, int:5, float:6, bool:7, str:8"
	# formatter = "list_int:0, list_str:1, list_float:2, list_bool:3,list_str:4, int:5, float:6, bool:7, str:8"

	data = leer_data_withFormatter(input_data, formatter)
	print(data)


	input_data = "./multiData/matrizData.txt"
	formatter = "list_int:0, list_str:1, list_float:2, list_str:3>{int:0, float:2}, list_bool:4"
	data = leer_data_withFormatter(input_data, formatter)
	print(data)
