# Totient de Euler o Función de Euler

> La **función de Euler**, también conocida como **φ(n)** o **totient**, es una función matemática que cuenta la cantidad de enteros positivos menores o iguales a n que son coprimos con n. 

*Dos números son coprimos si el único divisor común entre ellos es 1.*



> Para un número $ n $, si su factorización en números primos es: $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$
>
> donde $ p_1, p_2, \dots, p_k $ son primos distintos, la función totient se calcula como:
>
> $
> \varphi(n) = n \left( 1 - \frac{1}{p_1} \right) \left( 1 - \frac{1}{p_2} \right) \cdots \left( 1 - \frac{1}{p_k} \right)
> $

**Ejemplo:** Para calcular $ \varphi(12) $:

Factorizamos $ 12 = 2^2 \cdot 3 $.

Aplicamos la fórmula:

$
\varphi(12) = 12 \left( 1 - \frac{1}{2} \right) \left( 1 - \frac{1}{3} \right)
$

$\varphi(12) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4$

Entonces, hay 4 números menores o iguales a 12 que son coprimos con 12: $ 1, 5, 7, 11 $.



## **Propiedades:**

- $\varphi(1) = 1$

- Si $ p $ es primo, entonces:

  $\varphi(p) = p - 1$

  - porque todos los números menores a $ p $ son coprimos con $ p $.

- La función es multiplicativa, es decir, si $ a $ y $ b $ son coprimos, entonces:

  $\varphi(a \cdot b) = \varphi(a) \cdot \varphi(b)$

-  la cantidad de números entre 1 y $p^k$ que son divisibles por $p$, donde $p$ es un número primo y $k\ge 1$

- Si $p$ es primo y  $k\ge 1$, entonces hay exactamente $\frac{p^k}{p}$ números entre 1 y $p^k$ que dividen a p:

  $\varphi(p^k) = p^k - p^{k-1} = p^k (1-\frac{1}{p})$

> Si usamos $ p = 5 $ y $ k = 4 $, queremos encontrar cuántos números entre $ 1 $ y $ 5^4 = 625 $ son divisibles por $ 5 $.
> **Paso 1: Aplicar la fórmula**
> La fórmula es:
> 
> $
> \frac{5^4}{5} = 5^{4-1} = 5^3 = 125
> $
> 
> Calculamos:
> 
> $
> 5^4 = 625
> $
> $
> \frac{625}{5} = 125
> $
> 
> **Paso 2: Interpretación**
> Esto significa que hay exactamente 125 números entre $ 1 $ y $ 625 $ que son divisibles por $ 5 $. Estos números son:
> 
> $
> 5, 10, 15, 20, \dots, 625
> $
> 
> Y efectivamente, si los contamos, hay 125 múltiplos de $ 5 $ en este rango.

- En general, para números no coprimos $a$ y $b$ se cumple:

  $\varphi(ab) = \varphi(a) . \varphi(b) .\frac{d}{\varphi(d) }  $

  donde: $d = MCD(a,b)$



## **Orden** multiplicativo de un elemento

> Siendo n un numero positivo entero y $a$ un entero tal que $MCD(a, n) = 1$
>
> El orden de un número $ a $ módulo $ n $ es el menor entero positivo $ k $ tal que:
>
> $
> a^k \equiv 1 \pmod{n}
> $
>
> Es decir, el orden de $ a $ es el número de veces que debes multiplicar $ a $ por sí mismo (tomando módulo $ n $) hasta que obtienes 1.
>
> 
>
> $Ord_{n}(a) = k$       Se lee: Orden de $a$ modulo $n$

**Ejemplo:** Si $ a = 2 $ y $ n = 7 $, el orden de 2 módulo 7 es 3, porque:

$
2^1 \equiv 2 \pmod{7}
$
$2^2 \equiv 4 \pmod{7}$
$2^3 \equiv 1 \pmod{7}$

Por lo tanto, el orden de 2 módulo 7 es 3.



### propiedades

*si se cumple $MCD(a,n)=1$ y $r = Ord_{n}(a)$*

- si $a^m \equiv 1 \  (mod\ n)$, donde $m$ es un numero entero positivo, entonces $r|m$
- si $r | \varphi(n)$
- para dos enteros $s$ y $t$,  $a^t \equiv a^s \ (mod\ n)$ se cumple si: $s \equiv t\ (mod \ n)$
- si $m$ es un entero positivo, entonces en orden de $a^m$ modulo $n$  es $\frac{r}{MCD(r, m)}$
- En  orden de $a^m$ modulo $n$  es $r$ si y solo si $MCD(m,r)=1$





## **Raíces primitivas** de n

>  Una raíz primitiva de $ n $ es un número $ g $ tal que sus potencias generan todos los números enteros coprimos menor o igual a $ n $, es decir, $ \{ 1, 2, 3, \dots, n-1 \} $ bajo el módulo $ n $.

