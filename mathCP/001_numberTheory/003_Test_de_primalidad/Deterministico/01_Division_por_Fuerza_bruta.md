

# **Método de División por Fuerza Bruta**

El método de División por Fuerza Bruta para comprobar si un número $ n $ es primo consiste en verificar si es divisible por cualquier número entero desde 2 hasta la raíz cuadrada de $ n $.



**Pasos del Algoritmo:**

1. Si $ n \leq 1 $, no es primo.
2. Verifica si $ n $ es divisible por 2 (excepción inicial para números pares).
3. Itera por todos los números impares desde 3 hasta $ \sqrt{n} $:
    - Si $ n $ es divisible por alguno de ellos, entonces no es primo.
4. Si no encuentra divisores, $ n $ es primo.

```
1. Si n <= 1, retornar "No primo".
2. Si n es divisible por 2, retornar "No primo".
3. Para i desde 3 hasta sqrt(n), con paso de 2:
       Si n % i == 0, retornar "No primo".
4. Retornar "Primo".

```

```python
import math

def es_primo_fuerza_bruta(n):
    if n <= 1:
        return False  # No es primo
    if n == 2:
        return True  # 2 es primo
    if n % 2 == 0:
        return False  # Números pares mayores a 2 no son primos

    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False  # Divisible, no es primo

    return True  # Es primo

# Ejemplo
numero = 29
print(f"{numero} es primo: {es_primo_fuerza_bruta(numero)}")

```



**Complejidad**

- **Tiempo:**
  $ O(\sqrt{n}) $, ya que solo probamos divisores hasta $ n $.

- **Espacio:**
  $ O(1) $, porque no usamos memoria adicional significativa.

---

**Ventajas:**
- Sencillo de entender e implementar.
- Eficiente para números pequeños.

**Desventajas:**
- Ineficiente para números grandes.
- No es adecuado para aplicaciones donde se requiera probar primalidad de números muy grandes rápidamente.
