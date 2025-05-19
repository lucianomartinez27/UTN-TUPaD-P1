def contar_digito(numero, digito):
    if numero < 10:
        return 1 if digito == numero else 0
    else:
        return contar_digito(numero % 10, digito) + contar_digito(numero // 10, digito)

print(contar_digito(0, 0))
