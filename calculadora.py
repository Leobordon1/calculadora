import os
print("------------------")
print("Calculadora")
print("------------------")
while True:
	def calculadora (numero1, numero2):
		if opcion == 1:
			os.system("cls")
			return  numero1 + numero2
		elif opcion == 2:
			os.system("cls")
			return numero1 - numero2
		elif opcion == 3:
			os.system("cls")
			return numero1 * numero2
		elif opcion == 4:
			os.system("cls")
			return numero1 / numero2
		else:
			return "Opción no válida"

	print("Que operacion desea realizar?")
	print("Opcion 1 - Suma")
	print("Opcion 2 - Resta")
	print("Opcion 3 - Multiplicaion")
	print("Opcion 4 - Division")
	print("Opcion 5 - Salir")

	opcion =int(input("Ingrese una opción:"))
	if opcion == 5:
		os.system("cls")
		print("Gracias por usar la calculadora")
		break
	numero1 = int(input("Ingrese un numero:"))
	numero2 = int(input("Ingrese otro numero:"))

	print(calculadora(numero1, numero2))