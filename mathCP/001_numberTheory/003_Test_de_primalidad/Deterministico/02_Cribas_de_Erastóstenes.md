# **La Criba de Eratóstenes**

La Criba de Eratóstenes es un algoritmo eficiente para encontrar todos los números primos menores o iguales a un número dado $ n $. Se basa en eliminar múltiplos de números primos desde 2 en adelante.



**Pasos del Algoritmo:**

1. Crear una lista de números desde 2 hasta $ n $.
2. Inicializar un marcador para todos los números como "posiblemente primos".
3. Para cada número $ p $ en la lista, comenzar con $ p = 2 $:
   - Marcar como no primos todos los múltiplos de $ p $ mayores o iguales a $ p^2 $.
4. Avanzar al siguiente número que no esté marcado como no primo.
5. Los números que permanecen sin marcar son primos.



**Pseudocódigo**

```
1. Crear una lista `es_primo` de tamaño n+1, inicializada en True.
2. Asignar `es_primo[0]` y `es_primo[1]` a False (0 y 1 no son primos).
3. Para p desde 2 hasta sqrt(n):
       Si es_primo[p] es True:
           Marcar todos los múltiplos de p como False desde p^2 hasta n.
4. Retornar los índices de los valores que son True en es_primo.

```

```python
def criba_eratostenes(n):
    if n < 2:
        return []  # No hay primos menores a 2

    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos

    for p in range(2, int(n**0.5) + 1):
        if es_primo[p]:  # Si p es primo
            for multiple in range(p * p, n + 1, p):
                es_primo[multiple] = False

    # Retornar los números primos
    return [i for i, primo in enumerate(es_primo) if primo]

# Ejemplo
limite = 30
primos = criba_eratostenes(limite)
print(f"Primos menores o iguales a {limite}: {primos}")

```

**ejemplo**

```
Primos menores o iguales a 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Complejidad**

- **Tiempo:**
  $ O(n \log(\log(n))) $, debido a que marcamos múltiplos de cada primo.

- **Espacio:**
  $ O(n) $, porque almacenamos un arreglo de tamaño $ n+1 $.

---

**Ventajas:**
- Muy eficiente para encontrar todos los primos hasta un límite dado.
- Fácil de implementar y optimizar.

**Desventajas:**
- Requiere memoria proporcional a $ n $, lo que puede ser un problema para valores muy grandes.
- No está diseñado para probar la primalidad de un único número grande.
