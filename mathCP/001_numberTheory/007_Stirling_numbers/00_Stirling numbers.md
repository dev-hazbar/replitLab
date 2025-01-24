# **Stirling numbers**

\section*{Números de Stirling}

Los números de Stirling son herramientas matemáticas utilizadas en combinatoria para describir relaciones específicas entre particiones de conjuntos o términos relacionados con factoriales. Existen dos tipos principales:

1. Números de Stirling de Primer Tipo \( c(n,k) \)

Definición: Los números de Stirling de primer tipo, \( c(n,k) \), cuentan el número de permutaciones de \( n \) elementos con exactamente \( k \) ciclos.

Fórmula Recursiva:
$
c(n,k) = c(n-1,k-1) + (n-1) \cdot c(n-1,k)
$
$
c(0,0) = 1 \quad (\text{caso base})
$
$
c(n,0) = 0 \quad \text{para} \ n > 0
$
$
c(0,k) = 0 \quad \text{para} \ k > 0
$

Ejemplo:
$
c(3,2) = 3
$
Las permutaciones de 3 elementos con 2 ciclos son: 
$
(1)(23), \ (2)(13), \ (3)(12)
$

2. Números de Stirling de Segundo Tipo \( S(n,k) \)

Definición: Los números de Stirling de segundo tipo, \( S(n,k) \), cuentan el número de maneras de particionar \( n \) elementos en \( k \) subconjuntos no vacíos.

Fórmula Recursiva:
$
S(n,k) = k \cdot S(n-1,k) + S(n-1,k-1)
$
$
S(0,0) = 1 \quad (\text{caso base})
$
$
S(n,0) = 0 \quad \text{para} \ n > 0
$
$
S(0,k) = 0 \quad \text{para} \ k > 0
$

Ejemplo:
$
S(3,2) = 3
$
Las particiones de 3 elementos en 2 subconjuntos son:
$
\{1\}, \{2,3\}, \ \{2\}, \{1,3\}, \ \{3\}, \{1,2\}
$

Aplicaciones

  - Combinatoria: Contar permutaciones y particiones.
  - Probabilidad: Funciones generadoras y distribuciones.
  - Álgebra: Relación con los números de Bell y expansiones polinómicas.





**Números de Stirling**

Los números de Stirling son herramientas matemáticas utilizadas en combinatoria para describir relaciones específicas entre particiones de conjuntos o términos relacionados con factoriales. Existen dos tipos principales:

1. Números de Stirling de Primer Tipo \( c(n,k) \)

Definición: Los números de Stirling de primer tipo, \( c(n,k) \), cuentan el número de permutaciones de \( n \) elementos con exactamente \( k \) ciclos.

Fórmula Recursiva:
$
c(n,k) = c(n-1,k-1) + (n-1) \cdot c(n-1,k)
$
$
c(0,0) = 1 \quad (\text{caso base})
$
$
c(n,0) = 0 \quad \text{para} \ n > 0
$
$
c(0,k) = 0 \quad \text{para} \ k > 0
$

Ejemplo:
$
c(3,2) = 3
$
Las permutaciones de 3 elementos con 2 ciclos son: 
$
(1)(23), \ (2)(13), \ (3)(12)
$

2. Números de Stirling de Segundo Tipo \( S(n,k) \)

Definición: Los números de Stirling de segundo tipo, \( S(n,k) \), cuentan el número de maneras de particionar \( n \) elementos en \( k \) subconjuntos no vacíos.

Fórmula Recursiva:
$
S(n,k) = k \cdot S(n-1,k) + S(n-1,k-1)
$
$
S(0,0) = 1 \quad (\text{caso base})
$
$
S(n,0) = 0 \quad \text{para} \ n > 0
$
$
S(0,k) = 0 \quad \text{para} \ k > 0
$

Ejemplo:
$
S(3,2) = 3
$
Las particiones de 3 elementos en 2 subconjuntos son:
$
\{1\}, \{2,3\}, \ \{2\}, \{1,3\}, \ \{3\}, \{1,2\}
$

Aplicaciones

  - Combinatoria: Contar permutaciones y particiones.
  - Probabilidad: Funciones generadoras y distribuciones.
  - Álgebra: Relación con los números de Bell y expansiones polinómicas.

