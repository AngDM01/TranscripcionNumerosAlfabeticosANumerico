# Mapeo de variables relevante para formar los números
mapeo =  {
  "cero": 0, "uno": 1, "un": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
  "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
  "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16,
  "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinti": 20, "veinte": 20,
  "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60,
  "setenta": 70, "ochenta": 80, "noventa": 90, "ciento": 100,
  "doscientos": 200, "trescientos": 300, "cuatrocientos": 400,
  "quinientos": 500, "seiscientos": 600, "setecientos": 700,
  "ochocientos": 800, "novecientos": 900, "mil": 1000, "millon": 1000000, "millones": 1000000
}

# Función para determinar el número
def convertir_a_numero(texto):
  resultado = 0
  subresultado = 0
  factor = 1  # se multiplicará el resultado para obtener el número
  palabras = texto.split(" ")

  for palabra in palabras:
    if palabra == "y":  # ignorar "y"
        continue

    if palabra in mapeo:
      # Si es mil, multiplicar antes de sumar
      if palabra == "mil":
        resultado = resultado + (subresultado * mapeo[palabra])
        subresultado = 0
      # Si es millon, sumar antes de multiplicar
      elif palabra == "millon" or palabra == "millones":
        resultado = (resultado + subresultado) * mapeo[palabra]
        subresultado = 0
      else:
        subresultado += mapeo[palabra]

  resultado += subresultado  # Al final sumamos cualquier subresultado restante

  return resultado
