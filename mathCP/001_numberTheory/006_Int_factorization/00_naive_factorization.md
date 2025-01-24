# 1. Método Ingenuo (Naive) - O(√n)

**objetivo de factorización:** obtener todos los factores primos de un numero



Este método prueba cada número entero desde 2 hasta √n para determinar si es un factor.



## Pseudocódigo
```
ALGORITMO FactoresNaive(n)
    SI n < 2 DEVOLVER "Sin factores primos"
    INICIALIZAR factores ← []

    PARA d DESDE 2 HASTA √n HACER     # El √n cambia cada vez que n cambia
        MIENTRAS n % d = 0 HACER
            AGREGAR d a factores
            n ← n / d       #

    SI n > 1 AGREGAR n a factores
    DEVOLVER factores
FIN ALGORITMO
```

> La línea $ n \leftarrow \frac{n}{d} $ en el seudocódigo actualiza el valor de $ n $ después de encontrar un divisor $ d $. El propósito es reducir $ n $ dividiendo repetidamente por $ d $ hasta que ya no sea divisible por $ d $. Esto asegura que:
> 
> 1. **Eliminación de factores**: Cada vez que $ d $ divide a $ n $, agregamos $ d $ a la lista de factores y eliminamos ese múltiplo de $ d $ en $ n $.
> 2. **Evitamos repeticiones**: Una vez que $ d $ ya no divide a $ n $, pasamos al siguiente divisor, evitando que se agregue $ d $ múltiples veces más allá de lo necesario.



```python
def naive_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
```




**Características**:

- Complejidad: O(√n)
- Ventajas: Simple y fácil de implementar.
- Desventajas: Ineficiente para números grandes.



### Ejemplo


Hagamos el ejemplo del número $ n = 102 $ utilizando el seudocódigo paso a paso:

**Inicialización:**
- $ n = 102 $
- $ d = 2 $ (iniciamos con el menor divisor primo).
- $ \text{factores} = [] $ (lista vacía para almacenar los factores).

**Iteraciones del bucle:**

- **Divisor $ d = 2 $:**
  - $d$ va desde 2 hasta $\sqrt{102} = 10... \approx 10$
  - $ 102 \% 2 = 0 $ → $ d = 2 $ es un factor.
  - Agregamos 2 a $ \text{factores} $: $ \text{factores} = [2] $.
- Actualizamos $ n \leftarrow 102 / 2 = 51 $.
- **Divisor $ d = 3 $:**
  - $d$ va desde 3 hasta $\sqrt{51} = 7... \approx 7$
  - $ 51 \% 3 = 0 $ → $ d = 3 $ es un factor.
  - Agregamos 3 a $ \text{factores} $: $ \text{factores} = [2, 3] $.
- Actualizamos $ n \leftarrow 51 / 3 = 17 $.
- **Divisor $ d = 4 $:**
  - $d$ va desde 4 hasta $\sqrt{17} = 4... \approx 4$
- $ 17 \% 4 \neq 0 $ → $ d = 4 $ no es un factor.
  - *por lo que este d = 4 es el ultimo valor que se evalúa
- **Divisor $ d = 5, 6, \dots, 10 $:**
  - *ya no se evalúan*

**Finalización:**

- Después del bucle, $ n > 1 $, por lo que $ n = 17 $ es un factor primo.
- Agregamos 17 a $ \text{factores} $: $ \text{factores} = [2, 3, 17] $.

**Resultado:**
Los factores primos de $ 102 $ son:
\[ [2, 3, 17] \]
