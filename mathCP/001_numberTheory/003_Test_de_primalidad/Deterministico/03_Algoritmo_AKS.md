# Algoritmo AKS(Agrawal-Kayal-Saxena)



Algoritmo AKS: Decide si un número natural $ n $ es un número primo o compuesto.

1. Si existen números naturales $ a, b > 1 $ tales que $ n = a^b $, entonces $ n $ es compuesto.

2. Encuentra el más pequeño valor de $ r $ tal que $ o_r(n) > \log_2^2(n) $. If $r$ and $n$ are not coprime, then output composite.

3. Si $ 1 < \text{mcd}(a, n) < n $ para algún número natural $ a \leq r $, entonces $ n $ es compuesto.
4. Si $ n \leq r $, entonces $ n $ es primo.


5. Para $ a $ desde $ 1 $ hasta $ \left\lfloor \sqrt{\varphi(r)} \log_2(n) \right\rfloor $, haga lo siguiente:
    - Si $ (x + a)^n \not\equiv x^n + a \pmod{x^r - 1, n} $, entonces $ n $ es compuesto.

6. Si no se encuentra ninguna condición de composición, entonces $ n $ es primo.



## Análisis e implementación

- El primer paso se puede efectuar comprobando que $\left\lfloor \sqrt[b]{n} \right\rfloor^b \neq n$ para $ b = 2, 3, 4, \ldots, \left\lfloor \log_2 n \right\rfloor $. Esto requiere un tiempo $ \tilde{\mathcal{O}}(\log^3 n) $.

- El segundo paso se puede implementar buscando al primer valor de $ r $ que verifique $n^k \not\equiv 1 \pmod{r}$ para cualquier valor de $ k = 1, 2, 3, \ldots, \left\lfloor \log_2^2(n) \right\rfloor $. Como $ r \leq \lceil \log_2^5 n \rceil $, entonces este paso se efectúa en un tiempo $ \tilde{\mathcal{O}}(\log^7 n) $.

- En el tercer paso se puede utilizar el algoritmo de Euclides para buscar el máximo común divisor de dos números. Dado que se necesitan calcular $ r $ de estos valores, el tiempo necesario es $ \mathcal{O}(\log^6 n) $.

- En el cuarto paso solo se necesita comparar los dígitos. Esto necesita un tiempo $ \mathcal{O}(\log n) $.

- El quinto paso es el más lento de todos. Se puede utilizar una variante de la exponenciación binaria para calcular la parte izquierda de cada congruencia. Se necesitan calcular
$\left\lfloor \sqrt{\phi(r)} \log_2(n) \right\rfloor$ de estas congruencias. Por lo tanto, este paso requiere un tiempo $ \tilde{\mathcal{O}}(\log^{21/2} n) $.

- Por lo tanto, el algoritmo AKS requiere un tiempo $ \tilde{\mathcal{O}}(\log^{21/2} n) $. Es decir, el algoritmo AKS resuelve el problema de la primalidad de manera determinista y en un tiempo polinómico. En la práctica, el algoritmo parece correr en un tiempo $ \tilde{\mathcal{O}}(\log^6 n) $. Este tiempo se podría demostrar siempre y cuando se demuestre la conjetura de los números primos gemelos.





### Explicación de $ (\text{mod } a, b) $:

Cuando escribimos una congruencia de la forma
$A \equiv B \ (\text{mod } a, b),$
estamos diciendo que $ A - B $ debe ser divisible por ambos $ a $ y $ b $. Esto implica que:

- La congruencia en $ a $:
$A \equiv B \ (\text{mod } a),$
lo que significa que $ A - B $ es divisible por $ a $.
- La congruencia en $ b $:
$A \equiv B \ (\text{mod } b),$
lo que significa que $ A - B $ es divisible por $ b $.

Es decir, la notación $ (\text{mod } a, b) $ combina dos condiciones de divisibilidad a la vez.

**Ejemplo sencillo**:
Si tenemos una congruencia de la forma
$A \equiv B \ (\text{mod } 6, 4),$
esto significa que:

- $ A - B $ es divisible por $ 6 $.
- $ A - B $ también es divisible por $ 4 $.

Por lo tanto, $ A - B $ debe ser divisible por el mínimo común múltiplo (MCM) de $ 6 $ y $ 4 $, que es $ 12 $. Así que:

$A \equiv B \ (\text{mod } 12).$

Es decir, $ A $ y $ B $ son congruentes módulo $ 12 $, porque $ A - B $ debe ser divisible por el MCM de $ 6 $ y $ 4 $.





## Pseudocódigo



$\textbf{Input:} $ integer $ n = 31 > 1 $.

**$\textbf{(* Step 1 *)} $**
If $ (n = a^b \text{ for integers } a > 1 \text{ and } b > 1) $,
  output composite.
For $(  b = 2; b \leq \log_2(n); b++ )$ \{
  $ a = n^{\frac{1}{b}} $;
  If ($ a $ is integer),
    Return[Composite]
\}
$ a = n^{1/2} \dots n^{1/4} = \{ 5.568, 3.141, 2.360 \} $



