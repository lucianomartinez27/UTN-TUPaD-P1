def es_palindromo(palabra):
    palabra = palabra.lower().strip()
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:len(palabra)-1])
