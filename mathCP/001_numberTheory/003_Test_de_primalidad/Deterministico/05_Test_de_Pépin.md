

# El test de primalidad de Pépin



El test de primalidad de Pépin es un algoritmo especializado para determinar si un número primo de Fermat es realmente primo. Los números de Fermat tienen la forma:
$F_n = 2^{2^n} + 1$

El test establece que un número de Fermat F_n es primo si y solo si:
$3^{(F_n - 1)/2} ≡ -1\  (mod\  F_n)$

Pasos del Test de Pépin:
1. Calcular F_n:
   $F_n = 2^{2^n} + 1$

2. Realizar el cálculo modular: Elevar 3 a la potencia (F_n - 1)/2, utilizando exponentiación modular para manejar la magnitud del cálculo.

3. Verificar la congruencia: Si el resultado es -1 mod F_n, entonces F_n es primo. Si no, F_n es compuesto.

Implementación en Python:
Aquí tienes una implementación básica del test de Pépin:

```python
def pepin_test(n):
    """
    Test de Pépin para verificar si el número de Fermat F_n es primo.
    """
    # Calcular F_n = 2^(2^n) + 1
    F_n = 2**(2**n) + 1
    
    # Calcular la potencia modular: 3^((F_n - 1) / 2) % F_n
    exp = (F_n - 1) // 2
    result = pow(3, exp, F_n)
    
    # Verificar la congruencia
    return result == F_n - 1  # -1 es equivalente a F_n - 1 en módulo F_n

# Ejemplo de uso
n = 4  # Cambiar por el índice deseado
print(f"F_{n} es primo: {pepin_test(n)}")

```

**Notas:**

- Este test es extremadamente costoso computacionalmente para valores grandes de n, ya que el tamaño de F_n crece exponencialmente. 
- Para n > 4, se suelen usar técnicas especializadas o supercomputadoras para realizar los cálculos.
