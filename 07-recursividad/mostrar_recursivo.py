def mostrar_recursivo(funcion, n):
    print(funcion(n))
    if n > 1:
        mostrar_recursivo(funcion, n - 1)