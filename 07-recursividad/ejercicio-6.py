def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        return ultimo_digito + suma_digitos(n // 10)

print(suma_digitos(1234567890))