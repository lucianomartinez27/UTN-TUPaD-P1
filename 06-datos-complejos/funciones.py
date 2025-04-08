from pila import Pila

def es_cierre(caracter):
    return caracter in "]})"

def obtener_apertura(caracter):
    return {
        '}' : '{',
        ')' : '(',
        ']' : '[',
    }[caracter]

def balanceado(cadena):
    pila = Pila()
    for caracter in cadena:
        if es_cierre(caracter):
            if pila.desapilar() != obtener_apertura(caracter):
                return False
        else:
            pila.apilar(caracter)
    return pila.esta_vacia()

