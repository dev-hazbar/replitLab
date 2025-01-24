
# Algoritmo de Euclides Extendido

El algoritmo de Euclides no sólo sirve para encontrar el máximo común divisor de dos números, sino que también nos indica que el *mcd* se puede expresar como combinación lineal de los mismos. 

- Además, el *mcd* es el menor entero positivo en que estos dos números se pueden usar como combinación lineal. 

- Lo que buscamos con el algoritmo extendido de Euclides, son los coeficientes de esta combinación lineal.

>  Esta propiedad resulta de gran utilidad, sobre todo al momento de resolver ecuaciones Diofantinas (ecuaciones de la forma *ax* + *by* = *c*, donde todos son enteros y *a*, *b* y *c* son constantes).

> Otra aplicación útil es  cuando ocurre que: *a* y *b* son primos relativos (por lo que *c* = 1), entonces *x* es el inverso multiplicativo de *a* módulo *b*. Por ejemplo, para 5*x* + 3*y* = 1, una solución es 5(-1) + 3(2) = 1, y tenemos que 5(-1) ≡ 1 mod 3 y 3(2) ≡ 1 mod 5.

Para encontrar los valores de *x* e *y*, consideremos lo siguiente. Expresando el *mcd* como combinación lineal de las entradas, implica que *c* = *mcd*:
	*mcd(a,b) = ax + by*
También sabemos que:
	*mcd(a,b) = mcd(b, a mod b)*
Si hacemos que **$a_1 = a, b_1 = b,\ a_2 = b$ y $b_2 = (a\ mod\ b) = a -bk$** , donde *k* es entero, entonces:
	*mcd(a1, b1) = mcd(a2, b2)*
Reemplazando en la primera ecuación tenemos:
*$mcd(a1, b1) = a_1x_1 + b_1y_1$*
*$mcd(a2, b2) = a_2x_2 + b_2y_2$*
*…*
*$mcd(an, bn) = a_nx_n + b_ny_n$*
Si hacemos *mcd*(*a*,*b*) = *d*, y suponiendo que tenemos dos iteraciones además de los valores de *x* e *y* para la segunda ($x_2, y_2$):
*$mcd(a1, b1) = a_1x_1 + b_1y_1$* = *d*
*$mcd(a2, b2) = a_2x_2 + b_2y_2$* = *d*

Sabemos que **$a_2 = b_1,\ b_2 = a_1 -b_1k $ y $ k = \lfloor \frac{a1}{b1} \rfloor$,** por lo que:
*$d = a_1x_1 + b_1y_1$*
*$d = a_2x_2 + b_2y_2 = b_1x_2 + (a_1 -b_1k)y_2$*

Uniendo las dos ecuaciones:
*$a_1x_1 + b_1y_1= b_1x_2 + (a_1 -b_1k)y_2$*

rescribiendo la ecuación: 
**$a_1x_1 + b_1y_1= a_1y_2 + b_1(x_2 -ky_2)$**
Lo anterior se cumple si:
$x_1 = y_2$
$y_1 = x_2 -ky_2 = x_2 - \lfloor \frac{a1}{b1} \rfloor y_2 $
Con esto, podemos calcular los valores de x e y en base a lo anteriores. Ahora sólo necesitamos obtener cuales son los valores iniciales.

> **Sabemos que en la última iteración $a_n= d$ y $b_n = 0$, entonces nos queda que:**
> $mcd(a_n, b_n) = a_nx_n + b_ny_n$
> $d = dx_n + 0y_n$
> $x_n = 1, y_n = 0$



Casos ejemplo: las salidas estan dara de la siguiente manera: **x, y, MCD(a,b)**



| Entrada:    | 25 58                                                        |
| ----------- | ------------------------------------------------------------ |
| Desarrollo: | mcd(58, 25 mod 58)<br>mcd(58,25) = mcd(25, 58 mod 25)<br>mcd(25, 8) = mcd( 8, 25 mod  8)<br>mcd( 8, 1) = mcd( 1,  8 mod  1)<br>mcd( 1, 0) = 1<br><br>        x=  1, y=  0<br> 8  1; x=  0, y=  1 –( 8/ 1)×0 = 1, d= 1<br>25  8; x=  1, y=  0 –(25/ 8)×1 =-3, d= 1<br>58 25; x= -3, y=  1 –(58/25)×-3= 7, d= 1<br>25 58; x=  7, y= -3 –(25/58)×7 =-3, d= 1<br> |
| Salida:     | 7 –3 1                                                       |



| Entrada:    | 4 6                                                          |
| ----------- | ------------------------------------------------------------ |
| Desarrollo: | mcd( 4, 6)= mcd( 6, 4 mod 6)<br>mcd( 6, 4)= mcd( 4, 6 mod 4)<br>mcd( 4, 2)= mcd( 2, 4 mod 2)<br>mcd( 2, 0)= 2<br><br>     x=  1, y=  0<br>2 4; x=  0, y=  1 -(2/4)×0 = 1, d= 1<br>2 4; x=  1, y=  0 -(6/4)×1 =-1, d= 1<br><br>4 6; x= -1, y=  1 –(4/6)×-1= 1, d= 1<br> |
| Salida:     | -1 1 1                                                       |



| Entrada:    | 17 17                                                        |
| ----------- | ------------------------------------------------------------ |
| Desarrollo: | mcd(17,17) = mcd(17, 17 mod 17)<br>mcd(17, 0) = 17<br><br>       x=  1, y=  0<br>17 17; x=  0, y=  1 –(17/17)×0 = 1, d= 1<br>Salida:	0 1 17<br> |
| Salida:     | 0 1 17                                                       |







Entrada:	17 17

mcd(17,17) = mcd(17, 17 mod 17)<br>mcd(17, 0) = 17<br><br>       x=  1, y=  0<br>17 17; x=  0, y=  1 –(17/17)×0 = 1, d= 1<br>Salida:	0 1 17<br>