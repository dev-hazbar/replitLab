# Sistemas de ecuación modular

## Teorema del resto Chino

- **Paso1**: Verificar si cada ecuación tenga solución 

  > ax ≡ b mod n 
  >
  > 
  >
  > *Si*: MCD(a, n) divide a  **b**   *entonces la ecuación tiene solución*

- **Paso2**:

  > *Para verificar si se puede resolver el ejercicio por el método del resto chino*
  >
  > **verificar si  en MCD de todos los módulos son co-primos**

  >Existe solución en  
  >
  >0 ≤ x < (Producto de todos los módulos)
  >
  



### **usando métodos de sustitución**

```
Hallar la solución de:
x ≡ 2 mod 5
2x ≡ 1 mod 7
3x ≡ 4 mod 11

PASO1:
Existe solución para cada ecuación:
MCD(1,5) = 1 divide a 2
MCD(2,7) = 1 divide a 1
MCD(3,11) = 1 divide a 4

PASO2:
Verificar si se puede usar el teorema del resto chino (Existe solución)
en MCD de 2 a 2 de los modulos (5, 7, 11)
MCD(5,7) = 1
MCD(7,11) = 1
MCD(5,11) = 1
Entonces ---> como todos los módulos son co-primos Existe solución

PASO3:
x ≡ 2 mod 5
x = 5r + 2      r ∈ ℤ

Remplazar en la ecuación: 2x ≡ 1 mod 7
2(5r + 2) ≡ 1 mod 7
10r + 4 ≡ 1 mod 7
7r+3r + 4+3 ≡ 1+3 mod 7
3r ≡ 4 mod 7               calcular el inverso de 3 mod 7 = 2
2(3)r ≡ 4(2) mod 7
6r ≡ 8 mod 7
7r-r ≡ 7+1 mod 7
-r ≡ 1 mod 7
r ≡ -1 mod 7
r ≡ 6 mod 7
r = 7s + 6

Remplazar en r en función de s en : x = 5r + 2
x = 5(7s + 6)+2
x = 35s + 32    s ∈ ℤ

Remplazar en la ecuación 3: 3x ≡ 4 mod 11
3x ≡ 4 mod 11
3(35s + 32) ≡ 4 mod 11
105s + 96 ≡ 4 mod 11
6s ≡ 7 mod 11        calcular el inverso de 6 mod 11 = 2
s ≡ 3 mod 11
s = 11t + 3   t ∈ ℤ

remplazar t en :
x = 35s + 32    s ∈ ℤ
x = 35(11t + 3) + 32   
x = 385t + 137 

Entoces la respuesta es : 137



```

### **Usando la formula del resto chino**

> x = ∑ ai × Mi × modinv(Mi, ni)  (mod N)

#### `Derivación de la formula`

```
Teorema del Resto Chino:
El teorema del resto chino establece que si tienes un sistema de congruencias de la forma:

x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
⋮
x ≡ ak (mod nk)

si los ni son coprimos (es decir, el máximo común divisor de cada par de ni y nj es 1), entonces existe una única solución para x módulo N, donde N es el producto de todos los ni (es decir, N = n1 × n2 × ⋯ × nk).

DERIVACIÓN DE LA FORMULA:
1. Multiplicación por el producto de los módulos: El valor x se puede expresar como una suma ponderada de los restos ai y los módulos ni. La clave aquí es que queremos una forma de "ajustar" cada ai a una congruencia válida en su módulo ni.

2. Construcción del producto: Para cada congruencia, se construye un término:

Mi = N / ni

Aquí, Mi es el producto de todos los nj excepto ni. Este Mi es el factor que ajusta la congruencia de ai para que, cuando se sume, contribuya a la solución final en el módulo N.

3. Corrección de Mi: Para que el término "ai × Mi" sea congruente con ai en el módulo ni, necesitamos multiplicarlo por el inverso multiplicativo de Mi módulo ni, que se denota como modinv(Mi, ni).

Es decir, necesitamos encontrar un valor bi tal que:

Mi × bi ≡ 1 (mod ni)

Composición de la solución: La solución final es una suma ponderada de todos los términos ai × Mi × modinv(Mi, ni), lo que da como resultado la fórmula:
ni: modulo i-esimo
x = ∑ ai × Mi × modinv(Mi, ni)  (mod N)

Donde el valor final de x es el resultado del sistema de congruencias, y se toma módulo N.

En resumen:
La fórmula ai × modinv(Mi, ni) × Mi asegura que cada término contribuya de manera correcta a la solución final. El inverso multiplicativo modinv(Mi, ni) es necesario para "ajustar" el valor de Mi para que, al sumarlo, el resultado sea congruente con ai en el módulo ni.

```

```
Aplicando la fórmula del TCR:
Paso 1: Calcular N
N = 5 ⋅ 7 ⋅ 11 = 385

Paso 2: Calcular Mi para cada mi:
M1 = 385 / 5 = 77
M2 = 385 / 7 = 55
M3 = 385 / 11 = 35

Paso 3: Calcular Mi^(-1) (inverso modular):
M1^(-1) módulo 5:
77 ≡ 2 (mod 5), y el inverso de 2 módulo 5 es 3.

M2^(-1) módulo 7:
55 ≡ 6 (mod 7), y el inverso de 6 módulo 7 es 6.

M3^(-1) módulo 11:
35 ≡ 2 (mod 11), y el inverso de 2 módulo 11 es 6.

Paso 4: Sustituir en la fórmula:
x ≡ a1 M1 M1^(-1) + a2 M2 M2^(-1) + a3 M3 M3^(-1) (mod N)
x ≡ (2 ⋅ 77 ⋅ 3) + (4 ⋅ 55 ⋅ 6) + (5 ⋅ 35 ⋅ 6) (mod 385)

Calculamos cada término:
2 ⋅ 77 ⋅ 3 = 462
4 ⋅ 55 ⋅ 6 = 1320
5 ⋅ 35 ⋅ 6 = 1050

Suma:
462 + 1320 + 1050 = 2832

Paso 5: Reducir módulo 385:
2832 ÷ 385 = 7 (residuo 97).

Por lo tanto:
x ≡ 97 (mod 385)

Solución final:
x = 97 + 385k, k ∈ Z

```





