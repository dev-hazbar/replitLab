# Wilson's Theorem

El test de Wilson es un método determinístico para verificar la primalidad de un número. 

> Se basa en el Teorema de Wilson, que establece que un número $ p > 1 $ es primo si y solo si:
> 
> $(p-1)! \equiv -1 \ (\text{mod} \ p)$

Razones:
- **Determinismo**: Si calculas $ (p-1)! $ y lo reduces módulo $ p $, el resultado es inequívoco y siempre el mismo para un $ p $ dado.
- **Coste computacional**: Aunque es determinístico, su implementación directa no es práctica para números grandes, ya que calcular $ (p-1)! $ tiene un coste factorial, lo que lo hace ineficiente en comparación con otros tests.

En resumen, el test de Wilson es determinístico pero poco eficiente, por lo que rara vez se usa en la práctica.






Así que podemos simplemente calcular $(n-1)! \ (\text{mod} \ n)$ para verificar si $ n $ es primo.

El código sería el siguiente:

```python
def isPrime(n):
    fac = 1
    for i in range(1, n):   # desde 1 hasta n-1
        fac = (fac * i) % n
    return (fac == n-1)     # verdadero si (n-1)! mod n = n-1, es decir, (n-1)! = -1 mod n
```

Sin embargo, esto es absurdamente lento; esto requiere $ O(n) $ multiplicaciones, incluso más lento que la división de prueba mencionada anteriormente. (Esto es comparable a la división de prueba no modificada, verificando hasta $ n-1 $ en lugar de $ n $.)
