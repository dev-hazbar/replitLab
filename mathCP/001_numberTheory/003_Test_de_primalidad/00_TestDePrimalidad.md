# Test de Primalidad

**Métodos determinísticos**: son más lentos pero infalibles.

**Métodos probabilísticos**: son rápidos y adecuados para aplicaciones prácticas como criptografía, aunque tienen un margen de error.

## Tipos de test
**1. Métodos Determinísticos**

- **División por Fuerza Bruta**
Verifica si el número es divisible por cualquier número menor o igual a su raíz cuadrada.
Ineficiente para números grandes.

- **Criba de Eratóstenes**
Genera todos los números primos hasta un límite dado.
Útil para encontrar primos en un rango.

- **Algoritmo AKS**
Un método determinístico que funciona para cualquier número entero.
Es polinómico, pero lento en la práctica para números grandes.

- **Test de Lucas-Lehmer**
Específico para comprobar si un número es un primo de Mersenne.

- **Test de Pépin**
Se utiliza para comprobar si un número de Fermat es primo.

---

**2. Métodos Probabilísticos**

- **Test de Fermat**
Basado en el Pequeño Teorema de Fermat:
\[
a^{n-1} \equiv 1 \pmod{n}
\]
No es confiable para números compuestos "pseudoprimos de Fermat".

- **Test de Miller-Rabin**
Un refinamiento del test de Fermat.
Verifica si \( n \) falla ciertas condiciones de primalidad.
Muy utilizado debido a su equilibrio entre velocidad y precisión.

- **Test de Solovay-Strassen**
Basado en el símbolo de Jacobi y generaliza el test de Fermat.

- **Test de Baillie-PSW**
Combina Lucas y Miller-Rabin.
Hasta ahora, no se han encontrado contraejemplos.

- **Test de Lehmann**
Usa propiedades de los números cuadráticos modulares.
