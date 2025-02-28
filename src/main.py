import functions as functions

# Entrada del usuario por consola convietiendo a minúscula
numero = str(input("Ingrese un número alfabéticamente, ejemplo: siete\n").lower())

# Impresión del dato ingresado por el usuario
print("Entrada:", numero)

# Impresión del valor númerico
print("Salida:", functions.convertir_a_numero(numero))