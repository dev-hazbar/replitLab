# Binomio de Newton

El binomio de Newton es una fórmula que permite expandir potencias de binomios de la forma $ (a + b)^n $ en términos de una suma de términos. La fórmula general es:


$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$
**Componentes principales:**

- **Coeficiente binomial**: 

  $$
  \binom{n}{k} = \frac{n!}{k!(n-k)!}
  $$

Representa el número de formas de elegir $ k $ elementos de un conjunto de $ n $ elementos.

- **Expresión general**: Cada término en la expansión es de la forma:

  $$
  \binom{n}{k} a^{n-k} b^k
  $$

Donde:
- $ k $ va desde $ 0 $ hasta $ n $.
- $ a^{n-k} $ y $ b^k $ representan las potencias de los términos $ a $ y $ b $, respectivamente.

---

**Ejemplo práctico: Expandir $ (x + y)^3 $:**

Aplicando la fórmula:

$
(x + y)^3 = \sum_{k=0}^{3} \binom{3}{k} x^{3-k} y^k
$

Calcular cada término:

- Para $ k = 0 $: $\binom{3}{0} x^{3-0} y^0 = 1 \cdot x^3 \cdot 1 = x^3$

- Para $ k = 1 $: $\binom{3}{1} x^{3-1} y^1 = 3 \cdot x^2 \cdot y = 3x^2 y$

- Para $ k = 2 $: $\binom{3}{2} x^{3-2} y^2 = 3 \cdot x^1 \cdot y^2 = 3xy^2$

- Para $ k = 3 $: $\binom{3}{3} x^{3-3} y^3 = 1 \cdot x^0 \cdot y^3 = y^3$

**Resultado final**:

$(x + y)^3 = x^3 + 3x^2 y + 3xy^2 + y^3$

---
**Para expandir $(x + y)^5$ utilizando el binomio de Newton:**

Fórmula general:
$
(x + y)^5 = \sum_{k=0}^{5} \binom{5}{k} x^{5-k} y^k
$

Coeficientes binomiales:
Calculamos $\binom{5}{k}$ para $k = 0, 1, 2, 3, 4, 5$:

$
\binom{5}{0} = 1, \quad \binom{5}{1} = 5, \quad \binom{5}{2} = 10, \quad \binom{5}{3} = 10, \quad \binom{5}{4} = 5, \quad \binom{5}{5} = 1
$

Desarrollo de términos:
$
(x + y)^5 = \binom{5}{0} x^5 y^0 + \binom{5}{1} x^4 y^1 + \binom{5}{2} x^3 y^2 + \binom{5}{3} x^2 y^3 + \binom{5}{4} x^1 y^4 + \binom{5}{5} x^0 y^5
$

Sustituyendo valores:

$
\binom{5}{0} x^5 y^0 = 1 \cdot x^5 = x^5
$
$
\binom{5}{1} x^4 y^1 = 5 \cdot x^4 y = 5x^4 y
$
$
\binom{5}{2} x^3 y^2 = 10 \cdot x^3 y^2 = 10x^3 y^2
$
$
\binom{5}{3} x^2 y^3 = 10 \cdot x^2 y^3 = 10x^2 y^3
$
$
\binom{5}{4} x^1 y^4 = 5 \cdot x y^4 = 5xy^4
$
$
\binom{5}{5} x^0 y^5 = 1 \cdot y^5 = y^5
$

Resultado final:
$
(x + y)^5 = x^5 + 5x^4 y + 10x^3 y^2 + 10x^2 y^3 + 5xy^4 + y^5
$

