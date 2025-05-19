def calcular_potencia(n, m):
    if m == 0:
        return 1
    return n * calcular_potencia(n, m-1)

print(calcular_potencia(3, 2))