from mostrar_recursivo import mostrar_recursivo
def fibonnaci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

mostrar_recursivo(fibonnaci, 10)