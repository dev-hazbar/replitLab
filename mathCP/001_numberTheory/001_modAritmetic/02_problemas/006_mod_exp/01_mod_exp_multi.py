def mod_exp_mulIt(a, b, n):
	"""Utilizando multiplicacion para calcular el modulo del exponente"""
	"""Ineficientes para exponentes grandes"""
	res = 1
	for i in range(b):
		res = (res * a) % n

	return res % n


if __name__ == "__main__":
	import sys

	cpDataRead_PATH = "../../../../../cpDataRead/cpDataGeneral/"
	sys.path.append(cpDataRead_PATH)

	from inputReader import leer_datos

	INPUT_FILE = "./input.txt"
	OUTPUT_FILE = "./output.txt"

	INPUT_DATA = leer_datos(INPUT_FILE, "entero", "data_horizontal_list")
	OUTPUT_DATA = leer_datos(OUTPUT_FILE, "entero", "data_vertical")

	import unittest

	class TestSuma(unittest.TestCase):

		def test_mod_congruence(self):
			index = 1
			EXP = True
			for [a, b, n], EXP in zip(INPUT_DATA, OUTPUT_DATA):
				with self.subTest(a=a, b=b, n=n, test=index):
					RES = mod_exp_mulIt(a, b, n)
					self.assertEqual(
						RES, EXP,
						f"\n[!] mod_exp_mulIt({a}, {b}, {n}) -> Got {RES} != {EXP} Exp")

				if RES != EXP:
					print(RES, EXP)
					break

				index += 1

	unittest.main()
