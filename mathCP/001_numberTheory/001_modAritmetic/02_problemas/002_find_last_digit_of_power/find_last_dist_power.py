

def ultima_cifra(a, b):
    # Encontrar la última cifra de a
    a = a % 10

    # Casos especiales
    if a == 0 or b == 0:
        return 1 if b == 0 else 0

    # Ciclos de las últimas cifras
    ciclos = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    ciclo = ciclos[a]
    longitud_ciclo = len(ciclo)

    # Encontrar la posición en el ciclo
    pos = b % longitud_ciclo

    # Ajustar la posición ya que % retorna 0 para múltiplos de longitud_ciclo
    if pos == 0:
        pos = longitud_ciclo

    return ciclo[pos - 1]


if __name__ == "__main__":

    import sys
    cpDataRead_PATH = '../../../../../cpDataRead/cpDataGeneral/'
    sys.path.append(cpDataRead_PATH)

    from inputReader import leer_datos

    INPUT_FILE = "./input.txt"
    OUTPUT_FILE = "./output.txt"

    INPUT_DATA = leer_datos(INPUT_FILE,'entero', 'data_horizontal_list')
    OUTPUT_DATA = leer_datos(OUTPUT_FILE,'entero', 'data_vertical')

    import unittest

    # Clase de prueba que hereda de unittest.TestCase
    class TestSuma(unittest.TestCase):

        def test_ultima_cifra(self):
            index = 1
            for  [a, b], EXP in zip(INPUT_DATA, OUTPUT_DATA):
                with self.subTest(a=a, b=b, test=index):
                    RES = ultima_cifra(a, b)
                    self.assertEqual(RES, EXP,
                        f"\n[!] ultima_cifra({a}, {b}) -> Got {RES} != {EXP} Exp")
                index += 1

    # Si ejecutas este script directamente, se ejecutarán las pruebas
    unittest.main()