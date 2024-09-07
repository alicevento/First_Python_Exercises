import random

# 1. Imprimir un mensaje: Escribe un programa que imprima "Hola, Python".
print("Hola, Python")

# 2. Sumar dos números:Escribe un programa que solicite dos números al usuario y luego imprima la suma.
print("Ejericicio 2: suma de números. Sólo puedes sumar números enteros")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2

# Imprime el resultado
print("La suma de los dos números es:", suma)

# 3. Número par o impar: Escribe un programa que solicite un número al usuario e indique si es par o impar.
print("Ejericicio 3: Números par o impar")
num = int(input("Ingrese un número: "))


# Imprime si el número es par o impar
if num % 2 == 0:
    print(num, "es par.")
else:
    print(num, "es impar.")
    

# 4. Área de un triángulo, dado su base y altura.
print("Ejericicio 4: Calcular área de un triángulo")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2

# Imprime el resultado
print("El área del triángulo es:", area)

# 5. Intercambio de valores: Escribe un programa que intercambie los valores de dos variables.
print("Ejercicio 5: Intercambio de valores")
num1 = 10
num2 = 20
# Intercambio de valores
num1, num2 = num2, num1

# Imprime los valores intercambiados
print("El valor de num1 es:", num1)
print("El valor de num2 es:", num2)

# 6. Conversión de temperatura: Escribe un programa que convierta una temperatura de grados Celsius a Fahrenheit.
print("Ejercicio 6: Conversión de temperatura (Celsius a Fahrenheit)")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
# Imprime el resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)

# 7. Números consecutivos: Escribe un programa que imprima los números del 1 al 10 en orden.
print("Ejercicio 7: Números consecutivos")
for i in range(1, 11):
    print(i)
#  Imprime números del 1 al 10 pero en aleatorio
print("Números aleatorios del 1 al 10:")
for i in range(10):
    print(random.randint(1, 10))

# 8. Suma de una lista: Escribe un programa que sume todos los números de una lista.
print("Ejercicio 8: Suma de una lista")
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
# Imprime el resultado
print("La suma de los números de la lista es:", suma)

# 9. Número mayor: Escribe un programa que solicite tres números y determine cuál es el mayor.
print("Ejercicio 9: Número mayor")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Determina el número mayor
if num1 > num2 and num1 > num3:
    print(num1, "es el número mayor.")
elif num2 > num1 and num2 > num3:
    print(num2, "es el número mayor.")
else:
    print(num3, "es el número mayor.")

# 10. Invertir una cadena: Escribe un programa que tome una cadena y la imprima al revés.
print("Ejercicio 10: Invertir una cadena de texto")
cadena = input("Ingrese una cadena de texto: ")
# Inverte la cadena
# línea clave para que funcione el programa: El slicing permite acceder a una subcadena o invertirla [start:stop:step]
invertida = cadena[::-1] 
# Imprime la cadena invertida
print("La cadena invertida es:", invertida)

# 11. Contador de vocales: Escribe un programa que cuente cuántas vocales hay en una cadena dada.
print("Ejercicio 11: Contar vocales en una cadena")
cadena = input("Ingrese una cadena de texto: ").lower()
vocales = "aeiou"
contador = 0

# Recorre la cadena y cuenta las vocales
for letra in cadena:
    if letra in vocales:
        contador += 1
# Imprime el resultado
print("La cadena tiene", contador, "vocales.")

# 12. Adivina el número: Escribe un programa donde el usuario tenga que adivinar un número entre 1 y 10.
print("Ejercicio 12: Adivina un número (entre 1 y 10)")
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina un número entre 1 y 10: "))

if intento == numero_secreto:
    print("¡Adivinaste!")
else:
    print(f"No adivinaste. El número era {numero_secreto}")
    
# 13. Factorial: Escribe un programa que calcule el factorial de un número
print("Ejercicio 13: Calcular el factorial de un número")
num = int(input("Ingresa un número: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es {factorial}")

# 14. Números pares en una lista: Escribe un programa que imprima todos los números pares de una lista dada.
print("Ejercicio 14: Números pares en una lista")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in lista if num % 2 == 0]
print("Números pares:", pares)

# 15. Tablas de multiplicar: Escribe un programa que imprima la tabla de multiplicar del 1 al 10 para un número dado por el usuario.
print("Ejercicio 15: Tablas de multiplicar")
num = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 16. Conversión de horas a segundos: Escribe un programa que convierta una cantidad de horas dada por el usuario a segundos.
print("Ejercicio 16: Conversión de horas a segundos")
horas = int(input("Ingrese la cantidad de horas: "))
segundos = horas * 3600
print(f"{horas} horas equivalen a {segundos} segundos.")

# 17. Suma de dígitos: Escribe un programa que tome un número entero y calcule la suma de sus dígitos.

# 18. Verificar palíndromo: Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# 19. Imprimir números impares: Escribe un programa que imprima todos los números impares entre 1 y 20.
# 20. Contador de palabras: Escribe un programa que cuente el número de palabras en una frase dada por el usuario.