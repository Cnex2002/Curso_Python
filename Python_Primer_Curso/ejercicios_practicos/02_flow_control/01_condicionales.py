
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

from os import system
if system("clear") != 0: system("cls")


# print ("Bienvenido, sistema creado por jhonny")

# number_one = input ("Ingrese un numero 1:")
# number_two = input ("Ingrese un numero 2:")

# number_one = int (number_one)
# number_two = int (number_two)

# if number_one > number_two :
#     print (f"El numero mayor es{number_one}, y el menor {number_two}")
# elif number_one == number_two:
#      print (f"El numero {number_one} es igual {number_two}")
# else:
#     print (f"El numero mayor {number_two}, y el numero menor es {number_one}")


print ("___________________________________________________________________________________")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# number_one = input ("Ingrese un numero 1:")
# number_two = input ("Ingrese un numero 2:")
# number_operador = input ("Ingrese un operador:")
# pantalla = ""

# number_one = int (number_one)
# number_two = int (number_two)
# number_operador = str (number_operador)


# if number_operador == "+":
#     pantalla = number_one + number_two
# elif number_operador == "-":
#      pantalla = number_one - number_two
# elif number_operador == "*":
#      pantalla = number_one * number_two
# elif number_operador == "/":
#      pantalla = number_one / number_two
# else:
#      pantalla = ""  

# if pantalla == "":
#      print (f"EL OPERADOR INGRESADO ES INCORRECTO {pantalla} {number_operador}")
# else :
#      print (f"ELRESULTADO ES {pantalla}")




# Ejercicio 3: years bisiesto
# Pide al usuario que introduzca un years y determina si es bisiesto.
# Un years es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


# years = input ("INGRESA EL years PARA PARA VER SI ES BISIESTO:")
# pantalla = ""

# years = int (years)


# if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
#      pantalla= f"El years {years} es bisiesto (tiene 366 días)."

# else:
#      pantalla= f"El years {years} no es bisiesto (tiene 365 días)."

# print (pantalla)

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 yearss)
# - Niño (3-12 yearss)
# - Adolescente (13-17 yearss)
# - Adulto (18-64 yearss)
# - Adulto mayor (65 yearss o más)


edad = input ("Ingrese su edad")

edad = int (edad)
pantalla= ""

if   edad >= 65:
     pantalla = f"La edad ingresada es de {edad} y es de un adulto mayor"
elif edad >= 18 and edad <= 64:
     pantalla = f"La edad ingresada es de {edad} y es de un adulto"
elif edad >= 13 and edad <= 17:
     pantalla = f"La edad ingresada es de {edad} y es de un adolecente"
elif edad >=3 and edad <= 2 :
     pantalla = f"La edad ingresada es de {edad} y es de un Niño"
else:
     pantalla = f"La edad ingresada es de {edad} y es de un bebe"

print (pantalla)




     
