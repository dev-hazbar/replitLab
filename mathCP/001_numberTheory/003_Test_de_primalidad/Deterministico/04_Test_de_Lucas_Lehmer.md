# Lucas–Lehmer primality test



## **Los números de Mersenne**

Los números de Mersenne son números enteros que tienen la forma:

$M_p = 2^p - 1$
donde p es un número entero positivo. Los números de Mersenne llevan este nombre en honor al matemático francés Marin Mersenne, quien estudió sus propiedades en el siglo XVII.

Propiedades principales:
- Relación con las potencias de 2: Cada número de Mersenne es una unidad menos que una potencia de 2. Por ejemplo:
  $M_2 = 2^2 - 1 = 3$
  $M_3 = 2^3 - 1 = 7$
  $M_4 = 2^4 - 1 = 15$

- Primalidad: Un número de Mersenne M_p puede ser primo solo si p es primo. Sin embargo, no todos los números M_p con p primo son primos. Por ejemplo:
  $M_2 = 3$ (primo)
  $M_3 = 7$ (primo)
  $M_5 = 31$ (primo)
  $M_{11} = 2047 = 23 × 89$ (compuesto)

Importancia en matemáticas: Los números de Mersenne son fundamentales en la búsqueda de primos grandes, porque los algoritmos como el test de Lucas–Lehmer son muy eficientes para estos números.

Ejemplos de números de Mersenne:
$M_2 = 2^2 - 1 = 3$
$M_3 = 2^3 - 1 = 7$
$M_5 = 2^5 - 1 = 31$
$M_7 = 2^7 - 1 = 127$
$M_{11} = 2^{11} - 1 = 2047$

Aplicaciones:
- Criptografía: Los números de Mersenne primos son usados en algoritmos de generación de claves.
- Computación distribuida: Proyectos como GIMPS (Great Internet Mersenne Prime Search) buscan números de Mersenne primos extremadamente grandes utilizando computadoras conectadas en red.
- Teoría de números: Son relevantes para estudiar patrones y propiedades de números primos y compuestos.


## **El test de Lucas–Lehmer**

El test de Lucas–Lehmer es un algoritmo utilizado para determinar si un número de Mersenne 	
$M_p = 2^p - 1$ (donde p es un número primo) es primo. Es eficiente para este propósito y tiene una base matemática sólida.

Proceso del test:
- Condición inicial: El test solo se aplica a números de Mersenne $M_p = 2^p - 1$, donde $p$ debe ser un número primo.

- Secuencia de Lucas-Lehmer: Se define una secuencia S_n de la siguiente manera:
  - $S_0 = 4$
  - $S_n = (S_{n-1}^2 - 2)\  mod\  M_p$  para $ n ≥ 1$

- Iteración: Calcula $S_{p-2}$ (es decir, se hacen $p-2$ iteraciones a partir de $S_0$).

- Condición de primalidad:
  Si $S_{p-2}\  mod\  M_p = 0$, entonces $M_p$ es primo. De lo contrario, $M_p$ es compuesto.

Ejemplo: con p = 7 (para $M_7 = 2^7 - 1 = 127$):
$M_7 = 127$

Calcula la secuencia S_n:
$S_0 = 4$
$S_1 = (4^2 - 2) mod 127 = 14$
$S_2 = (14^2 - 2) mod 127 = 67$
$S_3 = (67^2 - 2) mod 127 = 42$
$S_4 = (42^2 - 2) mod 127 = 111$
$S_5 = (111^2 - 2) mod 127 = 0$

$S_5\  mod\  127 = 0$, por lo que $M_7 = 127$ es primo.

Propiedades y ventajas:
- Eficiencia: Aprovecha la estructura específica de los números de Mersenne.
- Simplicidad: Aunque involucra cálculos modulares repetidos, la implementación es directa.

Limitaciones:
- Solo funciona para números de Mersenne.
- Requiere que p sea primo; si p no lo es, M_p siempre será compuesto.
