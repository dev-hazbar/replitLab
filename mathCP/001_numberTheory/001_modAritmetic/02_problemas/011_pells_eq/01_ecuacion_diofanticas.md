

# Ecuaciones diofánticas

- Una ecuación diofántica es una ecuación en la que interesa encontrar las soluciones enteras



## propiedades de las ecuaciones diofánticas



## Ecuaciones diofánticas lineales o identidad de Bézout

> Ecuaciones de la forma:
>
> **$ax + by = c$**
>
> *en la que "x" e "y" son variables*
>
> *siendo a, b y c números enteros dados*

>Existencia de solución:
>
>$Ax + By = C$
>
>si cumple: $d={mcd} (A,B)$ es un divisor de *C* 
>
>en otras palabras si $d$ divide a $C$

>**Solución General**:
>
>Si una ecuación diofántica tiene solución, necesariamente tiene infinitas soluciones y todas son de la forma:
>
>**$x = x_0 + u\frac{B}{d}$**
>
>**$y = y_0 - u\frac{A}{d}$**
>
>Donde $d=mcd(A,B)$, "u" ∈ Z  y $x_0$ e $y_0$ son una solución particular de la ecuación.

### Solucion particular de Ecuaciones diofánticas lineales o identidad de Bézout

teniendo la siguiente ecuación a solucionar: $Ax + By = C$

- **paso1**: Verificar la existencia de solución: si cumple: $d={mcd} (A,B)$ es un divisor de *C* 

- **paso2**: si $d$ es diferente de 1 entonces rescribir la función 

  $Ax + By = d$

- **paso3**: obtener los valores de $x_1$ e $y_1$1 utilizando *el algoritmo extendido de Euclides*

- **paso4**: Obtener los $x$ e $y$ para la ecuación original

  $C_0 = \frac{C}{d}$

  $ x_0 = C_0x_1$

  $ y_0 =  C_0y_1$

- **paso5**: Obtener la solución generalizada



### Solución particular

Tenemos la ecuación diofántica **$6x+10y=104$**

1. Buscamos el *d* = mcd(6, 10). A través del algoritmo de Euclides encontramos que d=2. Como d|C (donde "|" significa "divide a"), es decir, 2|104, 
2. rescribimos la ecuación: **$6x+10y=2$**
3. calculamos una solución particular mediante la Identidad de Bézout: x1=2 e y1=−1. **Utilizando algoritmo de Euclides extendido** La ecuación quedaría así: $ 6(2)+10(−1)=2$.
4. Ahora tenemos una solución para la ecuación $6x+10y=2$. Con $x_1=2 $ e $ y_1=−1$. Si multiplicamos cada parte de la ecuación por $C_0 =\frac{C}{d}=\frac{104}{2}=52$, tendremos la solución particular de nuestra ecuación original $6x+10y=104$. La ecuación quedaría así: 6⋅2⋅52+10⋅(−1)⋅52=104. por lo tanto x0=104 e y0=−52
5. Con lo que hemos visto arriba, buscamos la solución general:
  > $x = x_0 + u\frac{B}{d} = 104 + u\frac{10}{2} = 104 + 5u$
  > $y = y_0 - u\frac{A}{d} = -52 - u\frac{6}{2} = -52 - 3u$

### Solución por aritmética modular

Supongamos la siguiente ecuación diofántica: **$3x+7y=1$**

1. buscamos el *d* = mcd(3, 7). A través del algoritmo de Euclides encontramos que d=1. Como d|C (donde "|" significa "divide a"), es decir, 1|1, 

2. Convertimos la ecuación a una congruencia modular entonces quedaría:

  $3x≡1(mod7)$

3. Calculamos la ecuación usando el inverso modular de:  $3\  mod\  7 = 5$

  *(5)3x≡1(5) (mod7)*

  *14x+x≡5 (mod7)*

  *x≡5 (mod7)*

  **x=7n+5, n∈Z   ∴  x=5**

4. Ya que sabemos que x=5, podemos encontrar el valor de y resolviendo la restante:

  **$3x+7y=1$**
  *3(5)+7y=1*
  *y = -2*

5. Entonces tenemos que d=1, x=5 e y=−2. Podemos obtener la ecuación generalizada:
  > $x = x_0 + u\frac{B}{d} = 5 + u\frac{7}{1} = 5+ 7u$
  > $y = y_0 - u\frac{A}{d} = -2 - u\frac{3}{1} = -2 - 3u$







## Bibliografía

https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_diof%C3%A1ntica

https://w3.ual.es/eventos/OMERSMEALMERIA/GEOMETRIA/Diofanticas.pdf

https://mate.dm.uba.ar/~pdenapo/apuntes-algebraI/2020/2do-cuatrimestre/clase-16-diofanticas.pdf