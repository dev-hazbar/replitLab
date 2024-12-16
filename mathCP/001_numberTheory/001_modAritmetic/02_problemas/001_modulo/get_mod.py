import math


def mod(a, b):
    if b == 0:
        return float("inf")

    return a - b * math.floor(a / b)


def modpy(a, b):
    if b == 0:
        return float("inf")
    return a % b


def elorion():
    print(f"Elorion from {__file__}")


if __name__ == "__main__":
    import sys
    cpDataRead_PATH = '../../../../../cpDataRead/cpDataGeneral/'
    sys.path.append(cpDataRead_PATH)

    from inputReader import leer_datos

    INPUT_FILE = "./input.txt"
    OUTPUT_FILE = "./output.txt"

    INPUT_DATA = leer_datos(INPUT_FILE, 'entero', 'data_horizontal_list')
    OUTPUT_DATA = leer_datos(OUTPUT_FILE, 'entero', 'data_vertical')

    import unittest

    # Clase de prueba que hereda de unittest.TestCase
    class TestSuma(unittest.TestCase):

        def test_mod(self):
            index = 1
            for [a, b], EXP in zip(INPUT_DATA, OUTPUT_DATA):
                with self.subTest(a=a, b=b, test=index):
                    RES = mod(a, b)
                    self.assertEqual(
                        RES, EXP,
                        f"\n[!] mod({a}, {b}) -> Got {RES} != {EXP} Exp")

                if RES != EXP:
                    print(RES, EXP)
                    break
                index += 1

    # Si ejecutas este script directamente, se ejecutarán las pruebas
    unittest.main()
