def get_mod_inverse(a, m):

    if gcd(a, m) == 1:
        """Calcular el inverso modular de a modulo m"""
        for i in range(m):
            if (a * i) % m == 1:
                return i

    return  float('inf')



def gcd(a, b):
    """ Devuelve el MCD de a y b utilizando el Algoritmo de Euclides. """
    while b != 0:
        a, b = b, a % b
    return a


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
                    RES = get_mod_inverse(a, b)
                    self.assertEqual(RES, EXP,
                        f"\n[!] get_mod_inverse({a}, {b}) -> Got {RES} != {EXP} Exp")


                if RES != EXP:
                    print(RES, EXP)
                    print(type(RES), type(EXP))
                    break

                index += 1

    unittest.main()