

# Suma y Reseta modular

Exploremos la propiedad de la suma de la aritmética modular:
> Suma Modular
> (A + B) mod C = (A mod C + B mod C) mod C

> Resta Modular
>(A - B) mod C = (A mod C - B mod C) mod C


## Ejercicio de Suma Modular
Un ejercicio típico de aritmética modular de sumas y restas puede ser planteado de la siguiente manera:

Enunciado del ejercicio:
Dado un conjunto de operaciones de suma y resta en un módulo específico, calcular el resultado final y devolverlo en el rango [0, módulo-1].

Entradas:
Lista de operaciones: Una lista de números enteros y operadores (ejemplo: ["+5", "-3", "+7", "-2"]).
Módulo: Un número entero positivo que define el módulo (ejemplo: 10).
Salidas:
Resultado modular: El resultado final de las operaciones aplicadas módulo el número especificado.
Ejemplo:
Entrada:
Lista de operaciones: ["+5", "-3", "+7", "-2"]
Módulo: 10
Proceso:
Suma/resta de los números:
0 + 5 = 5
5 - 3 = 2
2 + 7 = 9
9 - 2 = 7
Aplicación del módulo:
7 mod 10 = 7 (en este caso no cambia porque está dentro del rango).
Salida:
Resultado modular: 7


## Tests por Casos

