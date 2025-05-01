###
# 04 - Variables
# Las variables sirven para almacenar información en la memoria.
# Python es un lengauaje de tipado dinámico, por lo que no es necesario declarar el tipo de la variable.
###

# Asignación de variables
# Solo se hace de poner esto:
my_name = "Juan"
print(my_name)

# Tipado dinamico: el tipado de dato se determina en tiempo de ejecución
# que no tienes que declararlo explicitamente

name = "Juan"
print ( name )
name = 10
print ( type ( name ))
age = 10

# Tipado fuert: Pytghon no realiza conversiones automáticas entre tipos de datos
#print ( "Hola" + 10 ) # TypeError: can only concatenate str (not "int") to str

print (f"hola {my_name}, tengo {age + 5} años") # f-string


# NO recomendada forma de asignar variables
name, age, height = "Juan", 10, 1.80

# Convención de nombres de variables
# mi_nombre_de_variable        snake_case
# se recomienda para nombres de costantes  Upper_Case
# MI_NOMBRE_DE_CONSTANTE


#No se recomienda  estos nombres de variables
# MiNombreDeVariable

