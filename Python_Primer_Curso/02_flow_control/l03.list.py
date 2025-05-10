###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el paso (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print ("_____________________EJERCICIO 1___________________________________")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print (mensaje [7:14]) 


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print ("_____________________EJERCICIO 2___________________________________")
numeros = [10, 20, 30, 40, 50]

temp = numeros[0]  # temp guarda el valor 10
numeros [0] = numeros [-1]
numeros [-1] = temp

print (numeros)


# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print ("_____________________EJERCICIO 3___________________________________")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print (sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print ("_____________________EJERCICIO 4___________________________________")

listae4 = [1, 2, 3]

listae2 = listae4 + listae4
print (listae2)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print ("_____________________EJERCICIO 5___________________________________")

lista_centro = [10, 20, 30, 40, 50]
print (len(lista_centro))
centro = lista_centro [len (lista_centro)//2 : len (lista_centro)//2+1]
print (centro)


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print ("_____________________EJERCICIO 6___________________________________")



# VERSION SIN AUTOMATIZAR 
# lista_reversa = [1, 2, 3, 4, 5, 6]

# # PARA COGUER LA PRIMERA MITAD
# centro_reversa = lista_reversa [: len (lista_reversa)//2  ]
# # PARA COGER LA SEGUNDA MITAD
# centro_reversa2 = lista_reversa [len (lista_reversa)//2:]
# print (centro_reversa2)
# primero_indice = centro_reversa [0]
# centro_reversa [0] = centro_reversa [-1]
# centro_reversa [-1] = primero_indice 
# print (centro_reversa)

# resultado = centro_reversa + centro_reversa2
# print (resultado)


# AUTOMATIZADA 
print("_____________________EJERCICIO 6___________________________________")
lista_reversa = [1, 2, 3, 4, 5, 6]

# Obtener la primera mitad e invertirla
primera_mitad = lista_reversa[:len(lista_reversa)//2][::-1]

# Obtener la segunda mitad
segunda_mitad = lista_reversa[len(lista_reversa)//2:]

# Combinar ambas partes
resultado = primera_mitad + segunda_mitad

print(resultado)


# DE ESTA MANERA DAS UN ARRAY LA VUELTA
hola = [1 , 2 ,3 ,4 ]
print (hola [::-1])     

