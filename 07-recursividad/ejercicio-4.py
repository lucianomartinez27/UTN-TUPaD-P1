def convertir_binario(n_decimal):
    resultado = n_decimal // 2
    resto = n_decimal % 2
    if resultado == 0:
        return "1"
    return convertir_binario(resultado) + str(resto)

print(convertir_binario(1567))
