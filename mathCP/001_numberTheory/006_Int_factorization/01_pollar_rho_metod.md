# factorización método de Pollar Rho





#### Algorithm

> According to the Pollard Rho algorithm, the polynomial method $g(x)=(x^2-1)\ mod\  N$ but currently we are using $g(x)=(x^2+1)\ mod\  N$. It will give output as a trivial factor or no factor will be returned.
> 
> **Step 1:** Start with x=2 and take y=x
> **Step 2:** Check if it is divisible by 2 then return 2, otherwise go to step 3
> **Step 3:** Loop until you get a divisor
> **Step 4:** Update x with g(x) and update y with g(g(y))
> **Step 5:** Calculate GCD for modulo of (x-y) and N.
> If GCD of both number is not N then GCD is our factor otherwise *go to step 3*






## Algoritmo de Factorización de Pollard Rho

La factorización de Pollard Rho es un algoritmo heurístico eficiente para encontrar factores no triviales de un número entero compuesto $ n $. Es particularmente útil para números que tienen factores pequeños o medianos. Utiliza técnicas de teoría de números y funciones iterativas para detectar ciclos en un gráfico implícito de residuos modulares.

**Idea Principal**
El algoritmo genera una secuencia pseudoaleatoria $ x_1, x_2, x_3, \dots $ definida por una función iterativa $ f(x) $, y busca un ciclo en esta secuencia utilizando el algoritmo del "*tortuga y liebre*" de Floyd para detección de ciclos.

Cuando se encuentra un ciclo, se calcula el máximo común divisor $ \text{gcd} $ entre las diferencias de algunos términos de la secuencia y $ n $. Este valor es un factor no trivial de $ n $, si existe.

**Pasos del Algoritmo**

- Definir la función iterativa Una función común es
    $
    f(x) = (x^2 + c) \mod n,
    $
    donde $ c $ es una constante pequeña ($ c = 1 $ o $ c = -1 $ son valores típicos).

- Inicializar las variables
    $
    x \leftarrow \text{valor inicial} \quad (\text{normalmente } x = 2),
    $
    $
    y \leftarrow x \quad (\text{para el método tortuga y liebre}),
    $
    $
    d \leftarrow 1 \quad (\text{el divisor común inicial}).
    $

- Iterar hasta encontrar un factor no trivial Mientras $ d = 1 $:

   Actualiza las secuencias:
  $
  x \leftarrow f(x),
  $
  $
  y \leftarrow f(f(y)),
  $
  Calcula:
  $
  d = \text{gcd}(\lvert x - y \rvert, n).
  $

- Verificar el resultado

  Si $ d = n $, la iteración falló, prueba otra función $ f(x) $ o un valor inicial diferente.
  Si $ d > 1 $ y $ d < n $, entonces $ d $ es un factor no trivial de $ n $.



**Ventajas y Limitaciones del Algoritmo de Pollard Rho**

Ventajas

  - Es sencillo de implementar.
  - Es eficiente para factores pequeños y medianos, especialmente en números semiprimos.


Limitaciones

  - No es eficiente para números compuestos con factores grandes.
  - No garantiza la factorización completa en una sola ejecución; puede requerir varios intentos con distintas funciones o valores iniciales.



## **Ejemplo**

### Letra rho

*(secuencia de elementos de la función)*

Supongamos que tenemos la ecuación F(x)= x² mod n. Siendo n el número que queramos factorizar.



Veamos un ejemplo para n=323, empezando por ejemplo con x=2.



F(2) = 2² mod 323 = 4

F(4) = 4² mod 323 = 16

F(16) = 16² mod 323 = 256

F(256) = 256² mod 323 = 290

F(290) = 290² mod 323 = 120

F(120) = 120² mod 323 = 188

F(188) = 188² mod 323 = 137

F(137) = 137² mod 323 = 35

F(35) = 35² mod 323 = 256

F(256) = 16² mod 323 = 290

F(290) = 290² mod 323 = 120



Como se ve marcado en rojo, a partir de F(35) los resultados empiezan a repetirse, entrando en un ciclo.



Si representamos en un dibujo los resultados obtenidos vemos que su forma es similar al de la letra griega rho. Lo que da nombre al algoritmo.



### Solución

Sabiendo F(x) = x² mod n, calcularemos, x = F(x), y = F(F(y)) y por último d = mcd(lx-yl, n). Sí d=1 se siguiremos el cálculo con los nuevos valores dados, en cambio, sí d=1 el valor de d sera un factor de n



Veamos un ejemplo para n=323, empezando por ejemplo con x=2 y=2



x = F(2) = 2² mod 323 = 4

y = F(F(2)) = (2²)² mod 323 = 16

d = mcd(l4-16l, 323) = 1



x = F(4) = 4² mod 323 = 16

y = F(F(16)) = (16²)² mod 323 = 290

d = mcd(l16-290l, 323) = 1



x = F(16) = 16² mod 323 = 256

y = F(F(290)) = (290²)² mod 323 = 188

d = mcd(l256-188l, 323) = 1



x = F(256) = 256² mod 323 = 290

y = F(F(188)) = (188²)² mod 323 = 35

d = mcd(l256-188l, 323) = 1



x = F(290) = 290² mod 323 = 188

y = F(F(35)) = (35²)² mod 323 = 290

d = mcd(l188-290l, 323) = 17



Por lo tanto 17 es un factor


## observaciones

### Factorización Completa con el Algoritmo de Pollard Rho

