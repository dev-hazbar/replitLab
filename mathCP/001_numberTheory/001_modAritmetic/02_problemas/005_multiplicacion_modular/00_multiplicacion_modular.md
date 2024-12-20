# Multiplicación modular

Exploremos la propiedad multiplicativa de la aritmética modular:
> (A * B) mod C = (A mod C * B mod C) mod C


## casos de pruebas

```python
# 1. Casos generales (valores variados de lista y módulo)
assert multiplicacion_modular([2, 3, 4], 5) == 4  # (2*3*4) % 5 = 24 % 5 = 4
assert multiplicacion_modular([1, 1, 1], 3) == 1  # (1*1*1) % 3 = 1
assert multiplicacion_modular([2, 5, 3], 7) == 6  # (2*5*3) % 7 = 30 % 7 = 6
assert multiplicacion_modular([3, 4], 6) == 0     # (3*4) % 6 = 12 % 6 = 0
assert multiplicacion_modular([6, 7, 8], 10) == 6 # (6*7*8) % 10 = 336 % 10 = 6

# 2. Casos con módulo 1 (siempre resulta 0)
assert multiplicacion_modular([7, 8, 9], 1) == 0  # (7*8*9) % 1 = 0
assert multiplicacion_modular([3, 5, 11], 1) == 0 # (3*5*11) % 1 = 0
assert multiplicacion_modular([2, 4], 1) == 0     # (2*4) % 1 = 0
assert multiplicacion_modular([15, 20, 25], 1) == 0  # (15*20*25) % 1 = 0
assert multiplicacion_modular([1, 1, 1, 1], 1) == 0  # (1*1*1*1) % 1 = 0

# 3. Casos con lista de números grandes (overflow manejado por módulo)
assert multiplicacion_modular([10**9, 10**9], 10**9 + 7) == 49 # Overflow: 10**18 % (10**9 + 7) = 49
assert multiplicacion_modular([2**30, 2**30], 2**31 - 1) == 1  # Modular producto grande
assert multiplicacion_modular([10**8, 10**8, 10**8], 97) == 16 # Rápida reducción modular
assert multiplicacion_modular([999999999, 888888888], 1234567) == 1098023
assert multiplicacion_modular([10**12, 10**15, 10**20], 17) == 1

# 4. Casos con números negativos en la lista
assert multiplicacion_modular([-3, 4, 5], 7) == 6  # ((-3)*4*5) % 7 = -60 % 7 = 6
assert multiplicacion_modular([-2, -3], 5) == 1    # ((-2)*(-3)) % 5 = 6 % 5 = 1
assert multiplicacion_modular([2, -3, -4], 11) == 3  # (2*(-3)*(-4)) % 11 = 24 % 11 = 3
assert multiplicacion_modular([-1, -1, -1], 7) == 6  # ((-1)*(-1)*(-1)) % 7 = -1 % 7 = 6
assert multiplicacion_modular([-10, 20], 13) == 4    # (-10*20) % 13 = -200 % 13 = 4

# 5. Casos con módulo primo (propiedades especiales)
assert multiplicacion_modular([5, 7, 11], 13) == 8  # Producto simple
assert multiplicacion_modular([6, 6, 6], 19) == 2   # Producto múltiple
assert multiplicacion_modular([13, 26, 39], 7) == 0 # Multiplicador múltiplo del módulo
assert multiplicacion_modular([1, 2, 3, 4, 5], 31) == 120  # Producto completo
assert multiplicacion_modular([17, 19, 23], 29) == 18  # Todos son primos menores al módulo

# 6. Casos límite (módulo grande o lista mínima)
assert multiplicacion_modular([1, 2], 10**9) == 2        # Lista con el mínimo de elementos
assert multiplicacion_modular([3, 3], 10**12) == 9       # Producto pequeño
assert multiplicacion_modular([10**6, 10**6], 10**9) == 36 # Modular simple
assert multiplicacion_modular([1, 1], 10**18) == 1       # Unidad siempre igual
assert multiplicacion_modular([123456789, 987654321], 10**9 + 9) == 259259260

# 7. Casos con elementos repetidos
assert multiplicacion_modular([2, 2, 2], 3) == 2     # (2*2*2) % 3 = 8 % 3 = 2
assert multiplicacion_modular([5, 5, 5, 5], 7) == 4  # (5^4) % 7 = 625 % 7 = 4
assert multiplicacion_modular([10, 10, 10], 13) == 12 # (10^3) % 13 = 1000 % 13 = 12
assert multiplicacion_modular([1, 1, 1, 1], 5) == 1  # Todas las entradas son 1
assert multiplicacion_modular([3, 3, 3, 3], 6) == 3  # Múltiplos repetidos

# 8. Casos con módulo pequeño en comparación con los números
assert multiplicacion_modular([10, 20, 30], 2) == 0   # Todos son pares
assert multiplicacion_modular([9, 15, 27], 3) == 0    # Todos son divisibles por 3
assert multiplicacion_modular([4, 6, 8], 5) == 2      # Producto: 192 % 5 = 2
assert multiplicacion_modular([7, 8, 9], 10) == 6     # Producto: 504 % 10 = 6
assert multiplicacion_modular([3, 7, 9], 4) == 3      # Producto: 189 % 4 = 3

# 9. Casos con módulo mayor que todos los números de la lista
assert multiplicacion_modular([2, 3, 4], 100) == 24   # Producto menor que el módulo
assert multiplicacion_modular([1, 2, 3], 50) == 6     # Producto menor que el módulo
assert multiplicacion_modular([5, 6], 50) == 30       # Producto menor que el módulo
assert multiplicacion_modular([10, 10], 150) == 100   # Producto menor que el módulo
assert multiplicacion_modular([9, 11], 200) == 99     # Producto menor que el módulo

# 10. Casos con listas largas
assert multiplicacion_modular([2]*10, 1000) == 24     # 2^10 % 1000 = 24
assert multiplicacion_modular([3]*15, 7) == 5         # 3^15 % 7 = 5
assert multiplicacion_modular([5]*20, 13) == 9        # 5^20 % 13 = 9
assert multiplicacion_modular([1]*100, 10) == 1       # Todos son 1
assert multiplicacion_modular([7]*50, 23) == 14       # Reducción modular acumulativa

# 11. Casos con combinaciones de números y módulo 0
assert multiplicacion_modular([0, 1, 2], 5) == 0      # Un elemento es 0
assert multiplicacion_modular([10, 0, 15], 7) == 0    # Producto cero por 0
assert multiplicacion_modular([5, 7, 0, 11], 13) == 0 # Producto cero por 0
assert multiplicacion_modular([0, 0, 0], 17) == 0     # Todos son 0
assert multiplicacion_modular([10, 20, 30], 0) == None # Dividir entre 0 es inválido

# 12. Casos con módulo 2 (verificando paridad)
assert multiplicacion_modular([1, 3, 5], 2) == 1      # Todos impares
assert multiplicacion_modular([2, 4, 6], 2) == 0      # Todos pares
assert multiplicacion_modular([2, 3, 4], 2) == 0      # Mezcla: resultado par
assert multiplicacion_modular([1, 2, 3], 2) == 0      # Mezcla: resultado par
assert multiplicacion_modular([7, 9, 11], 2) == 1     # Todos impares

# 13. Casos extremos y edge cases
assert multiplicacion_modular([0, 0], 10) == 0        # Producto es 0
assert multiplicacion_modular([1, 1], 1) == 0         # Módulo 1 siempre es 0
assert multiplicacion_modular([100, 200], 1) == 0     # Producto cualquier número % 1 = 0
assert multiplicacion_modular([10**9, 10**9], 10**9) == 0 # Producto múltiplo del módulo
assert multiplicacion_modular([10**9], 2) == 0        # Número par y módulo pequeño

# 14. Casos con listas mezcladas (números grandes y pequeños)
assert multiplicacion_modular([1, 10**9, 3], 5) == 3      # Mezcla de grandes y pequeños
assert multiplicacion_modular([10**6, 2, 10**3], 7) == 6  # Mezcla, reducción modular intermedia
assert multiplicacion_modular([2, 3, 10**8], 13) == 6     # Resultado pequeño tras modular
assert multiplicacion_modular([7, 10, 2], 100) == 40      # Producto más pequeño que el módulo
assert multiplicacion_modular([4, 5, 2**10], 50) == 0     # Reducción por múltiplos de módulo

# 15. Casos con números primos en la lista
assert multiplicacion_modular([2, 3, 5], 7) == 6          # Producto de primos
assert multiplicacion_modular([7, 11, 13], 19) == 5       # Modular de primos mayores
assert multiplicacion_modular([17, 19, 23], 29) == 18     # Todos primos menores al módulo
assert multiplicacion_modular([3, 5, 7, 11], 13) == 9     # Más primos en lista
assert multiplicacion_modular([31, 37], 41) == 40         # Producto de primos menores al módulo

# 16. Casos con módulo igual a un elemento en la lista
assert multiplicacion_modular([5, 6, 7], 7) == 0          # Un elemento divisible por el módulo
assert multiplicacion_modular([10, 20, 30], 10) == 0      # Un múltiplo del módulo
assert multiplicacion_modular([1, 2, 10], 10) == 0        # Último múltiplo del módulo
assert multiplicacion_modular([13, 26], 13) == 0          # Todos múltiplos del módulo
assert multiplicacion_modular([7, 14, 21], 7) == 0        # Lista compuesta por múltiplos

# 17. Casos con números cercanos al módulo
assert multiplicacion_modular([6, 6, 6], 7) == 6          # Números cercanos al módulo
assert multiplicacion_modular([9, 9, 9], 10) == 9         # Producto múltiple más cercano
assert multiplicacion_modular([4, 8], 9) == 5             # Cerca pero no múltiplo
assert multiplicacion_modular([11, 12], 13) == 2          # Reducción modular simple
assert multiplicacion_modular([98, 99], 100) == 2         # Muy cercanos al módulo

# 18. Casos con listas grandes y reducción modular acumulativa
assert multiplicacion_modular([10] * 50, 13) == 4         # (10^50) % 13 = 4
assert multiplicacion_modular([2] * 30, 7) == 2           # (2^30) % 7 = 2
assert multiplicacion_modular([3, 4, 5] * 10, 19) == 11   # Producto modular repetido
assert multiplicacion_modular([7, 8, 9] * 5, 17) == 16    # Reducción modular acumulada
assert multiplicacion_modular([10**5] * 100, 97) == 54    # Lista muy grande, con módulo

# 19. Casos con elementos negativos y módulos variados
assert multiplicacion_modular([-2, -3, 4], 5) == 4        # (-2 * -3 * 4) % 5 = 24 % 5 = 4
assert multiplicacion_modular([-5, 6, 7], 11) == 7        # (-5 * 6 * 7) % 11 = -210 % 11 = 7
assert multiplicacion_modular([-10, 20, 30], 13) == 6     # Producto negativo
assert multiplicacion_modular([-1, -1, -1], 7) == 6       # (-1)^3 % 7 = -1 % 7 = 6
assert multiplicacion_modular([-4, -4], 9) == 7           # (-4 * -4) % 9 = 16 % 9 = 7

# 20. Casos límite (listas mínimas o muy grandes)
assert multiplicacion_modular([1, 2], 10) == 2            # Lista mínima
assert multiplicacion_modular([10**9] * 100, 1000) == 0   # Lista grande
assert multiplicacion_modular([999999999] * 1000, 1000) == 0  # Muy grande

# 21. Casos con valores repetidos pero no cero
assert multiplicacion_modular([2, 2, 2], 3) == 2         # Todos iguales, módulo 3
assert multiplicacion_modular([3, 3, 3, 3], 5) == 4      # Producto de múltiplos del 3
assert multiplicacion_modular([5, 5, 5], 6) == 5         # Producto de 5 % 6
assert multiplicacion_modular([7, 7], 13) == 10          # Producto de 7 % 13
assert multiplicacion_modular([1, 1, 1], 11) == 1        # Producto
```