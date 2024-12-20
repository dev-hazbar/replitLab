def mod_exp(a, b, c):

	if a == 0 and b == 0:
		return float("INF")

	if b == 0:
		return 1

	b_bin = list(bin(b)[2:])

	exp = 1
	base = a
	res = 1

	while len(b_bin):
		bin_value = int(b_bin.pop())
		if bin_value:
			value = (base**exp) % c
			res = (res * value) % c

		exp = 2 * exp

	return res


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
					RES = mod_exp(a, b, n)
					self.assertEqual(
						RES, EXP,
						f"\n[!] mod_exp_mulIt({a}, {b}, {n}) -> Got {RES} != {EXP} Exp")

				if RES != EXP:
					print(f"ERROR TEST: GOT {RES} != {EXP} EXP")
					break

				index += 1

	unittest.main()
