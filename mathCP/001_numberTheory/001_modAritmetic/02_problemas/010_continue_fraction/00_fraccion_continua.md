# Fracción Continua

Las fracciones continuas son expresiones matemáticas que representan números a través de una secuencia de cocientes y divisores, de la forma:

$$
x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + \dots}}}
$$
Donde x se puede expresar usando un array denominado **expansión de fracción continua**: $$[a_0; a_1, a_2, a_3, \dots, a_n]$$

Donde:

> $a_0$ es la parte entera del número.
> $a_1$, $a_2$, $a_3$, … son números enteros positivos llamados coeficientes de la fracción continua.

**Propiedades principales**
`Números racionales`: Pueden representarse como fracciones continuas finitas. Ejemplo:

7/3 = 2 + 1/3 o como [2;3]

`Números irracionales`: Se representan mediante fracciones continuas infinitas y periódicas o no periódicas. Ejemplo:

La raíz cuadrada de un número entero no cuadrado genera una fracción continua periódica:
√2 = [1;2,2,2,…]

`Convergentes`: Cada truncamiento de la fracción continua da una aproximación racional al número, llamada convergente.

Ejemplo para π = [3;7,15,1,292,…]:

π ≈ 3 + 1/7 = 22/7

**Aplicaciones**

- Aproximación de números irracionales: Son útiles para encontrar aproximaciones racionales precisas.
- Teoría de números: Se emplean en problemas de ecuaciones diofánticas.
- Criptografía: Aplicadas en algoritmos como RSA.

## convertir un racional a fracción continua

- **Paso1**: El número se separa en parte entera y decimal.
- **Paso2**: Si la parte decimal es distinta de cero, se calcula la inversa de esa parte decimal y se repite el proceso con el resultado.

$$
\frac{98}{35} = 2 + \frac{28}{35} = 2 + \frac{1}{\frac{35}{28}} = 2 + \frac{1}{1+\frac{7}{28}} = 2 + \frac{1}{1+\frac{1}{\frac{28}{7}}} = 2 + \frac{1}{1+\frac{1}{4}}
$$

La expansión de fracción continua: 98/35 es [2;1,4]



### usando algoritmo de Euclides

convertir 98/35

|                          | **Cociente** | **Resto** |
| ------------------------ | ------------ | --------- |
| **División 98 entre 35** | 2            | 28        |
| **División 35 entre 28** | 1            | 7         |
| **División 28 entre 7**  | 4            | 0         |

Así, además de obtener que el MCD de 98 y 35 es 7, obtenemos de nuevo los ya conocidos cocientes incompletos 2, 1 y 4 de la fracción c

La expansión de fracción continua: 98/35 es [2;1,4]



## convertir un decimal a Fracción continua

- **Paso1**: El número se separa en parte entera y decimal.
- **Paso2**: Si aun hay decimales, se calcula la inversa de esa parte decimal y se repite el proceso con el resultado.

```
π=3.141592...
ITERACIÓN 1
paso1: π=3 + 0.141592...
paso2: inverso del decimal     1/0.141592... = 7.062513...

ITERACIÓN 2
paso1:  7 + 0.062513...
paso2: 1/0.062513... = 15.9965...

```

$$
\pi = [3; 7, 15, 1, 292, \dots]
$$