```python
# 1. Caso base (sumas y restas simples dentro del rango del módulo)
assert calcular_modular(["+3", "+4", "-2"], 10) == 5  # 3 + 4 - 2 = 5
assert calcular_modular(["+8", "-5", "+3"], 10) == 6  # 8 - 5 + 3 = 6
assert calcular_modular(["+0", "+0", "-0"], 10) == 0  # Todo es cero
assert calcular_modular(["+9", "+0", "-4"], 10) == 5  # 9 + 0 - 4 = 5
assert calcular_modular(["+2", "-3", "+8"], 10) == 7  # 2 - 3 + 8 = 7

# 2. Caso con resultados negativos (verificar reducción al rango del módulo)
assert calcular_modular(["-3", "-7"], 10) == 0  # -3 - 7 = -10, -10 mod 10 = 0
assert calcular_modular(["-8", "-5"], 10) == 7  # -8 - 5 = -13, -13 mod 10 = 7
assert calcular_modular(["-1", "-10", "+4"], 10) == 3  # -1 - 10 + 4 = -7, -7 mod 10 = 3
assert calcular_modular(["+0", "-15", "+5"], 7) == 4  # 0 - 15 + 5 = -10, -10 mod 7 = 4
assert calcular_modular(["-25"], 6) == 5  # -25 mod 6 = 5

# 3. Caso con grandes números (verificar reducción correcta)
assert calcular_modular(["+1000", "-999"], 10) == 1  # 1000 - 999 = 1, 1 mod 10 = 1
assert calcular_modular(["+12345", "-6789"], 100) == 56  # 12345 - 6789 = 5556, 5556 mod 100 = 56
assert calcular_modular(["-500", "+250", "+250"], 30) == 0  # -500 + 250 + 250 = 0, 0 mod 30 = 0
assert calcular_modular(["+100", "+200", "+300"], 50) == 0  # 100 + 200 + 300 = 600, 600 mod 50 = 0
assert calcular_modular(["+1000000", "-999999"], 2) == 1  # 1000000 - 999999 = 1, 1 mod 2 = 1

# 4. Caso con módulo pequeño (verificar operaciones repetitivas)
assert calcular_modular(["+3", "+3", "+3"], 2) == 1  # 3 + 3 + 3 = 9, 9 mod 2 = 1
assert calcular_modular(["+1", "+2", "+3"], 1) == 0  # Todo % 1 es 0
assert calcular_modular(["+5", "-5"], 3) == 0  # 5 - 5 = 0, 0 mod 3 = 0
assert calcular_modular(["+4", "+4", "+4"], 4) == 0  # 4 + 4 + 4 = 12, 12 mod 4 = 0
assert calcular_modular(["+5", "+5", "-1"], 2) == 1  # 5 + 5 - 1 = 9, 9 mod 2 = 1

# 5. Caso de operaciones sin números (lista vacía o sin valores válidos)
assert calcular_modular([], 10) == 0  # Lista vacía, resultado inicial es 0
assert calcular_modular(["+0"], 10) == 0  # Solo un 0
assert calcular_modular([], 1) == 0  # Lista vacía con módulo 1
assert calcular_modular(["+0", "-0"], 5) == 0  # Todos son 0
assert calcular_modular([], 100) == 0  # Lista vacía con módulo grande

# 6. Caso con módulo igual a 1 (todo resultado será 0)
assert calcular_modular(["+100"], 1) == 0  # 100 mod 1 = 0
assert calcular_modular(["-50"], 1) == 0  # -50 mod 1 = 0
assert calcular_modular(["+999", "-888"], 1) == 0  # (999 - 888) mod 1 = 0
assert calcular_modular(["+0", "-0"], 1) == 0  # Todo es 0 mod 1
assert calcular_modular(["+5", "-10", "+20"], 1) == 0  # (5 - 10 + 20) mod 1 = 0

# 7. Caso con módulo grande (verificar eficiencia y correcta reducción)
assert calcular_modular(["+1000000000"], 1000000007) == 1000000000  # Número menor que el módulo
assert calcular_modular(["+1000000009"], 1000000007) == 2  # 1000000009 mod 1000000007 = 2
assert calcular_modular(["-1000000010"], 1000000007) == 4  # -1000000010 mod 1000000007 = 4
assert calcular_modular(["+999999999", "-999999998"], 1000000007) == 1  # (999999999 - 999999998) mod 1000000007 = 1
assert calcular_modular(["+500", "+500", "+500"], 1000) == 500  # 1500 mod 1000 = 500

# 8. Caso con operaciones alternadas y varios signos (orden y acumulación)
assert calcular_modular(["+5", "-3", "+7", "-4"], 10) == 5  # 5 - 3 + 7 - 4 = 5
assert calcular_modular(["+6", "-1", "+2", "-8", "+3"], 7) == 2  # 6 - 1 + 2 - 8 + 3 = 2 (mod 7)
assert calcular_modular(["-9", "+4", "+10", "-6"], 11) == 9  # -9 + 4 + 10 - 6 = -1 mod 11 = 10
assert calcular_modular(["+8", "+5", "-13", "+6", "-6"], 9) == 0  # 8 + 5 - 13 + 6 - 6 = 0 mod 9
assert calcular_modular(["-100", "+50", "+70"], 30) == 20  # -100 + 50 + 70 = 20 mod 30 = 20

# 9. Caso de combinación de operaciones vacías y módulo mínimo inválido (control de errores)
# Lista vacía y módulo 10
assert calcular_modular([], 10) == 0  # Lista vacía, resultado 0

# Lista vacía con módulo pequeño
assert calcular_modular([], 2) == 0  # Lista vacía, resultado 0

# Lista vacía con módulo muy grande
assert calcular_modular([], 1000000) == 0  # Resultado 0 para lista vacía

# Módulo inválido (como 0 o negativo, agregar control en la función)
try:
    calcular_modular(["+5"], 0)  # Debería lanzar un error o devolver algo controlado
except ValueError:
    print("Módulo inválido manejado correctamente")

# Módulo negativo
try:
    calcular_modular(["+5"], -10)  # Debería lanzar un error
except ValueError:
    print("Módulo negativo manejado correctamente")

# 10. Caso con números y resultados extremos (grandes positivos y negativos)
assert calcular_modular(["+999999999"], 100) == 99  # 999999999 mod 100 = 99
assert calcular_modular(["-999999999"], 100) == 1  # -999999999 mod 100 = 1
assert calcular_modular(["+1000000", "-999999"], 1000) == 1  # (1000000 - 999999) mod 1000 = 1
assert calcular_modular(["-1000000", "+999999"], 1000) == 999  # (-1000000 + 999999) mod 1000 = 999
assert calcular_modular(["+123456789", "-987654321"], 100000) == 23468  # Resultado grande reducido correctamente

# 11. Caso con lista de operaciones que incluye valores redundantes (0 o repetitivos)
assert calcular_modular(["+0", "-0", "+0"], 10) == 0  # Todos son cero
assert calcular_modular(["+5", "-5", "+0"], 10) == 0  # 5 - 5 + 0 = 0 mod 10
assert calcular_modular(["+10", "-10", "+10", "-10"], 7) == 0  # Todo se anula
assert calcular_modular(["+6", "-6", "+6", "-6"], 6) == 0  # Todo se anula exactamente al módulo
assert calcular_modular(["+0", "+0", "+0", "+0"], 1) == 0  # Siempre es 0 mod 1

# 12. Caso con lista de operaciones muy larga (prueba de rendimiento y acumulación correcta)
assert calcular_modular(["+1"] * 1000, 10) == 0  # (1000 * 1) mod 10 = 0
assert calcular_modular(["-1"] * 500, 15) == 5  # (-500) mod 15 = 5
assert calcular_modular(["+5", "-5"] * 100, 7) == 0  # Todo se anula
assert calcular_modular(["+2"] * 10000, 1000) == 0  # (10000 * 2) mod 1000 = 0
assert calcular_modular(["+1", "-2", "+3", "-4"] * 250, 12) == 10  # Suma acumulativa mod 12

# 13. Caso con módulo igual al resultado exacto
assert calcular_modular(["+10", "-5", "+5"], 10) == 0  # 10 - 5 + 5 = 10, 10 mod 10 = 0
assert calcular_modular(["+12", "-6", "+6"], 12) == 0  # 12 - 6 + 6 = 12, 12 mod 12 = 0
assert calcular_modular(["+50", "-25", "-25"], 25) == 0  # 50 - 25 - 25 = 0, 0 mod 25 = 0
assert calcular_modular(["+20", "-10", "+30", "-40"], 10) == 0  # 20 - 10 + 30 - 40 = 0
assert calcular_modular(["+100", "-50", "-50"], 100) == 0  # Todo se anula al módulo

# 14. Caso con combinaciones de operaciones que superan múltiples veces el módulo
assert calcular_modular(["+100", "+200", "+300"], 50) == 0  # 600 mod 50 = 0
assert calcular_modular(["-100", "-200", "-300"], 60) == 0  # -600 mod 60 = 0
assert calcular_modular(["+1000", "-1000", "+1000", "-1000"], 7) == 0  # Todo se anula al módulo

# 15. Caso con combinación de operaciones complejas y resultados que exceden el rango del módulo
assert calcular_modular(["+100000", "-50000", "+25000", "-12500"], 1000) == 250  # (100000 - 50000 + 25000 - 12500) mod 1000 = 250
assert calcular_modular(["+987654", "-123456", "+654321"], 99999) == 77779  # (987654 - 123456 + 654321) mod 99999 = 77779
assert calcular_modular(["+123456", "-654321", "+987654"], 10000) == 3210  # (123456 - 654321 + 987654) mod 10000 = 3210
assert calcular_modular(["+100000000", "-99999999", "+50000000"], 1000000) == 100000  # (100000000 - 99999999 + 50000000) mod 1000000 = 100000
assert calcular_modular(["+99999999", "-9999999", "+88888888"], 5000000) == 3888888  # (99999999 - 9999999 + 88888888) mod 5000000 = 3888888


```

