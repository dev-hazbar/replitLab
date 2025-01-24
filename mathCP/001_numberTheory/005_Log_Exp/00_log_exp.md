# Exponenciación Logarítmica




El objetivo del problema es implementar una función que calcule $ x^n $ (es decir, $ x^n $). Una solución directa sería multiplicar $ x $ por sí mismo $ n $ veces, lo que tendría una complejidad temporal de $ O(n) $. Sin embargo, este enfoque no es eficiente para valores grandes de $ n $.

Para mejorar la eficiencia, el artículo propone utilizar la exponenciación rápida o exponenciación por cuadrados, que reduce la complejidad temporal a $ O(\log n) $. Este método se basa en las siguientes propiedades matemáticas:

> Si $ n $ es par, entonces
> $
> x^n = (x^2)^{n/2}.
> $
> Si $ n $ es impar, entonces
> $x^n = x \times x^{n-1}.$

Utilizando estas propiedades, se puede diseñar un algoritmo que divide el problema en subproblemas más pequeños, reduciendo $ n $ a la mitad en cada paso, lo que resulta en una solución más eficiente.

> El artículo también aborda cómo manejar exponentes negativos invirtiendo la base $ x $ y convirtiendo $ n $ en positivo, ya que
> $x^{-n} = \frac{1}{x^n}.$

Para una comprensión más profunda y una implementación detallada, puedes consultar el artículo completo en Dev.to:



## Ejercicio

LeetCode Problem 50: Pow(x, n) - Logarithmic Exponentiation (Medium)

Implement pow(x, n), which calculates x raised to the power n (i.e., $x^n$).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000

Constraints:
- $ -100.0 < x < 100.0 $
- $ -2^{31} \leq n \leq 2^{31} - 1 $
- $ n $ is an integer.
- $ x^n $ is guaranteed to be a valid 32-bit integer result.
