# ecuación modular



## propiedad de aritmética modular

> x ≡ a mod n
>
> **otra Forma de escribir la equivalencia**
>
> x = nk+a        k ∈ ℤ

>**Se puede realizar operación suma en ambos miembros**
>
>3k + 1 ≡ 4 mod 5
>
>3k + 1 **+4** ≡ 4 **+4** mod 5
>
>*Recomendable sumar números para obtener múltiplos del módulo*

>10r+4 ≡ 1 mod 7
>
>**10r** ---> **7r + 3r** dividir en múltiplos del modulo
>
>4 *+ 3* ----> 7 sumar para cumplir múltiplos del modulo

>**Los múltiplos del módulo se anulan**
>
>**7r** + 3r **+7** ≡ 4 mod 7
>
>7r = 0 por ser múltiplo de 7
>
>7 = 0 por ser múltiplo de 7
>
>3r ≡ 4 mod 7

>**Calcular el inverso**
>
>en la aritmética modular no existe la división por lo tanto aplicar el inverso modular
>
>o encontrar un numero que sea igual que **modulo ± 1** que es lo mismo que calcular el inverso modular 
>
>**(2)**3r  ≡ 4**(2)** mod 7
>
>6r ≡ 8 mod 7
>
>6r**+r-r** ≡ 7+1 mod 7
>
>**7r**-r ≡ 1 mod 7
>
>-r ≡ 1 mod 7
>
>r ≡ -1 mod 7
>
>r ≡ **0** -1 mod 7
>
>r ≡ **7** -1 mod7
>
>r ≡ 6 mod 7

## Teoría de ecuación modular

> teniendo la siguiente ecuación modular
>
> *ax ≡ b mod n*
>
> **La ecuación tiene solución si:**
>
> MCD(a, n) | b   
>
> (**MCD(a, n) divide a  "b"** )



>*ax ≡ b mod n*
>
>si se cumple MCD(a, n) | b    pero  MCD(a, n) = d   &  d != 1
>
>se puede reducir a una ecuación equivalente dividiendo cara miembro el MCD
>
>ax/d ≡  b/d   (mod  n/d)
>
>
>
>ejemplo: *10x ≡ 5 mod 15*
>
>MCD(10,15) = 5
>
>10x/5  ≡ 5/5  mod 15/5
>
>2x ≡ 1 mod 3 

> La cantidad de soluciones que una una ecuación modular tiene esta dada por el MCD
>
> si MCD = 1 , Tiene una única solución
>
> si MCD = 5, posee 5 soluciones

> *ax ≡ b mod n*
>
> Las soluciones se calculan usando la siguiente formula
>
> **x = x₀ + (n / MCD(a, n))k**
>
> k ∈ ℤ    k = 1, 2, 3, ...<MCD(a,n)
>
> 
>
>  **x₀** : la primera solución cuando de su ecuación reducida

`Resolveremos la ecuación modular con varias soluciones 10x ≡ 20 (mod 25).`


```
Paso 1: Plantear la ecuación
Supongamos que tenemos:

10x ≡ 20 (mod 25).

Aquí:
a = 10,
m = 25,
b = 20.

El gcd(10, 25) = 5, lo cual implica que la ecuación tiene 5 soluciones distintas.

Paso 2: Reducir la ecuación
Dividimos la ecuación completa por el gcd(10, 25) = 5:

(10x)/5 ≡ 20/5 (mod 25/5).
Esto simplifica a:

2x ≡ 4 (mod 5).

Paso 3: Resolver la ecuación reducida
Para 2x ≡ 4 (mod 5), calculamos el inverso multiplicativo de 2 (mod 5), que es 3 (porque 2 ⋅ 3 ≡ 1 (mod 5)).

Multiplicamos ambos lados por 3:

x ≡ 4 ⋅ 3 (mod 5).
x ≡ 12 (mod 5).
x ≡ 2 (mod 5).

La solución de la ecuación reducida es:

x ≡ 2 (mod 5).

Paso 4: Expandir las soluciones al módulo original
El módulo original es 25, y como gcd(10, 25) = 5, habrá 5 soluciones distintas. Las soluciones se generan a partir de:

x = 2 + (25/5)k = 2 + 5k, k ∈ {0, 1, 2, 3, 4}.

Sustituimos k con estos valores:

Para k = 0: x = 2,
Para k = 1: x = 2 + 5⋅1 = 7,
Para k = 2: x = 2 + 5⋅2 = 12,
Para k = 3: x = 2 + 5⋅3 = 17,
Para k = 4: x = 2 + 5⋅4 = 22.

Paso 5: Verificar las soluciones
Sustituimos estas soluciones (x = 2, 7, 12, 17, 22) en la ecuación original 10x ≡ 20 (mod 25):

Para x = 2: 10⋅2 = 20 ≡ 20 (mod 25),
Para x = 7: 10⋅7 = 70 ≡ 20 (mod 25),
Para x = 12: 10⋅12 = 120 ≡ 20 (mod 25),
Para x = 17: 10⋅17 = 170 ≡ 20 (mod 25),
Para x = 22: 10⋅22 = 220 ≡ 20 (mod 25).

Todas son válidas.

Respuesta final
La ecuación 10x ≡ 20 (mod 25) tiene las 5 soluciones distintas:

x ≡ 2, 7, 12, 17, 22 (mod 25).

```



`Resolveremos la ecuación modular 3x ≡ 4 (mod 7).`

```
Pasos:
1. Determinar si la ecuación tiene solución:
   Verificamos si gcd(3, 7) = 1. Como 3 y 7 son coprimos, la ecuación tiene solución única módulo 7.

2. Encontrar el inverso multiplicativo de 3 módulo 7:
   El inverso multiplicativo de 3 es el número y tal que:
   3y ≡ 1 (mod 7).
   Probamos valores de y:
   - 3⋅1 = 3 ≡ 1 (mod 7)
   - 3⋅1 = 3 ≡ 1 (mod 7)
   - 3⋅2 = 6 ≡ 1 (mod 7)
   - 3⋅3 = 9 ≡ 2 (mod 7)
   - 3⋅5 = 15 ≡ 1 (mod 7)

   Por lo tanto, el inverso de 3 módulo 7 es 5.

3. Multiplicar ambos lados de la ecuación por el inverso:
   5⋅(3x) ≡ 5⋅4 (mod 7)
   x ≡ 20 (mod 7).

4. Reducir 20 módulo 7:
   20 ÷ 7 = 2 (residuo 6).

   Por lo tanto:
   x ≡ 6 (mod 7).

Solución:
La solución es x ≡ 6 (mod 7).
```




## prompt para un ejercicio
Genera una lista de casos de prueba para un test unitario en formato de texto. Enfócate en casos críticos para el problema, detallando tipos de entrada y valores esperados.

Resolver una ecuación lineal modular:

Descripción: Dado tres enteros a, b, y n, resuelve la ecuación ax ≡ b mod n para x.
Entrada: Tres enteros a, b, y n donde 1 ≤ a, b, n ≤ 10^9.
Salida: Un entero x que satisface la ecuación, o indica que no hay solución.
Ejemplo: Entrada: 3 4 7, Salida: 5 (porque 3⋅5 ≡ 4 mod 7).

FORMATO DE RESPUESTA:
Agragale un comentario en el encabezado cada caso de prueba, por cada caso de prueba debe haber 3 tests
entregame la salida en un textbox,
(la entrada y valor esperado esten en una linea por caso)
Inputs: 3 4 7 -> expected: 5