**$\textbf{(* Step 2 *)}$**
Find the smallest $ r $ such that $ O_r(n) > (\log_2 n)^2 $.
$ \text{maxk} = \left\lfloor (\log_2 n)^2 \right\rfloor; $
$ \text{maxr} = \max[3, \lceil (\log_2 n)^5 \rceil] $; *(maxr really isn't needed)*
$ \text{nextR} = \text{True}; $
For ($ r = 2; \text{nextR} \text{ and } r < \text{maxr};\  r++ $) \{
  $ \text{nextR} = \text{False}; $
  For ($ k = 1; (!\text{nextR}) \text{ and } k \leq \text{maxk};\  k++ $) \{
    $ \text{nextR} = (\text{Mod}[n^k, r] == 1 \text{ or } \text{Mod}[n^k, r] == 0) $
  \}
\}
$ r--; $ *( the loop over increments by one )*

$ r = 29 $



**$\textbf{(* Step 3 *)}$**
If ($ 1 < \text{gcd}(a,n) < n $ for some $ a \leq r $),
  output composite.
  For ($ a = r; a > 1; a-- $) \{
    If $ (\text{gcd} = \text{GCD}[a,n]) > 1 \text{ and } \text{gcd} < n $,
    Return[Composite]
  \}

$ \text{gcd} = \{ \text{GCD}(29,31)=1, \text{GCD}(28,31)=1, \dots, \text{GCD}(2,31)=1 \} \not\sim 1 $



**$\textbf{(* Step 4 *)}$**
If ($ n \leq r $),
  output prime.
  If ($ n \leq r $),
    Return[Prime] *( this step may be omitted if $ n > 5690034 $)*

  $ 31 > 29 $



**$\textbf{(* Step 5 *)}$**
For $ a = 1 \text{ to }
\left\lfloor
\sqrt{\varphi(r)} \log_2(n)
\right\rfloor $ do
  If $ ((X+a)^n \neq X^n + a \ (\text{mod } X^r - 1, n)) $,
    output composite;

$\varphi[x] := \text{EulerPhi}[x];$

$\text{PolyModulo}[f] := \text{PolynomialMod}[\text{PolynomialRemainder}[f, x^{r}-1, x], n];$
$ \text{max} = \left\lfloor \log_2(n) \sqrt{\varphi(r)} \right\rfloor; $
For ($ a = 1; a \leq \text{max}; a++ $) \{
  If ($ \text{PolyModulo}[(x+a)^n - \text{PolynomialRemainder}[x^n + a, x^{r}-1], x] \neq 0 $) \{
    Return[Composite]
  \}
\}

$(x+a)^{31} =
  a^{31} + 31a^{30}x + 465a^{29}x^2 + 4495a^{28}x^3 + 31465a^{27}x^4 + 169911a^{26}x^5 + 736281a^{25}x^6 + 2629575a^{24}x^7 + 7888725a^{23}x^8 + 20160075a^{22}x^9 + 44352165a^{21}x^{10} + 84672315a^{20}x^{11} + 141120525a^{19}x^{12} + 206253075a^{18}x^{13} + 265182525a^{17}x^{14} + 300540195a^{16}x^{15} + 300540195a^{15}x^{16} + 265182525a^{14}x^{17} + 206253075a^{13}x^{18} + 141120525a^{12}x^{19} + 84672315a^{11}x^{20} + 44352165a^{10}x^{21} + 20160075a^9x^{22} + 7888725a^8x^{23} + 2629575a^7x^{24} + 736281a^6x^{25} + 169911a^5x^{26} + 31465a^4x^{27} + 4495a^3x^{28}$

$\text{PolynomialRemainder}[(x+a)^{31}, x^{29}-1] =
  465a^2 + a^{31} + (31a + 31a^{30})x + (1 + 465a^{29})x^2 + 4495a^{28}x^3 + 31465a^{27}x^4 + 169911a^{26}x^5 + 736281a^{25}x^6 + 2629575a^{24}x^7 + 7888725a^{23}x^8 + 20160075a^{22}x^9 + 44352165a^{21}x^{10} + 84672315a^{20}x^{11} + 141120525a^{19}x^{12} + 206253075a^{18}x^{13} + 265182525a^{17}x^{14} + 300540195a^{16}x^{15} + 300540195a^{15}x^{16} + 265182525a^{14}x^{17} + 206253075a^{13}x^{18} + 141120525a^{12}x^{19} + 84672315a^{11}x^{20} + 44352165a^{10}x^{21} + 20160075a^9x^{22} + 7888725a^8x^{23} + 2629575a^7x^{24} + 736281a^6x^{25} + 169911a^5x^{26} + 31465a^4x^{27} + 4495a^3x^{28}$

$(A) \, \text{PolynomialMod}[\text{PolynomialRemainder}[(x+a)^{31}, x^{29}-1], 31] = a^{31} + x^2$

$(B) \, \text{PolynomialRemainder}[x^{31} + a, x^{29}-1] = a + x^2$

$(A) - (B) = a^{31} + x^2 - (a + x^2) = a^{31} - a$

$\text{max} = \left\lfloor \log_2(31) \sqrt{\varphi(29)} \right\rfloor = 26$

{ $1^{31}-1 = 0 \, (\text{mod} \, 31), \, 2^{31}-2 = 0 \, (\text{mod} \, 31), \, 3^{31}-3 = 0 \, (\text{mod} \, 31), \dots, \, 26^{31}-26 = 0 \, (\text{mod} \, 31)$ }



**$\textbf{(* Step 6 *)}$**
Output prime.
31 \text{ Must be Prime}
