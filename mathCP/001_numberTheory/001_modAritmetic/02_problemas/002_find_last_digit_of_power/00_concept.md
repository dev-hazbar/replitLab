# encontrar ultima cifra de la potencia


Para resolver el problema de encontrar la última cifra de a^b dado dos números enteros a y b, puedes seguir estos pasos:

1. **Encontrar el patrón cíclico de las últimas cifras**: Las potencias de un número tienen un patrón cíclico en sus últimas cifras. Por ejemplo, consideremos el número a=2:

    2^1 = 2 → última cifra es 2
    2^2 = 4 → última cifra es 4
    2^3 = 8 → última cifra es 8
    2^4 = 16 → última cifra es 6
    2^5 = 32 → última cifra es 2 `(y el ciclo se repite)`

   Así, las últimas cifras de las potencias de 2 forman el ciclo 2, 4, 8, 6.

2. **Reducir el exponente b usando el ciclo**: Para encontrar la última cifra de a^b, necesitamos saber la posición de b dentro del ciclo. Esto se puede hacer usando el módulo con la longitud del ciclo.

3. **Aplicar el ciclo para obtener la última cifra**: Utiliza el valor reducido del exponente para determinar la última cifra.

Ejemplo paso a paso:
Supongamos que queremos encontrar la última cifra de 3^10:

1. Determinar el patrón cíclico de las últimas cifras de 3:

    3^1 = 3 → última cifra es 3
    3^2 = 9 → última cifra es 9
    3^3 = 27 → última cifra es 7
    3^4 = 81 → última cifra es 1
    3^5 = 243 → última cifra es 3 (el ciclo se repite)

   El ciclo es 3, 9, 7, 1.

2. Reducir el exponente b usando el ciclo: El ciclo tiene una longitud de 4. Entonces, calculamos 10 mod 4:

    10 mod 4 = 2

    Esto significa que la última cifra de 3^10 es la misma que la última cifra de 3^2.

3. Aplicar el ciclo: De nuestro ciclo, sabemos que 3^2 = 9 y la última cifra es 9.

Entonces, la última cifra de 3^10 es 9.

Generalización del método:
1. Encuentra el ciclo de las últimas cifras de las potencias de a.
2. Calcula b mod (longitud del ciclo).
3. Usa el resultado para encontrar la última cifra de a^b.





**Generalización del método:**

- Encuentra el `ciclo de las últimas cifras` de las potencias de a.
- Calcula b mod (longitud del ciclo).
- Usa el resultado para encontrar la última cifra de  a^b

Si deseas un algoritmo más formal, podrías implementarlo en un lenguaje de programación, como Python:

```python
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

# Ejemplo de uso
print(ultima_cifra(3, 10))  # Output: 9
```
Este código encontrará la última cifra de a^b de manera eficiente, utilizando los patrones cíclicos de las últimas cifras.