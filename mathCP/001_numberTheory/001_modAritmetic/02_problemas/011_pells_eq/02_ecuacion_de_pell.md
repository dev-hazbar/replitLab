# Ecuación de pell

Una **ecuación de Pell** es una [ecuación diofántica](https://es.wikipedia.org/wiki/Ecuación_diofántica) de la forma:

> $x^2−Dy^2=1$
>
> donde **D** es un entero positivo que no es un cuadrado perfecto, $x$ e $y$ son enteros que queremos encontrar.

Donde *n* es un [número entero](https://es.wikipedia.org/wiki/Número_entero).



## Pasos para resolver la ecuación de Pell:

  1. **Expandir $ D $ en una fracción continua periódica:**
      Calcular la fracción continua periódica de  $\sqrt{D}$. Esta fracción continua se usa para encontrar soluciones de la ecuación.

 

Escribe $D$ como una fracción continua:

$$
   D = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \cdots}}}
$$

   Donde:

   - $ a_0 = \lfloor \sqrt{D} \rfloor $ (la parte entera de$ \sqrt{D} $).
   - Encuentra los coeficientes $ [a_0; a_1, a_2, a_3, \dots] $ hasta que la expansión se vuelva periódica.


2. **Solución fundamental:**
   La primera solución fundamental $ (x_1, y_1) $ puede obtenerse usando la fracción continua. Es el par de enteros que satisface la ecuación para el menor período.

   
   - **Calculo de convergencia**
      Los convergentes son fracciones que se obtienen truncando la fracción continua después de $ k $ términos. Si la fracción continua es:

      $$
      D = [a_0; a_1, a_2, \dots, a_k, \dots]
      $$

      Los convergentes se calculan como:

      $$
      \frac{p_k}{q_k}
      $$

      donde:

      - $ p_k $ y $ q_k $ se calculan recursivamente:

      $$
      p_{-2} = 0, \quad p_{-1} = 1, \quad p_k = a_k p_{k-1} + p_{k-2}\\
      q_{-2} = 1, \quad q_{-1} = 0, \quad q_k = a_k q_{k-1} + q_{k-2}
      $$
   - **Probar los convergentes**

      Sustituye cada convergente $ (p_k, q_k) $ en la ecuación: $x^2 - D y^2 = 1$

      La primera pareja $ (p_k, q_k) $ que satisfaga la ecuación es la *solución fundamental* $ (x_1, y_1) $.


3. **Generar soluciones adicionales:**
   Si $ (x_1, y_1) $ es la *solución fundamental*, las soluciones generales están dadas por la siguiente fórmula:

   $x_n + y_n \sqrt{D} = (x_1 + y_1 \sqrt{D})^n$

   Donde *$ n $ es un entero positivo*. Los valores de $ x_n $ y $ y_n $ se obtienen expandiendo la potencia de la expresión.
   
   **NOTA**; una vez expandido la potencia de la expresión:
   
   ​	$x_n$: será la parte entera
   
   ​	$y_n$: será en coeficiente de $\sqrt{D}$

## Ejemplo

### Resolver $ x^2 - 2y^2 = 1 $:

**Fracción continua de $ \sqrt{2} $:**

La fracción continua de $ \sqrt{2} $ es: $ \sqrt{2} = [1; 2, 2, 2, \dots]$

**Solución fundamental:**

Tomando el primer par convergente: $x_1 = 3, \quad y_1 = 2$


Verificamos: $ 3^2 - 2 \cdot 2^2 = 9 - 8 = 1$

Entonces, $ (x_1, y_1) = (3, 2) $ es la solución fundamental.

**Soluciones adicionales:**
> Solución general 
> $$
> (x_n, y_n) = \left( x_1 + y_1 \cdot \sqrt{2} \right)^n = \left( 3 + 2 \cdot \sqrt{2} \right)^n
> $$

Para $ n = 2 $:

$$
(x_2, y_2) = \left( x_1 + y_1 \cdot \sqrt{2} \right)^2 = \left( 3 + 2 \cdot \sqrt{2} \right)^2\\
expandiendo:\ x_2 = 17, \quad y_2 = 12
$$


**Solución para $ n = 3 $:**

$
\left( x_1 + \frac{y_1}{2} \right)^3 = \left( 3 + \frac{2}{2} \right)^3
$

Expandimos usando el binomio de Newton:

$
\left( 3 + \frac{2}{2} \right)^3 = 3^3 + 3 \cdot 3^2 \cdot \left( \frac{2}{2} \right) + 3 \cdot 3 \cdot \left( \frac{2}{2} \right)^2 + \left( \frac{2}{2} \right)^3
$

Parte entera:

$
x_3 = 3^3 + 3 \cdot 3 \cdot 2^2 = 27 + 54 = 99
$

Coeficiente de $ 2^2 $:

$
y_3 = 3 \cdot 3^2 \cdot 2 + 3 \cdot 2^3 = 54 + 16 = 70
$

Solución: $ (x_3, y_3) = (99, 70) $.

**Solución para $ n = 4 $:**

$
\left( x_1 + \frac{y_1}{2} \right)^4 = \left( 3 + \frac{2}{2} \right)^4
$

Expandimos:

$
\left( 3 + \frac{2}{2} \right)^4 = \left( 3 + \frac{2}{2} \right)^2 \cdot \left( 3 + \frac{2}{2} \right)^2
$

Sabemos que:

$
\left( 3 + \frac{2}{2} \right)^2 = 17 + 12 \cdot 2
$

Entonces:

$
\left( 3 + \frac{2}{2} \right)^4 = (17 + 12 \cdot 2)^2
$

Parte entera:

$
x_4 = 17^2 + 2 \cdot 12^2 = 289 + 288 = 577
$

Coeficiente de $ 2^2 $:

$
y_4 = 2 \cdot 17 \cdot 12 = 408
$

Solución: $ (x_4, y_4) = (577, 408) $.

**Solución para $ n = 5 $:**

$
\left( x_1 + \frac{y_1}{2} \right)^5 = \left( 3 + \frac{2}{2} \right)^5
$

Usamos la recurrencia:

$
x_5 = 2 \cdot 3 \cdot 577 - 99 = 3363
$

$
y_5 = 2 \cdot 3 \cdot 408 - 70 = 2378
$

Solución: $ (x_5, y_5) = (3363, 2378) $.



`Así, las soluciones son: (3, 2), (17, 12), (99, 70), (577, 408), (3363, 2378), ...`