![conversion de pi](https://lemnismath.org/wp-content/uploads/2022/03/web-pi_3.gif|----)



## convertir numero irracional a Fracción continua



Los números irracionales tienen fracciones continuas infinitas y periódicas o no periódicas.

Procedimiento:

- **Paso1** *Obtén la parte entera*: Sea 𝑥 el número. Define 𝑎₀ = ⌊𝑥⌋.
- **Paso2** Calcula la parte fraccionaria: Define 𝑥₁ = 1 / (𝑥 − 𝑎₀), y repite.
- **Paso3** Continúa iterando: Cada 𝑥ₙ produce un nuevo 𝑎ₙ = ⌊𝑥ₙ⌋.

Ejemplo:
Para √2:

√2 = 1.414 ⟹ 𝑎₀ = 1, 𝑥₁ = 1 / (√2 − 1) = 2.414 ⟹ 𝑎₁ = 2, 𝑥₂ = 1 / (2.414 − 2) = 2.414 ⟹ 𝑎₂ = 2, ...
$$
\sqrt{2} = 1.414 \quad \Rightarrow \quad a_0 = 1, \quad x_1 = \frac{1}{\sqrt{2} - 1}= \sqrt{2} + 1 = 2.414
$$

$$
x_1 = 2.414\quad \Rightarrow \quad a_1 = 2, \quad x_2 = \frac{1}{\sqrt{2} +1 -2} = \sqrt{2} + 1  = 2.414 \quad \Rightarrow \quad a_2 = 2, \dots
$$



Fracción continua periódica: [1; 2, 2, 2, ...]



### **Demostración de lo anterior**

Sabemos que $\sqrt{2}$ está entre uno y dos.

Sea entonces *y* tal que $\sqrt{2} = 1 + \frac{1}{y}$                                                    [1].

Despejando, tenemos que $y= \frac{1}{\sqrt{2}-1}$  racionalizando $y= {1+\sqrt{2}}$             [2]

remplazamos $\sqrt{2}$ en función de $y$ Entoces: $y= {1+\sqrt{2}} = {1+\sqrt{2} =1 + 1 + \frac{1}{y}} =2 + \frac{1}{y}$             [2]

Sustituyendo [2] en [1] se tiene que
$$
\sqrt{2} = 1 + \frac{1}{ 2 + \frac{1}{y}}
$$
Repitiendo la sustitución hasta el infinito
$$
\sqrt{2} = 1 + \frac{1}{ 2 + \frac{1}{ 2 + \frac{1}{ 2 + \frac{1}{...}}}}
$$
Fracción continua periódica: [1; 2, 2, 2, ...]





`Cálculo de la fracción continua de`  $\sqrt{5} $

1. Definimos el número: $x = \sqrt{5}.$


2. Elevamos al cuadrado: $x^2 = 5.$
3. Construcción de la diferencia de cuadrados:
$x^2 - 4 = 5 - 4 = 1.$
Por lo tanto, tenemos:
$x^2 -4 =  1.$
$(x+2)(x-2)=  1.$


4. Despejando \( x \):

$x = 2 + \frac{1}{2 + x}$

5. sustitución iterativa de x:
   $$
   x =2 + \frac{1}{2 + x} = 2 + \frac{1}{2 + 2 + \frac{1}{2 + x}}= 2 + \frac{1}{4 + \frac{1}{2 + x}}= 2 + \frac{1}{4 + \frac{1}{2 + 2 + \frac{1}{2 + x}}} = 2 + \frac{1}{4 + \frac{1}{4 + \frac{1}{2 + x}}}\\

   =  2 + \frac{1}{4 + \frac{1}{4 + \frac{1}{4 + \frac{1}{...}}}}
   $$

6. $\sqrt{5} = [2;4,4,4,...]$



`ϕ (Sección áurea)`: $\frac{\sqrt{5}+1}{2}$


1. Definimos el número:

   $x = \frac{\sqrt{5} + 1}{2}.$

   $2x -1 = \sqrt{5}$

2. Elevamos al cuadrado:

	$(2x -1)^2 = (\sqrt{5})^2$

	Expandimos el numerador:

	$5=4x^2−4x−4$

	simplificamos:

	$x^2−x−1=0$

	factorizamos:

	$x(x−1)=1$

	despejamos una x

	$x=1+\frac{1}{x}$


3. Remplazos iterativos en función de x:
   $$
   x=1+\frac{1}{x} = 1+\frac{1}{1+\frac{1}{x}} = 1+\frac{1}{1+\frac{1}{1+\frac{1}{x}}}= 1+\frac{1}{1+\frac{1}{1+\frac{1}{1+\frac{1}{...}}}}
   $$


4. $\frac{\sqrt{5}+1}{2} = [1;1,1,1,1,...]$





## Calculo de convergencias

Truncando la fracción continua de un número *x = A/B* en puntos sucesivos de su desarrollo, obtenemos aproximaciones racionales *Pk/Qk* de *x* denominadas sus *convergentes*:
$$
\frac{A}{B} = [a_1, a_2, a_3,...,a_n]\\
\frac{P_1}{P_1} = [a_1] = \frac{1}{a_1}\\
\frac{P_2}{P_2} = [a_1,a_2] = \frac{1}{a_1 + \frac{1}{a_2}}\\
\frac{P_3}{P_3} = [a_1,a_2,a_3] = \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3} }}\\
$$

Los convergentes tienen la siguiente propiedad importante [Kapp]: **cada convergente Pk/Qk **es la mejor aproximación racional del número \*x\* con denominador no superior a **Qk**. Calculemos los convergentes en el ejemplo previo:

![](https://www.sacred-geometry.es/sg/sites/default/files/images/CFE_Compact_VS_Extended.png)



Según la propiedad anterior, 2/5 = 0.4 es la mejor aproximación racional posible de 5/12 = 0.4166666 con denominador no superior a 5 (error=4%). Puede apreciarse que la representación "expandida" de la fracción continua (la que termina en un 1) proporciona un convergente extra, 3/7 = 0.42857143. Esta es la mejor aproximación racional posible de 5/12 con denominador no superior a 7 (error=2.8%). Se observa pues que *utilizando la representación "compacta" de una fracción continua "se esconde" uno de los convergentes de la expansión*. Por lo tanto, resulta preferible trabajar con la representación "extendida" equivalente terminada en 1.



A medida que añadimos más índices al convergente, su cálculo directo se vuelve más y más complicado. Sin embargo, existe un método iterativo que nos permite calcular un convergente dado a partir de los dos precedentes [Kapp]. 

- Para inicializar el proceso necesitamos calcular P1/Q1, para el cual no existen convergentes previos; en este caso asumimos las condiciones iniciales **P-1/Q-1 = 1/0 y P0/Q0=0/1**. El proceso a seguir puede expresarse en forma de tabla como sigue:



![](https://www.sacred-geometry.es/sg/sites/default/files/images/CFE_Convergents_Algorism.png)



Ahora comprobemos como este algoritmo efectivamente proporciona los convergentes esperados para la representación en fracción continua "extendida" [2,2,1,1] de 5/12:

![](https://www.sacred-geometry.es/sg/sites/default/files/images/CFE_Convergents_Algorithm_example.png)








## Bibliografía

- [www.epsilones.com - fracciones-continuas](https://www.epsilones.com/paginas/articulos/articulos-110-fracciones-continuas.html)
- [es.wikipedia.org - fracciones_continua](https://es.wikipedia.org/wiki/Fracci%C3%B3n_continua)
- [lemnismath.org - fracciones-continuas-mejor-aproximacion](https://lemnismath.org/2022/05/fracciones-continuas-mejor-aproximacion/)
- [www.sacred-geometry.es - racciones-continuas](https://www.sacred-geometry.es/?q=es/content/fracciones-continuas)
- [euler.us.es - fracciones](https://euler.us.es/~orthonet/orthonet16/notas/fracciones.pdf)