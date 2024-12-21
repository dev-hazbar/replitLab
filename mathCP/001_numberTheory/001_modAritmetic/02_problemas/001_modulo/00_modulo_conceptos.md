## Concepto Básico del Módulo:

En términos generales, para un número a y un divisor n, el resultado de a mod n es el residuo de la división de a por n. Este residuo es un número que satisface:

### Teorema del residuo y el cociente

```
a = qn + r
```
donde q es el cociente, r es el residuo, y 0 ≤ r < n.

### Calculo de residuo
```
r = a - b * FUNCION_PISO(a/b)
```

```python
1. Signo del residuo:
El residuo tiene el mismo signo que el divisor "n"

2. Rango de valores de r:
- Si n > 0: r toma valores en el rango 0 ≤ r < n.
- Si n < 0: r toma valores en el rango n < r ≤ 0.
```

## Manejo de Signos en el Módulo:

```
Caso 1: Número positivo
Si a es positivo, a mod n es simplemente el residuo de dividir a por n. Por ejemplo:

6 mod 5 = 1
Aquí, 6 = 1 × 5 + 1, así que el residuo es 1.
```



```
Caso 2: Número negativo
Si a es negativo, el proceso es similar pero debemos ajustar para obtener un residuo positivo. Por ejemplo:

-6 mod 5

Dividimos -6 entre 5:

-6 ÷ 5 = -1.2

Redondeamos hacia el menor entero (hacia abajo) utilizando la función piso:

-2

Calculamos el producto del cociente redondeado por el divisor:

-2 × 5 = -10

Encontramos la diferencia:

-6 - (-10) = -6 + 10 = 4

Por lo tanto:

-6 mod 5 = 4
```

```
Caso 3: divisor negativo
Si a es positivo y n es negativo, el proceso es similar:

6 mod -5

Dividimos -6 entre 5:

6 ÷ -5 = -1.2

Redondeamos hacia el menor entero (hacia abajo) utilizando la función piso:

-2

Calculamos el producto del cociente redondeado por el divisor:

-2 × -5 = 10

Encontramos la diferencia:

6 - (10) = 6 - 10 = -4

Por lo tanto:

6 mod -5 = -4
```

```
Caso 4: divisor negativo
Si a es negativo y n es negativo, el proceso es similar:

-6 mod -5

Dividimos -6 entre -5:

-6 ÷ -5 = 1.2

Redondeamos hacia el menor entero (hacia abajo) utilizando la función piso:

1

Calculamos el producto del cociente redondeado por el divisor:

1 × -5 = -5

Encontramos la diferencia:

-6 - (-5) = -6 + 5 = -1

Por lo tanto:

-6 mod -5 = -1
```
