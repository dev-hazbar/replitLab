import math

def calcular_suma_modular(listInt, module):
	if module == 0 :
		return math.inf

	modAcum = 0
	for item in listInt:
		modAcum = (modAcum + item) % module
	return modAcum





if __name__ == '__main__':
	print(calcular_suma_modular([3, 4, -2], 10) == 5)

	import sys

	cpDataRead_PATH = "../../../../../cpDataRead/cpDataGeneral/"
	sys.path.append(cpDataRead_PATH)

	from inputReader import leer_datos

	INPUT_FILE = "./input.txt"
	OUTPUT_FILE = "./output.txt"

	INPUT_DATA = leer_datos(INPUT_FILE, "entero", "data_matriz_list")
	OUTPUT_DATA = leer_datos(OUTPUT_FILE,'entero', 'data_vertical')

	
	import unittest

	class TestSuma(unittest.TestCase):

		def test_calcular_suma_modular(self):
			index = 1
			for  [list, module], EXP in zip(INPUT_DATA, OUTPUT_DATA):
				with self.subTest(list=list, module=module, test=index):
					RES = calcular_suma_modular(list, module[0])
					self.assertEqual(RES, EXP,
						f"\n[!] calcular_suma_modular({list}, {module}) -> Got {RES} != {EXP} Exp")


				if RES != EXP:
					print(RES, EXP)
					break
				index += 1

	unittest.main()
