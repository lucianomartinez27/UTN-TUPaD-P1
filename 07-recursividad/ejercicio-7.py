def contar_bloques(alto_piramide):
    if alto_piramide == 1:
        return 1
    else:
        return alto_piramide + contar_bloques(alto_piramide - 1)

print(contar_bloques(10))