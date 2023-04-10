# Función de suma
def suma(num1, num2):
    return num1 + num2

# Función de resta
def resta(num1, num2):
    return num1 - num2

# Función de multiplicación
def multiplicacion(num1, num2):
    return num1 * num2

# Función de división
def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero."
    else:
        return num1 / num2

# Menú principal
print("Bienvenido a la calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Pedir opción al usuario
opcion = int(input("Selecciona una opción (1/2/3/4): "))

# Pedir números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar operación según opción seleccionada
if opcion == 1:
    resultado = suma(num1, num2)
elif opcion == 2:
    resultado = resta(num1, num2)
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
elif opcion == 4:
    resultado = division(num1, num2)
else:
    print("Opción inválida")

# Mostrar resultado
print("El resultado es:", resultado)
