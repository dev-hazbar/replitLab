# Teorema de Lucas

El Teorema de Lucas es una herramienta en teoría de números combinatoria que proporciona una forma eficiente de *calcular coeficientes binomiales módulo un número primo $ p $.* Este teorema es especialmente útil cuando $ n $ y $ k $ son grandes, ya que evita cálculos directos que podrían ser computacionalmente costosos.

Enunciado del Teorema de Lucas

> Sea $ p $ un número primo, y sean $ n $ y $ k $ números enteros no negativos.
>
>
>
> **Representemos $ n $ y $ k $ en base $ p $:**
>
> $n = n_r p^r + n_{r-1} p^{r-1} + \cdots + n_1 p + n_0,$
> $k = k_r p^r + k_{r-1} p^{r-1} + \cdots + k_1 p + k_0,$
>
>
>
> donde $ 0 \leq n_i, k_i < p $. Entonces:
>
> $\binom{n}{k} \mod p = \prod_{i=0}^{r} \binom{n_i}{k_i} \mod p,$
>
>
>
> donde $ \binom{n_i}{k_i} = 0 $ si $ n_i < k_i $.


## Pasos para usar el Teorema de Lucas

Los pasos para usar el Teorema de Lucas y calcular $ \binom{n}{k} \mod p $ son los siguientes:

1. **Descomponer $ n $ y $ k $ en base $ p $:**
   Representa $ n $ y $ k $ como sumas de potencias de $ p $, es decir:
   $
   n = n_r p^r + n_{r-1} p^{r-1} + \cdots + n_1 p + n_0,
   $
   $
   k = k_r p^r + k_{r-1} p^{r-1} + \cdots + k_1 p + k_0,
   $
   donde $ 0 \leq n_i, k_i < p $.

2. **Verificar que $ k_i \leq n_i $ para todos los dígitos:**
   Si en alguna posición $ k_i > n_i $, el resultado es:
   $
   \binom{n}{k} \mod p = 0.
   $

3. **Calcular los coeficientes binomiales individuales $ \binom{n_i}{k_i} $:**
   Para cada posición $ i $, calcula $ \binom{n_i}{k_i} $ usando la fórmula clásica de coeficientes binomiales:
   $
   \binom{n_i}{k_i} = \frac{n_i!}{k_i!(n_i - k_i)!}.
   $
   Trabaja módulo $ p $ en cada cálculo.

4. **Multiplicar los resultados parciales:**
   Una vez que tienes $ \binom{n_i}{k_i} \mod p $ para cada $ i $, calcula el producto total:
   $
   \binom{n}{k} \mod p = \prod_{i=0}^{r} \binom{n_i}{k_i} \mod p.
   $

5. **Devolver el resultado:**
El valor acumulado del producto es el resultado final de $ \binom{n}{k} \mod p $.


## Ejemplo práctico



### **Para los valores $ p = 5 $, $ n = 482 $, y $ k = 176 $, hemos descompuesto $ n $ y $ k $ en base 5:**

**Descomposición en base 5**


- Descomposición de $ n = 482 $ en base 5:
$
n = [2, 1, 4, 3]_5
$
- Descomposición de $ k = 176 $ en base 5:
$
k = [1, 0, 2, 1]_5
$

**Cálculo de los coeficientes binomiales mod 5 para cada par de dígitos**

Los coeficientes binomiales mod 5 para cada par de dígitos son los siguientes:

$\quad \binom{2}{1} \mod 5 = 2$
$ \quad \binom{1}{0} \mod 5 = 1$
$ \quad \binom{4}{2} \mod 5 = 1$
$ \quad \binom{3}{1} \mod 5 = 3$


Resultado final

El resultado final es:

$
\binom{482}{176} \mod 5 = 2 \cdot 1 \cdot 1 \cdot 3 \mod 5 = 1.
$

Por lo tanto,
$\binom{482}{176} \mod 5 = 1.$




###  **Tomemos $ n = 123 $, $ k = 45 $, y $ p = 11 $. Aplicamos el Teorema de Lucas.**

1. Descomponer $ n $ y $ k $ en base $ p = 11 $:
Descomposición de $ n = 123 $:
$
123 \div 11 = 11 \quad \text{cociente, residuo} \ 2 \quad \Rightarrow \quad n = 123 = (1 \cdot 11^2) + (0 \cdot 11^1) + (2 \cdot 11^0)
$
$
n = [1, 0, 2]_{11}
$
Descomposición de $ k = 45 $:
$
45 \div 11 = 4 \quad \text{cociente, residuo} \ 1 \quad \Rightarrow \quad k = 45 = (0 \cdot 11^2) + (4 \cdot 11^1) + (1 \cdot 11^0)
$
$
k = [0, 4, 1]_{11}
$

2. Aplicar el Teorema de Lucas:
Según el teorema:
$
\binom{123}{45} \mod 11 = \binom{1}{0} \cdot \binom{0}{4} \cdot \binom{2}{1} \mod 11
$

3. Calcular los coeficientes binomiales módulo $ p = 11 $:
- Primer término:
  $
  \binom{1}{0} = 1
  $
- Segundo término:
  $
  \binom{0}{4} = 0 \quad \text{(ya que $ 4 > 0 $)}
  $
- Tercer término:
  $
  \binom{2}{1} = \frac{2!}{1!(2 - 1)!} = 2
  $

4. Producto de los términos:}
$
\binom{123}{45} \mod 11 = 1 \cdot 0 \cdot 2 = 0
$

5. Resultado final:
$
\binom{123}{45} \mod 11 = 0
$
Esto indica que $ \binom{123}{45} $ es divisible por $ 11 $.

