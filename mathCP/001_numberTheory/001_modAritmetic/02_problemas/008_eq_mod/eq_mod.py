import sys
sys.path.append("../007_mod_inverse/")
from mod_inverse_euclides_modificado import euclides_extendido
from mod_inverse import gcd

def solve_eq_mod(numA, numB, module):

	if numA == 0:
		return float("inf")


	tempGCD = gcd(numA, module)
	if tempGCD != 1:
		if  numB%tempGCD == 0:
			print([numA, numB, module], f"Tiene {tempGCD} soluciones")
			# reducir
			numA = numA//tempGCD
			numB = numB//tempGCD
			module = module//tempGCD
		else:
			return float("inf")



	inverse = euclides_extendido(numA, module)

	if inverse == float("inf"):
		return inverse

	return (inverse * numB)%module



if __name__ == '__main__':

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
			for [a, b, m], EXP in zip(INPUT_DATA, OUTPUT_DATA):
				with self.subTest(a=a, b=b, mod=m, test=index):
					RES = solve_eq_mod(a, b, m)
					self.assertEqual(RES, EXP,
						f"\n[!] solve_eq_mod({a}, {b}, {m}) -> Got {RES} != {EXP} Exp")

				if RES != EXP:
					print(RES, EXP)
					print(type(RES), type(EXP))
					break

				index += 1

	unittest.main()