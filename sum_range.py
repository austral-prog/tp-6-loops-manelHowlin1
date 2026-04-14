def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    suma_total = 0
    if n <= 0:
        suma_total = 0
    else:
        for i in range(1, n+1):
            suma_total += i

    return suma_total

def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    suma_total = 0
    if n <= 0:
        suma_total = 0
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                suma_total += i
    return suma_total


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    total = 1
    if n <= 0:
        total = 1
    else:
        for i in range(1, n+1):
            total *= i
    return total
