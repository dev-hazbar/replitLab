import re

def leer_data_withFormatter(fileName, formatter):
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

		return data

	except Exception as e:
		print(f"{e}")
		print(f"[!] ERROR en DataParser convert: {dataStr} to-> {convertTo}")
		exit()


if __name__ == "__main__":
	input_data = "./multiData/multiData.txt"
	formatter = "list_int:0, list_str:1, list_float:2, list_bool:3,list_str:4>{int:0, float:2}, int:5, float:6, bool:7, str:8"
	# formatter = "list_int:0, list_str:1, list_float:2, list_bool:3,list_str:4, int:5, float:6, bool:7, str:8"

	data = leer_data_withFormatter(input_data, formatter)
	print(data)

	print("Elorion, Beto!!!")


	input_data = "./multiData/matrizData.txt"
	formatter = "list_int:0, list_str:1, list_float:2, list_str:3>{int:0, float:2}, list_bool:4"
	data = leer_data_withFormatter(input_data, formatter)
	print(data)



