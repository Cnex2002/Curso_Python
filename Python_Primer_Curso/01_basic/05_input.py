###
# 05 Entradoa de usuarios (input) version simplificada
# la funcion input() permite al usuario ingresar datos desde el teclado
###

# print("Hola, ¿cómo te llamas?")
nombre = input("Hola, ¿cómo te llamas?\n")  # Se guarda el valor ingresado por el usuario en la variable nombre

print("Hola " + nombre + ", ¿Encatado en conocerte?")

age = input("¿Cuántos años tienes?\n")  # Se guarda el valor ingresado por el usuario en la variable age
age = int(age)  # Convierte el valor de age a un número entero
print(f"Tienes {age} años")


print ("Obtener multiples valores a la vez")

country, city = input("¿De qué país y ciudad eres?\n").split()  # Se guarda el valor ingresado por el usuario en la variable country y city

print(f"Eres de {country} y vives en {city}")