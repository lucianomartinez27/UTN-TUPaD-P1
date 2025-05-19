from mostrar_recursivo import mostrar_recursivo

def calcular_factorial(n):
    if n == 0:
        return 1
    return n * calcular_factorial(n - 1)


mostrar_recursivo(calcular_factorial, 5)