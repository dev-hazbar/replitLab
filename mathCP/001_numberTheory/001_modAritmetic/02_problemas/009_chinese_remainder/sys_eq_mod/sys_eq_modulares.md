Genera una lista de casos de prueba para un test unitario en formato de texto. Enfócate en casos críticos para el problema, detallando tipos de entrada y valores esperados.


Sistemas de ecuaciones lineales modulares:

Descripción: Dado un conjunto de ecuaciones lineales modulares, encuentra un valor de x que satisface todas las ecuaciones.
Entrada: Una lista de tuplas (a_i, b_i, n_i) representando las ecuaciones a_i x ≡ b_i mod n_i.
Salida: Un entero x que satisface todas las ecuaciones, o indica que no hay solución.
Ejemplo: Entrada: [(2, 3, 5), (3, 4, 7)], Salida: 17.

FORMATO DE RESPUESTA:
Agragale un comentario en el encabezado cada caso de prueba, por cada caso de prueba debe haber 3 tests
entregame la salida en un textbox,
(la entrada y valor esperado esten en una linea por caso)
Inputs: [(2, 3, 5), (3, 4, 7)] -> expected: 17




# Caso de prueba 1: Solución única simple
Inputs: [(2, 3, 5), (3, 4, 7)] -> expected: 17
Inputs: [(2, 1, 3), (3, 2, 5)] -> expected: 11
Inputs: [(1, 1, 2), (1, 0, 3)] -> expected: 3

# Caso de prueba 2: Sin solución
Inputs: [(2, 3, 5), (2, 2, 5)] -> expected: No solution
Inputs: [(4, 1, 6), (2, 1, 4)] -> expected: No solution
Inputs: [(3, 1, 9), (3, 2, 9)] -> expected: No solution

# Caso de prueba 3: Solución única con números grandes
Inputs: [(4, 7, 9), (5, 3, 11)] -> expected: 70
Inputs: [(3, 5, 7), (4, 6, 9)] -> expected: 41
Inputs: [(6, 5, 13), (5, 4, 19)] -> expected: 138

# Caso de prueba 4: Sistema redundante con múltiples ecuaciones
Inputs: [(2, 3, 5), (2, 3, 10)] -> expected: 3
Inputs: [(3, 4, 6), (3, 4, 12)] -> expected: 10
Inputs: [(5, 1, 10), (5, 1, 20)] -> expected: 1

# Caso de prueba 5: Solución negativa permitida
Inputs: [(2, 1, 3), (3, 2, 5)] -> expected: -1
Inputs: [(2, -1, 3), (3, -2, 5)] -> expected: -1
Inputs: [(2, 2, 3), (3, 3, 4)] -> expected: -2

# Caso de prueba 6: Sin solución, módulos no coprimos
Inputs: [(2, 4, 6), (3, 5, 9)] -> expected: No solution
Inputs: [(6, 4, 8), (4, 2, 10)] -> expected: No solution
Inputs: [(5, 3, 7), (7, 4, 9)] -> expected: No solution

# Caso de prueba 7: Sistema con módulo primo
Inputs: [(1, 0, 7), (1, 1, 11)] -> expected: No solution
Inputs: [(1, 1, 5), (1, 2, 7)] -> expected: 12
Inputs: [(1, 1, 3), (1, 2, 5)] -> expected: 7

# Caso de prueba 8: Solución en el rango positivo
Inputs: [(1, 2, 4), (2, 3, 5)] -> expected: 8
Inputs: [(1, 3, 7), (2, 1, 9)] -> expected: 22
Inputs: [(2, 1, 5), (3, 2, 7)] -> expected: 8

# Caso de prueba 9: Solución en el rango muy grande
Inputs: [(7, 1, 13), (11, 3, 17)] -> expected: 157
Inputs: [(5, 2, 11), (6, 4, 13)] -> expected: 89
Inputs: [(4, 1, 15), (7, 2, 19)] -> expected: 106
