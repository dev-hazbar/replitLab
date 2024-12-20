import math

def calculate_multi_mod (list_int, module):

	if module == 0 :
		return math.inf

	acum_multi = 1
	for num in list_int:
		reduce_mod = num % module
		acum_multi = (acum_multi * reduce_mod) % module

	return acum_multi


if __name__ == '__main__':
	import sys

	cpDataRead_PATH = "../../../../../cpDataRead/cpDataGeneral/"
	sys.path.append(cpDataRead_PATH)

	from inputReader import leer_datos

	INPUT_FILE = "./input.txt"
	OUTPUT_FILE = "./output.txt"

	INPUT_DATA = leer_datos(INPUT_FILE, "cadena", "data_matriz_list")
	OUTPUT_DATA = leer_datos(OUTPUT_FILE,'entero', 'data_vertical')


	import unittest

	class TestSuma(unittest.TestCase):

		def test_TTT(self):
			index = 1
			for  data, EXP in zip(INPUT_DATA, OUTPUT_DATA):
				list_int = list(map(eval, data[0]))
				module = data[1][0]
				module = eval(module)

				with self.subTest(list=list_int, module=module, test=index):
					RES = calculate_multi_mod(list_int, module)
					self.assertEqual(RES, EXP,
						f"\n[!] calculate_multi_mod({list_int}, {module}) -> Got {RES} != {EXP} Exp")


				if RES != EXP:
					print(RES, EXP)
					break
				index += 1

	unittest.main()