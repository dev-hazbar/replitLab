# inverso modular

## **¿Qué es un inverso modular?**

En aritmética modular no tenemos una operación de división. Sin embargo, sí tenemos inversos modulares.

- El inverso modular de A (mod C) es A^-1
- (A * A^-1) ≡ 1 (mod C) o, de manera equivalente, (A * A^-1) mod C = 1
- Solo los primos relativos de C (los números que no comparten factores primos con C) tienen un inverso modular (mod C)

## **¿Cómo encontrar un inverso modular?**

Un método ingenuo de encontrar un inverso modular para A (mod C) es:

**Paso 1.** Calcula A * B mod C b para los valores de B entre 0 y C-1.

**Paso 2.** El inverso modular de A mod C es el valor B que hace que se cumpla A * B mod C = 1.

Observa que el término B mod C solo puede tener un valor entero entre 0 y C-1, así que probar valores mayores de B es redundante.

## **Ejemplo: A=3, C=7**

### Paso 1. Calcula A * B mod C para los valores de B entre 0 y C-1

```
3 * 0 ≡ 0 (mod 7)

3 * 1 ≡ 3 (mod 7)

3 * 2 ≡ 6 (mod 7)

3 * 3 ≡ 9 ≡ 2 (mod 7)

3 * 4 ≡ 12 ≡ 5 (mod 7)

3 * 5 ≡ 15 (mod 7) ≡ 1 (mod 7)  <------ ¡ENCONTRASTE EL INVERSO!

3 * 6 ≡ 18 (mod 7) ≡ 4 (mod 7)
```

### **Paso 2. El inverso modular de A mod C es el valor B que hace A * B mod C = 1**

5 es el inverso modular de 3 mod 7 ya que 5*3 mod 7 = 1.

¡Fácil!

Hagamos un ejemplo más en donde no encontremos un inverso.

## **Ejemplo: A=2 C=6.**

### **Paso 1. Calcula A \* B mod C para los valores de B entre 0 y C-1**
```
2 * 0 ≡ 0 (mod 6)

2 * 1 ≡ 2 (mod 6)

2 * 2 ≡ 4 (mod 6)

2 * 3 ≡ 6 ≡ 0 (mod 6)

2 * 4 ≡ 8 ≡ 2 (mod 6)

2 * 5 ≡ 10 ≡ 4 (mod 6)
```

### **Paso 2. El inverso modular de A mod C es el valor B que hace A \* B mod C = 1**

Ningún valor de B hace que se cumpla A * B mod C = 1. Por lo tanto, A no tiene inverso modular (mod 6).
Esto es porque 2 no es primo relativo de 6 (comparten el factor primo 2).

## **Este método parece lento...**

Hay un método mucho más rápido para encontrar el inverso de A (mod C) que vamos a discutir en los siguientes artículos sobre el algoritmo de Euclides extendido.



## Algoritmo de Euclides

> 
>
> **1.** Algoritmo de euclides
>
> MCD(A,B)=MCD(B, A mod B)=MCD(B,R)
>
> hasta que R=0 *porque*  MCD(N, 0) = N
>
> 
>
> **2.** Otra forma de calcular MCD pero menos optimo
>
> MCD(A,B)=MCD(A,A-B)





```
# Ejemplo:
MCD(270,192) = MCD(192,78) = MCD(78,36) = MCD(36,6) = MCD(6,0) = 6
MCD(270,192) = 6
```

## Algoritmo de Euclides extendido

El algoritmo de Euclides extendido es una herramienta clave para calcular el inverso modular de un número A módulo C. Aquí tienes un resumen del método:

Paso a paso:
Expresar la identidad de Bezout: Utilizando el algoritmo de Euclides, encontramos enteros x y y tales que:

A ⋅ x + C ⋅ y = gcd(A, C)

Si gcd(A, C) = 1, entonces x es el inverso modular de A mod C.

Razonamiento detrás:

Debido a que A ⋅ x ≡ 1 (mod C), esto implica que x es el inverso modular.
Si gcd(A, C) ≠ 1, entonces A no tiene un inverso modular bajo C.

Implementación práctica: En la práctica, puedes usar un proceso iterativo para determinar x y y. Aquí tienes un ejemplo en Python:

```python
def euclides_extendido(a, c):
    r0, r1 = a, c
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

    # Verifica si hay inverso
    if r0 != 1:
        raise ValueError(f"{a} no tiene inverso bajo módulo {c}")
    
    return s0 % c  # Asegúrate de que el resultado esté en el rango [0, C-1]

# Ejemplo
a = 7
c = 26
inverso = euclides_extendido(a, c)
print(f"El inverso de {a} mod {c} es {inverso}")
```

