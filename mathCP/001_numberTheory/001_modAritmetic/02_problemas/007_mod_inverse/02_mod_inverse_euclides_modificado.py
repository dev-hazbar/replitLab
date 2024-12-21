

def euclides_extendido(a, c):
	r0, r1 = a, c
	s0, s1 = 1, 0
	t0, t1 = 0, 1

	while r1 != 0:
		q = r0 // r1
		r0, r1 = r1, r0 - q * r1
		s0, s1 = s1, s0 - q * s1
		t0, t1 = t1, t0 - q * t1

	# Verifica si hay inverso
	if r0 != 1:
		return float("inf")
		#raise ValueError(f"{a} no tiene inverso bajo módulo {c}")

	return s0 % c  # Asegúrate de que el resultado esté en el rango [0, C-1]


if __name__ == "__main__":
	# print(get_mod_inverse(4,3))
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
			for [a, b], EXP in zip(INPUT_DATA, OUTPUT_DATA):
				with self.subTest(a=a, b=b, test=index):
					RES = euclides_extendido(a, b)
					self.assertEqual(RES, EXP,
						f"\n[!] euclides_extendido({a}, {b}) -> Got {RES} != {EXP} Exp")


				if RES != EXP:
					print(RES, EXP)
					print(type(RES), type(EXP))
					break

				index += 1

	unittest.main()