*El algoritmo de Pollard Rho está diseñado para encontrar un único factor no trivial* de un número compuesto $ n $ en una ejecución. Sin embargo, una vez que se encuentra un factor $ p $, podemos reducir el problema dividiendo $ n $ por $ p $ y repitiendo el proceso para factorizar completamente $ n $.

Pasos para Factorizar Completamente $ n $ con Pollard Rho

  - Ejecutar Pollard Rho para encontrar un factor $ p $ de $ n $.
  - Dividir $ n $ por $ p $: Esto da dos partes: $ p $ y $ n/p $.
  - Repetir Pollard Rho en $ n/p $ (si sigue siendo compuesto) hasta obtener solo números primos.


Ejemplo
Factoricemos $ n = 8051 $ con Pollard Rho:

  - El algoritmo encuentra un factor $ p = 97 $.
  - Dividimos $ n $ por $ p $: $ n/p = 8051/97 = 83 $.
  - $ 83 $ es primo, por lo que la factorización completa de $ 8051 $ es $ 97 \times 83 $.

Consideraciones

  - Repeticiones necesarias: Si $ n $ tiene varios factores, el algoritmo debe ejecutarse múltiples veces hasta que todos los factores sean primos.
  - Factores repetidos: Si $ n $ tiene potencias de un mismo factor primo ($ n = p^k $), el algoritmo puede tardar más en encontrar todos los factores. Sin embargo, generalmente se recomienda dividir $ n $ iterativamente por $ p $ hasta que no sea divisible.
  - Números primos: Si $ n $ es primo, el algoritmo no encontrará ningún factor no trivial (el GCD siempre será $ n $).





### Condiciones de Terminación del Algoritmo de Pollard Rho

El algoritmo de Pollard Rho termina cuando se cumple una de las siguientes condiciones:

1. Se Encuentra un Factor No Trivial
Durante las iteraciones, el algoritmo calcula el máximo común divisor (GCD) entre la diferencia de dos valores $ |x - y| $ y el número $ n $. Si el GCD es mayor que 1 y menor que $ n $, se ha encontrado un factor no trivial $ d $.
$
d = \text{GCD}(|x - y|, n), \quad \text{con} \ 1 < d < n.
$

2. El Número $ n $ es Primo
Si $ d = n $, significa que el algoritmo no pudo encontrar factores porque $ n $ es primo. En este caso, el algoritmo termina sin éxito en encontrar divisores.

3. Se Alcanza un Ciclo Repetitivo
El algoritmo utiliza la estrategia de "tortuga y liebre" para detectar ciclos en la secuencia generada por la función iterativa
$
f(x) = (x^2 + c) \mod n.
$
Si la secuencia entra en un ciclo sin encontrar un factor, el proceso debe reiniciarse con una nueva función o un valor inicial diferente.

4. Se Supera un Límite de Iteraciones
En la práctica, para evitar ejecuciones infinitas o ciclos improductivos, se establece un límite de iteraciones. Si no se encuentra un factor dentro de este límite, se puede cambiar la función $ f(x) $ o el valor inicial $ x_0 $, y volver a ejecutar el algoritmo.

Resumen de las Posibles Terminaciones

  - Factor encontrado: $ 1 < d < n $.
  - Número primo: $ d = n $.
  - Reinicio: Ciclo repetitivo detectado.
  - Límite de iteraciones alcanzado: Control práctico.



## Algoritmo del Conejo y la Liebre de Floyd

El algoritmo del conejo y la liebre de Floyd (o "Floyd's Cycle-Finding Algorithm") se utiliza para detectar ciclos en estructuras iterativas, como listas enlazadas o secuencias generadas por una función. Su ventaja principal es que es eficiente en espacio, utilizando solo dos punteros.

Idea Principal
El algoritmo utiliza dos punteros:

  - Liebre (fast): Se mueve dos pasos a la vez.
  - Conejo (slow): Se mueve un paso a la vez.


Si hay un ciclo, los dos punteros eventualmente se encontrarán dentro del ciclo. Si no hay ciclo, el puntero rápido alcanzará el final de la estructura.

Pasos del Algoritmo

Inicialización:
Coloca ambos punteros al inicio de la estructura.

Fase de Detección de Ciclo:

  - Mueve el puntero lento un paso y el rápido dos pasos.
  - Si en algún momento los dos punteros se encuentran, hay un ciclo.
  - Si el puntero rápido llega al final (o apunta a null en una lista enlazada), no hay ciclo.


Fase de Localización del Ciclo (Opcional):

  - Si se detecta un ciclo, reinicia uno de los punteros al inicio.
  - Mueve ambos punteros un paso a la vez.
  - El punto donde se encuentran nuevamente es el inicio del ciclo.



Explicación Visual del Algoritmo de la Liebre y el Conejo de Floyd}

1. Sin Ciclo
  En este caso, el puntero rápido llegará al final de la lista antes de alcanzar al puntero lento. Esto indica que no existe un ciclo.

2. Con Ciclo
  Cuando existe un ciclo, los punteros lento y rápido comienzan a dar vueltas dentro del ciclo. Al moverse a diferentes velocidades, eventualmente se cruzan.

3. Inicio del Ciclo
  La distancia entre el punto de inicio y el inicio del ciclo es igual a la distancia recorrida por el puntero lento desde la intersección hasta el inicio del ciclo.

Complejidad

  Tiempo: $ O(n) $, donde $ n $ es el número de nodos en la lista (o el período del ciclo en una secuencia).
  Espacio: $ O(1) $, ya que solo utiliza dos punteros.


Este algoritmo es ampliamente utilizado en problemas que implican estructuras repetitivas, como detectar bucles en listas enlazadas o analizar secuencias matemáticas.