Formalmente, $ g $ es una raíz primitiva de $ n $ si su orden módulo $ n $ es igual a $ \varphi(n) $, el número de enteros menores que $ n $ y que son coprimos con $ n $. 

$g = Ord_{n}(a) =  \varphi(n) $



### **Ejemplo:** Si $ n = 7 $, las raíces primitivas de 7 son 3 y 5, porque sus potencias generan todos los números coprimos con 7.

Las raíces primitivas de un número $ p $ (en este caso $ 7 $) se calculan en el grupo multiplicativo de los números enteros módulo $ p $. Estas raíces son los generadores del grupo cíclico $ \mathbb{Z}_p^* $.

**Pasos para calcular las raíces primitivas de 7:**

**Identificar el grupo:**
El grupo $ \mathbb{Z}_7^* $ contiene los números $ \{1, 2, 3, 4, 5, 6\} $.

**Calcular el orden de cada número:**
El orden de un número $ g $ es el menor entero $ k $ tal que: $g^k \equiv 1 \pmod{7}$

Una raíz primitiva tiene un orden igual a *$ \varphi(7) = 6 $*, donde $ \varphi $ es la función de Euler.

**Probar cada número:**
Para cada $ g \in \{2, 3, 4, 5, 6\} $, calcular las potencias sucesivas módulo 7. Si $ g^k \pmod{7} $ genera todos los elementos del grupo $ \mathbb{Z}_7^* $ antes de volver a 1, $ g $ es una raíz primitiva.

**Cálculos:**

- Para $ g = 2 $:

$
2^1 \equiv 2 \pmod{7}, \quad 2^2 \equiv 4 \pmod{7}, \quad 2^3 \equiv 1 \pmod{7}
$

El $ord_7(2) = 3$ , no es raíz primitiva.

- Para $ g = 3 $:

$
3^1 \equiv 3 \pmod{7}, \quad 3^2 \equiv 2 \pmod{7}, \quad 3^3 \equiv 6 \pmod{7}, \quad 3^4 \equiv 4 \pmod{7}, \quad 3^5 \equiv 5 \pmod{7}, \quad 3^6 \equiv 1 \pmod{7}
$

El  $ord_7(3) = 6$, es raíz primitiva.

- Para $ g = 4 $:

$
4^1 \equiv 4 \pmod{7}, \quad 4^2 \equiv 2 \pmod{7}, \quad 4^3 \equiv 1 \pmod{7}
$

El orden de 4 es 3, no es raíz primitiva.

- Para $ g = 5 $:

$
5^1 \equiv 5 \pmod{7}, \quad 5^2 \equiv 4 \pmod{7}, \quad 5^3 \equiv 6 \pmod{7}, \quad 5^4 \equiv 2 \pmod{7}, \quad 5^5 \equiv 3 \pmod{7}, \quad 5^6 \equiv 1 \pmod{7}
$

El orden de 5 es 6, es raíz primitiva.

- Para $ g = 6 $:

$
6^1 \equiv 6 \pmod{7}, \quad 6^2 \equiv 1 \pmod{7}
$

El orden de 6 es 2, no es raíz primitiva.

**Resultado:**
Las raíces primitivas de $ 7 $ son:

$
\{ 3, 5 \}
$



## Función de Euler
Este teorema es una generalización del Pequeño Teorema de Fermat. Si $ a $ es un entero positivo y $ n $ es un número entero positivo tal que $ \gcd(a, n) = 1 $ (es decir, $ a $ y $ n $ son coprimos), entonces:

> $a^{\varphi(n)} \equiv 1 \pmod{n}$

Donde $ \varphi(n) $ es la función phi de Euler, que cuenta la cantidad de enteros positivos menores o iguales a $ n $ que son coprimos con $ n $.

**Ejemplo:**

Si $ n = 10 $ y $ a = 3 $:

$
\varphi(10) = 4 \quad (\text{ya que los números coprimos con 10 son } 1, 3, 7, 9)
$

Entonces, según el Teorema de Euler:

$
3^4 \equiv 1 \pmod{10}
$

## El Pequeño teorema de Fermat

Este teorema establece que:

Si $ p $ es un número primo y $ a $ es un entero tal que $ a $ no es divisible por $ p $, entonces:

> $a^{p-1} \equiv 1 \pmod{p}$

**Ejemplo:**

Si $ p = 7 $ y $ a = 3 $:

$
3^{7-1} = 3^6 = 729
$

Y

$
729 \pmod{7} = 1
$

Por lo tanto, $ 3^6 \equiv 1 \pmod{7} $.



**Relación entre ambos:**

El Pequeño Teorema de Fermat es un caso particular del Teorema de Euler cuando $ n $ es primo, ya que $ \varphi(p) = p - 1 $ para cualquier número primo $ p $.





## bibliografía

https://cp-algorithms.com/algebra/phi-function.html
https://hojamat.es/parra/raizprim.pdf


