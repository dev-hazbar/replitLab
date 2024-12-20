

# Exponenciación modular


Por último, exploremos la **propiedad de la potenciación**:

> A^B mod C = ( (A mod C)^B ) mod C


## problema de exponenciación

A menudo queremos calcular **A^B mod C** para *valores grandes de B*.
Desafortunadamente, **A^B** se vuelve muy grande incluso para valores modestos de **B**.

`Por exjemplo:`

**2^90** = 1,237,940,039,290,000,000,000,000,000

**7^256** = 2,213,595,400,050,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 83,794,038,078,300,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000 721,264,246,243,000,000,000,000,000

Estos valores tan grandes causan que nuestras calculadoras y computadoras den un mensaje de **error (overflow)**.
Incluso aunque no lo hicieran, tomaría *mucho tiempo* encontrar el módulo de estos números tan largos de manera directa.

### ¿Qué podemos hacer para reducir el tamaño de los términos involucrados y hacer nuestro cálculo más rápido?

Supongamos que queremos calcular **2^90 mod 13**, pero tenemos una calculadora que no puede trabajar con números **más grandes que 2^50**.

Aquí esta una estrategia sencilla de **divide y vencerás**:

```
- Crear partes más pequeñas utilizando reglas de los exponentes:

2^90 = 2^50 * 2^40

- Aplicando módulo C a cada parte:

2^50 mod 13 = 1125899906842624 mod 13 = 4
2^40 mod 13 = 1099511627776 mod 13 = 3

- Aplicando propiedades de la multiplicación a cada partes:

2^90 mod 13 = (2^50 \* 2^40) mod 13
2^90 mod 13 = (2^50 mod 13 * 2^40 mod 13) mod 13
2^90 mod 13 = ( 4 * 3 ) mod 13
2^90 mod 13 = 12 mod 13
2^90 mod 13 = 12
```

### ¿Cómo podemos calcular A^B mod C rápidamente si B es una potencia de 2?

¿Cómo podríamos calcular **7^256 mod 13** al usar una calculadora que no pueda trabajar con números más grandes que **7^10** ?

Podríamos dividir **7^256** en *25 partes* de **7^10** y *1 parte* de **7^6**, pero esto no sería muy eficiente.

Hay una mejor manera....











## Exponenciación modular rápida



### ¿Cómo podemos calcular A^B mod C rápidamente si B es una potencia de 2?

Usando las reglas de la multiplicación modular:

```python
es decir, A^2 mod C = (A * A) mod C = ((A mod C) * (A mod C)) mod C

Podemos usar esto para calcular 7^256 mod 13 rápidamente:

7^1 mod 13 = 7
7^2 mod 13 = (7^1 *7^1) mod 13 = (7^1 mod 13 * 7^1 mod 13) mod 13

Podemos *sustituir* nuestro resultado anterior por 7^1 mod 13 en esta ecuación.

7^2 mod 13 = (7 *7) mod 13 = 49 mod 13 = 10
7^2 mod 13 = 10

7^4 mod 13 = (7^2 *7^2) mod 13 = (7^2 mod 13 * 7^2 mod 13) mod 13

Podemos *sustituir* nuestro resultado anterior por 7^2 mod 13 en esta ecuación.

7^4 mod 13 = (10 * 10) mod 13 = 100 mod 13 = 9
7^4 mod 13 = 9

7^8 mod 13 = (7^4 * 7^4) mod 13 = (7^4 mod 13 * 7^4 mod 13) mod 13

Podemos *sustituir* nuestro resultado anterior por 7^4 mod 13 en esta ecuación.

7^8 mod 13 = (9 * 9) mod 13 = 81 mod 13 = 3
7^8 mod 13 = 3

Continuamos de esta manera, sustituyendo resultados anteriores en nuestras ecuaciones.

... después de 5 iteraciones llegamos a:

7^256 mod 13 = (7^128 * 7^128) mod 13 = (7^128 mod 13 * 7^128 mod 13) mod 13
7^256 mod 13 = (3 * 3) mod 13 = 9 mod 13 = 9
7^256 mod 13 = 9
```

