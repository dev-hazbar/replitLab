def egcd(a, b):
    """Algoritmo extendido de Euclides para encontrar el GCD y los coeficientes de Bézout"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modinv(a, m):
    """Calcula el inverso multiplicativo de a modulo m usando el algoritmo extendido de Euclides"""
    gcd, x, _ = egcd(a, m)
    if gcd != 1:
        raise Exception('No tiene inverso multiplicativo')
    return x % m

def chinese_remainder_theorem(n, a):
    """Resuelve el sistema de congruencias usando el teorema del resto chino"""
    total = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        p = prod // ni
        total += ai * modinv(p, ni) * p

    return total % prod





if __name__ == '__main__':
	# Ejemplo de uso:
	n = [3, 5, 7]  # Módulos
	a = [2, 3, 2]  # Restos

	x = chinese_remainder_theorem(n, a)
	print(f"La solución es x = {x}")