```
Desglosemos el funcionamiento del algoritmo de Euclides extendido utilizando A = 3 y C = 7. Queremos calcular el inverso modular de 3 mod 7.

Variables iniciales:
r0 = 3, r1 = 7: residuos
s0 = 1, s1 = 0: coeficientes asociados a A
t0 = 0, t1 = 1: coeficientes asociados a C

Iteración 1:
Calculamos:
q = ⌊ r0 / r1 ⌋ = ⌊ 3 / 7 ⌋ = 0
Actualizamos:
r0, r1 = r1, r0 − q ⋅ r1 = 7, 3 − 0 ⋅ 7 = 7, 3
s0, s1 = s1, s0 − q ⋅ s1 = 0, 1 − 0 ⋅ 0 = 0, 1
t0, t1 = t1, t0 − q ⋅ t1 = 1, 0 − 0 ⋅ 1 = 1, 0
Estado después de la iteración 1:
r0 = 7, r1 = 3, s0 = 0, s1 = 1, t0 = 1, t1 = 0

Iteración 2:
Calculamos:
q = ⌊ r0 / r1 ⌋ = ⌊ 7 / 3 ⌋ = 2
Actualizamos:
r0, r1 = r1, r0 − q ⋅ r1 = 3, 7 − 2 ⋅ 3 = 3, 1
s0, s1 = s1, s0 − q ⋅ s1 = 1, 0 − 2 ⋅ 1 = 1, −2
t0, t1 = t1, t0 − q ⋅ t1 = 0, 1 − 2 ⋅ 0 = 0, 1
Estado después de la iteración 2:
r0 = 3, r1 = 1, s0 = 1, s1 = −2, t0 = 0, t1 = 1

Iteración 3:
Calculamos:
q = ⌊ r0 / r1 ⌋ = ⌊ 3 / 1 ⌋ = 3
Actualizamos:
r0, r1 = r1, r0 − q ⋅ r1 = 1, 3 − 3 ⋅ 1 = 1, 0
s0, s1 = s1, s0 − q ⋅ s1 = −2, 1 − 3 ⋅ −2 = −2, 7
t0, t1 = t1, t0 − q ⋅ t1 = 1, 0 − 3 ⋅ 1 = 1, −3
Estado después de la iteración 3:
r0 = 1, r1 = 0, s0 = −2, s1 = 7, t0 = 1, t1 = −3

Verificación del inverso:
El bucle termina porque r1 = 0. Verificamos que r0 = 1, lo que confirma que A = 3 tiene un inverso modular bajo C = 7.

El coeficiente s0 = −2 es el inverso modular, pero necesitamos que sea positivo. Ajustamos sumando 7 (el módulo):
s0 mod 7 = −2 + 7 = 5
El inverso modular de 3 mod 7 es 5.

Verificación final:
Multiplicamos:
3 ⋅ 5 = 15 y 15 mod 7 = 1
El resultado es correcto.

```



## Ejercicios





Genera una lista de casos de prueba para un test unitario en formato de texto. Enfócate en casos críticos para el problema, detallando tipos de entrada y valores esperados.

Diseñar una función para encontrar el inverso multiplicativo modular:

Descripción: Dado dos enteros a y n, encuentra el inverso multiplicativo de a módulo n (si existe).
Entrada: Dos enteros a y n donde 1 ≤ a, n ≤ 10^9.
Salida: Un entero que representa el inverso multiplicativo de a módulo n, o null si no existe.
Ejemplo: Entrada: 3 11, Salida: 4.


FORMATO DE RESPUESTA:
Agragale un comentario en el encabezado cada caso de prueba, por cada caso de prueba debe haber 3 tests
entregame la salida en un textbox,
(la entrada y valor esperado esten en una linea por caso)
Inputs: 3 11 -> expected: 4




```python
# Caso de prueba 1: Inverso multiplicativo con módulo primo (donde el inverso siempre existe)
Entrada: 3 7 -> Valor esperado: 5
Entrada: 4 11 -> Valor esperado: 3
Entrada: 5 13 -> Valor esperado: 8
Entrada: 2 17 -> Valor esperado: 9
Entrada: 7 19 -> Valor esperado: 11
Entrada: 9 23 -> Valor esperado: 18
Entrada: 11 29 -> Valor esperado: 8
Entrada: 12 31 -> Valor esperado: 13
Entrada: 13 37 -> Valor esperado: 10
Entrada: 17 41 -> Valor esperado: 35

# Caso de prueba 2: Inverso multiplicativo con módulo compuesto (donde el inverso puede no existir)
Entrada: 3 10 -> Valor esperado: 7
Entrada: 6 15 -> Valor esperado: 11
Entrada: 8 20 -> Valor esperado: null
Entrada: 9 28 -> Valor esperado: 25
Entrada: 4 12 -> Valor esperado: null
Entrada: 5 18 -> Valor esperado: null
Entrada: 7 24 -> Valor esperado: null
Entrada: 10 30 -> Valor esperado: null
Entrada: 12 35 -> Valor esperado: null
Entrada: 14 40 -> Valor esperado: null

# Caso de prueba 3: Casos donde el inverso no existe (a no es coprimo con n)
Entrada: 6 8 -> Valor esperado: null
Entrada: 9 12 -> Valor esperado: null
Entrada: 12 16 -> Valor esperado: null
Entrada: 14 21 -> Valor esperado: null
Entrada: 10 20 -> Valor esperado: null
Entrada: 15 25 -> Valor esperado: null
Entrada: 18 27 -> Valor esperado: null
Entrada: 20 30 -> Valor esperado: null
Entrada: 24 36 -> Valor esperado: null
Entrada: 25 35 -> Valor esperado: null
```