```python

# 1. Caso base (sumas y restas simples dentro del rango del módulo)
assert calcular_modular(["+3", "+4", "-2"], 10) == 5  # 3 + 4 - 2 = 5
assert calcular_modular(["+8", "-5", "+3"], 10) == 6  # 8 - 5 + 3 = 6
assert calcular_modular(["+0", "+0", "-0"], 10) == 0  # Todo es cero
assert calcular_modular(["+9", "+0", "-4"], 10) == 5  # 9 + 0 - 4 = 5
assert calcular_modular(["+2", "-3", "+8"], 10) == 7  # 2 - 3 + 8 = 7

# 1. Caso básico con sumas positivas y un módulo mayor
assert calcular_modular(["+5", "+10"], 20) == 15  # (5 + 10) mod 20 = 15
assert calcular_modular(["+7", "+8"], 10) == 5  # (7 + 8) mod 10 = 5
assert calcular_modular(["+2", "+3"], 5) == 0  # (2 + 3) mod 5 = 0
assert calcular_modular(["+0", "+0"], 1) == 0  # Suma de ceros
assert calcular_modular(["+50", "+70"], 100) == 20  # (50 + 70) mod 100 = 20

# 2. Caso con restas negativas y un módulo mayor
assert calcular_modular(["-5", "-10"], 20) == 5  # (-5 - 10) mod 20 = 5
assert calcular_modular(["-7", "-8"], 10) == 5  # (-7 - 8) mod 10 = 5
assert calcular_modular(["-2", "-3"], 5) == 0  # (-2 - 3) mod 5 = 0
assert calcular_modular(["-50", "-70"], 100) == 80  # (-50 - 70) mod 100 = 80
assert calcular_modular(["-0", "-0"], 1) == 0  # Resta de ceros

# 3. Caso mixto con sumas y restas, módulo positivo
assert calcular_modular(["+10", "-5"], 15) == 5  # (10 - 5) mod 15 = 5
assert calcular_modular(["+7", "-8"], 10) == 9  # (7 - 8) mod 10 = 9
assert calcular_modular(["+3", "-3"], 5) == 0  # (3 - 3) mod 5 = 0
assert calcular_modular(["+50", "-30"], 100) == 20  # (50 - 30) mod 100 = 20
assert calcular_modular(["+0", "-0"], 1) == 0  # Resultado sigue siendo 0

# 4. Caso con números mayores al módulo (reducción correcta)
assert calcular_modular(["+25", "-10"], 10) == 5  # (25 - 10) mod 10 = 5
assert calcular_modular(["+37", "-15"], 20) == 2  # (37 - 15) mod 20 = 2
assert calcular_modular(["+100", "-50"], 30) == 20  # (100 - 50) mod 30 = 20
assert calcular_modular(["+55", "-35"], 15) == 5  # (55 - 35) mod 15 = 5
assert calcular_modular(["+200", "-100"], 50) == 0  # (200 - 100) mod 50 = 0

# 5. Caso con módulo negativo o cero (control de errores)
try:
    calcular_modular(["+5"], -10)  # Módulo negativo, debería lanzar un error
except ValueError:
    print("Módulo negativo manejado correctamente")
try:
    calcular_modular(["+5"], 0)  # Módulo cero, debería lanzar un error
except ValueError:
    print("Módulo cero manejado correctamente")
try:
    calcular_modular([], 0)  # Lista vacía con módulo inválido
except ValueError:
    print("Lista vacía y módulo inválido manejados correctamente")
assert calcular_modular(["+5", "-5"], 10) == 0  # Resultado correcto con módulo positivo
assert calcular_modular(["+10", "-10"], 1) == 0  # Todo es 0 mod 1

# 6. Caso con módulo igual a 1 (todo resultado será 0)
assert calcular_modular(["+100"], 1) == 0  # 100 mod 1 = 0
assert calcular_modular(["-50"], 1) == 0  # -50 mod 1 = 0
assert calcular_modular(["+999", "-888"], 1) == 0  # (999 - 888) mod 1 = 0
assert calcular_modular(["+0", "-0"], 1) == 0  # Todo es 0 mod 1
assert calcular_modular(["+5", "-10", "+20"], 1) == 0  # (5 - 10 + 20) mod 1 = 0

# 7. Caso con módulo grande (verificar eficiencia y correcta reducción)
assert calcular_modular(["+1000000000"], 1000000007) == 1000000000  # Número menor que el módulo
assert calcular_modular(["+1000000009"], 1000000007) == 2  # 1000000009 mod 1000000007 = 2
assert calcular_modular(["-1000000010"], 1000000007) == 4  # -1000000010 mod 1000000007 = 4
assert calcular_modular(["+999999999", "-999999998"], 1000000007) == 1  # (999999999 - 999999998) mod 1000000007 = 1
assert calcular_modular(["+500", "+500", "+500"], 1000) == 500  # 1500 mod 1000 = 500

# 8. Caso con operaciones alternadas y varios signos (orden y acumulación)
assert calcular_modular(["+5", "-3", "+7", "-4"], 10) == 5  # 5 - 3 + 7 - 4 = 5
assert calcular_modular(["+6", "-1", "+2", "-8", "+3"], 7) == 2  # 6 - 1 + 2 - 8 + 3 = 2 (mod 7)
assert calcular_modular(["-9", "+4", "+10", "-6"], 11) == 9  # -9 + 4 + 10 - 6 = -1 mod 11 = 10
assert calcular_modular(["+8", "+5", "-13", "+6", "-6"], 9) == 0  # 8 + 5 - 13 + 6 - 6 = 0 mod 9
assert calcular_modular(["-100", "+50", "+70"], 30) == 20  # -100 + 50 + 70 = 20 mod 30 = 20

# 9. Caso de combinación de operaciones vacías y módulo mínimo inválido (control de errores)
assert calcular_modular([], 10) == 0  # Lista vacía, resultado 0
assert calcular_modular([], 2) == 0  # Lista vacía, resultado 0
assert calcular_modular([], 1000000) == 0  # Resultado 0 para lista vacía
try:
    calcular_modular(["+5"], 0)  # Debería lanzar un error o devolver algo controlado
except ValueError:
    print("Módulo inválido manejado correctamente")
try:
    calcular_modular(["+5"], -10)  # Debería lanzar un error
except ValueError:
    print("Módulo negativo manejado correctamente")

# 10. Caso con números y resultados extremos (grandes positivos y negativos)
assert calcular_modular(["+999999999"], 100) == 99  # 999999999 mod 100 = 99
assert calcular_modular(["-999999999"], 100) == 1  # -999999999 mod 100 = 1
assert calcular_modular(["+1000000", "-999999"], 1000) == 1  # (1000000 - 999999) mod 1000 = 1
assert calcular_modular(["-1000000", "+999999"], 1000) == 999  # (-1000000 + 999999) mod 1000 = 999
assert calcular_modular(["+123456789", "-987654321"], 100000) == 23468  # Resultado grande reducido correctamente

# 11. Caso con lista de operaciones que incluye valores redundantes (0 o repetitivos)
assert calcular_modular(["+0", "-0", "+0"], 10) == 0  # Todos son cero
assert calcular_modular(["+5", "-5", "+0"], 10) == 0  # 5 - 5 + 0 = 0 mod 10
assert calcular_modular(["+10", "-10", "+10", "-10"], 7) == 0  # Todo se anula
assert calcular_modular(["+6", "-6", "+6", "-6"], 6) == 0  # Todo se anula exactamente al módulo
assert calcular_modular(["+0", "+0", "+0", "+0"], 1) == 0  # Siempre es 0 mod 1

# 12. Caso con lista de operaciones muy larga (prueba de rendimiento y acumulación correcta)
assert calcular_modular(["+1"] * 1000, 10) == 0  # (1000 * 1) mod 10 = 0
assert calcular_modular(["-1"] * 500, 15) == 5  # (-500) mod 15 = 5
assert calcular_modular(["+5", "-5"] * 100, 7) == 0  # Todo se anula
assert calcular_modular(["+2"] * 10000, 1000) == 0  # (10000 * 2) mod 1000 = 0
assert calcular_modular(["+1", "-2", "+3", "-4"] * 250, 12) == 10  # Suma acumulativa mod 12

# 13. Caso con módulo igual al resultado exacto
assert calcular_modular(["+10", "-5", "+5"], 10) == 0  # 10 - 5 + 5 = 10, 10 mod 10 = 0
assert calcular_modular(["+12", "-6", "+6"], 12) == 0  # 12 - 6 + 6 = 12, 12 mod 12 = 0
assert calcular_modular(["+50", "-25", "-25"], 25) == 0  # 50 - 25 - 25 = 0, 0 mod 25 = 0
assert calcular_modular(["+20", "-10", "+30", "-40"], 10) == 0  # 20 - 10 + 30 - 40 = 0
assert calcular_modular(["+100", "-50", "-50"], 100) == 0  # Todo se anula al módulo

# 14. Caso con combinaciones de operaciones que superan múltiples veces el módulo
assert calcular_modular(["+100", "+200", "+300"], 50) == 0  # 600 mod 50 = 0
assert calcular_modular(["-100", "-200", "-300"], 60) == 0  # -600 mod 60 = 0
assert calcular_modular(["+1000", "-1000", "+1000", "-1000"], 7) == 0  # Todo se anula
assert calcular_modular(["+999999999", "-999999999"], 100) == 0  # 0 mod 100 = 0
assert calcular_modular(["+500", "-500", "+500", "-500"], 250) == 0  # Todo se anula al módulo

# 15. Caso con listas que incluyen solo un valor (mínimos elementos posibles)
assert calcular_modular(["+5"], 10) == 5  # 5 mod 10 = 5
assert calcular_modular(["-5"], 10) == 5  # -5 mod 10 = 5
assert calcular_modular(["+100"], 7) == 2  # 100 mod 7 = 2
assert calcular_modular(["-100"], 7) == 5  # -100 mod 7 = 5
assert calcular_modular(["+0"], 100) == 0  # 0 mod 100 = 0
```