Esto nos da un método para calcular **A^B mod C** rápidamente siempre y cuando **B sea una potencia de 2**.

Sin embargo, también necesitamos un método para una exponenciación modular rápida cuando **B no sea una potencia de 2**.

### ¿Cómo podemos calcular A^B mod C rápidamente para cualquier B?

![img](https://cdn.kastatic.org/ka-perseus-images/348688d0406ce0c0986251993dc9a8451bbe0e2c.jpg)

#### Paso 1: divide B en potencias de 2 al escribirlo en binario:

![img](https://cdn.kastatic.org/ka-perseus-images/1cf07dd1b812de338ef86bef936e743ddac79ced.jpg)

Comienza con el dígito de la extrema derecha, haz k=0 **y** para **cada dígito**:

- **Si el dígito es 1, necesitamos una parte para 2^k, de lo contrario no es necesario.**
- **Súmale 1 a k y muévete al siguiente dígito a la izquierda.**

![img](https://cdn.kastatic.org/ka-perseus-images/85b4660da7c4e4f1e1662686a9771a51b2cf4d08.jpg)

#### Paso 2: calcula el mod C de las potencias de dos ≤ B
```python
5^1 mod 19 = 5

5^2 mod 19 = (5^1 * 5^1) mod 19 = (5^1 mod 19 * 5^1 mod 19) mod 19
5^2 mod 19 = (5 * 5) mod 19 = 25 mod 19
5^2 mod 19 = 6

5^4 mod 19 = (5^2 * 5^2) mod 19 = (5^2 mod 19 * 5^2 mod 19) mod 19
5^4 mod 19 = (6 * 6) mod 19 = 36 mod 19
5^4 mod 19 = 17

5^8 mod 19 = (5^4 * 5^4) mod 19 = (5^4 mod 19 * 5^4 mod 19) mod 19
5^8 mod 19 = (17 * 17) mod 19 = 289 mod 19
5^8 mod 19 = 4

5^16 mod 19 = (5^8 * 5^8) mod 19 = (5^8 mod 19 * 5^8 mod 19) mod 19
5^16 mod 19 = (4 * 4) mod 19 = 16 mod 19
5^16 mod 19 = 16

5^32 mod 19 = (5^16 * 5^16) mod 19 = (5^16 mod 19 * 5^16 mod 19) mod 19
5^32 mod 19 = (16 * 16) mod 19 = 256 mod 19
5^32 mod 19 = 9

5^64 mod 19 = (5^32 * 5^32) mod 19 = (5^32 mod 19 * 5^32 mod 19) mod 19
5^64 mod 19 = (9 * 9) mod 19 = 81 mod 19
5^64 mod 19 = 5
```

#### Paso 3: usa las propiedades de multiplicación modular para combinar los valores calculados de mod C
```Python
5^117 mod 19 = ( 5^1 * 5^4 * 5^16 * 5^32 * 5^64) mod 19
5^117 mod 19 = ( 5^1 mod 19 * 5^4 mod 19 * 5^16 mod 19 * 5^32 mod 19 * 5^64 mod 19) mod 19
5^117 mod 19 = ( 5 * 17 * 16 * 9 * 5 ) mod 19
5^117 mod 19 = 61200 mod 19 = 1
5^117 mod 19 = 1
```

## Notas:

Existen más técnicas de optimización, pero están fuera del alcance de este artículo. Debe tenerse en cuenta que cuando realizamos exponenciación modular en criptografía, no es raro utilizar exponentes para B > 1000 bits.



## Optimizando dividiendo el exponente a la mitad

```Python
	def mod_exp(a, b, c):
		"""Optimizando dividiendo el exponente a la mitad"""
		if a == 0 and b == 0:
			return float("INF")

		if b == 0:
			return 1

		res = 1
		base = a
		while b > 1:
			if b % 2 == 1:
				res = (res * base) % c
				b -= 1

			b //= 2
			base = (base * base) % c

		return (res * base) % c

```