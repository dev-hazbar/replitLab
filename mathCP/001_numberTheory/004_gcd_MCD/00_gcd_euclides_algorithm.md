# Máximo Común Divisor (MCD o gcd)

1. **Método de descomposición en factores primos**
   Pasos:

   - Descompón ambos números en sus factores primos.
   - Identifica los factores comunes.
- Multiplica los factores comunes elevados al menor exponente.

   *Ejemplo:*
   Para $ 60 $ y $ 48 $:
   $
   60 = 2^2 \cdot 3 \cdot 5
   $
   $
   48 = 2^4 \cdot 3
$

   Factores comunes: $ 2^2 $ y $ 3^1 $
   $
   MCD = 2^2 \cdot 3 = 12
$

2. **Algoritmo de Euclides**
   Pasos:

   - Divide el número mayor por el menor.
   - Sustituye el número mayor por el divisor y el menor por el residuo.
   - Repite hasta que el residuo sea 0. El último divisor es el MCD.

   *Ejemplo:*
   Para $ 60 $ y $ 48 $:
   $
   60 \div 48 = 1 \quad \text{(residuo } 12\text{)}
   $
   $
   48 \div 12 = 4 \quad \text{(residuo } 0\text{)}
   $
   $
   MCD = 12
   $

3. **Método de resta repetida (versión más básica del algoritmo de Euclides)**
   Pasos:

   - Resta el número menor al mayor hasta que ambos números sean iguales.
   - El valor resultante es el MCD.

   *Ejemplo:*
   Para $ 60 $ y $ 48 $:
   $
   60 - 48 = 12
   $
   $
   48 - 12 = 36
   $
   $
   36 - 12 = 24
   $
   $
   24 - 12 = 12
   $
   Cuando ambos números son iguales ($ 12 = 12 $), el MCD es $ 12 $.

4. **Propiedades útiles**

   - Si $ b $ divide a $ a $, entonces $ MCD(a,b) = b $.
   - $ MCD(a,b) = MCD(b, a \mod b) $.



## Algoritmo de Euclides



