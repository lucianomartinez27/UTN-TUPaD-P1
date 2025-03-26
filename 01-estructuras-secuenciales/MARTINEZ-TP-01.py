# Practico N1 - Estructuras secuenciales
# Alumno: Martinez Luciano Joaquin

#Ejercicio 1

print("Hola mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#Ejercicio 4
radio_circulo = int(input("ingrese el radio de un círculo: "))
pi = 3.14
area = pi * (radio_circulo ** 2)
print(f"El area es {area}")
perimetro = 2 * pi * radio_circulo
print(f"El perimetro es {perimetro}")

#Ejercicio 5

cantidad_segundos = int(input("ingrese la cantidad de segundos: "))
horas = cantidad_segundos / 60 / 60
print(f"{cantidad_segundos} segundos equivalen a {horas} horas")

#Ejercicio 6

numero = int(input("ingrese un número del 1 al 9: "))

if (numero < 1 or numero > 9):
	print("numero incorrecto")
else:
	for i in range(1, 11):
		print(f"{numero} * {i} = {i*numero}")

#Ejercicio 7

un_numero =  int(input("ingrese un número distinto de 0: "))
otro_numero =  int(input("ingrese otro número distinto de 0: "))

if (un_numero == 0 or otro_numero == 0):
	print("numeros incorrecto")
else:
	print(f"{un_numero} * {otro_numero} = {un_numero * otro_numero}")
	print(f"{un_numero} / {otro_numero} = {un_numero / otro_numero}")
	print(f"{un_numero} + {otro_numero} = {un_numero + otro_numero}")
	print(f"{un_numero} - {otro_numero} = {un_numero - otro_numero}")

#Ejercicio 8

altura =  int(input("ingrese su altura en metros: "))
peso =  int(input("ingrese su peso en kg: "))
imc = peso / (altura **2)
print(f"su índice de masa corporal es {imc}")

#Ejercicio 9
temperatura_celsuis =  int(input("ingrese una temperatura en Celsuis: "))
temperatura_farenheit = (9/5) * temperatura_celsuis + 32
print(f"{temperatura_celsuis} grados Celsuis son {temperatura_farenheit} grados Fahrenheit")

#Ejercicio 10
primer_numero =  int(input("ingrese el primer número: "))
segundo_numero =  int(input("ingrese el segundo número: "))
tercer_numero =  int(input("ingrese tercer y último número: "))
promiedo = (primer_numero + segundo_numero + tercer_numero) / 3
print(f"el promedio de {primer_numero}, {segundo_numero} y {tercer_numero} es {promiedo}")