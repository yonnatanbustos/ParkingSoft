import csv
from datetime import datetime, timedelta

import numpy as np


class Ejemplo():
    try:
        f = open("parqueadero")
        print(f)
    except IOError as e:
        print("Uh oh! Esto no existe")
    formatoHora = "%H:%M:%S"
    formatoFecha = '%d/%m/%Y'
    fechaEntrada = datetime(2018, 4, 17).strftime(formatoFecha)
    print(fechaEntrada)
    fechaEntrada = datetime.strptime("10/02/2018", "%d/%m/%Y")
    # salida = time.strptime(formatoFecha)
    fechaSalida = datetime.strptime("10/03/2018", "%d/%m/%Y")
    print("fecha de entrada ", fechaEntrada)
    print("fecha de salida ", fechaSalida)
    horaEntrada = datetime.strptime("13:42:56", formatoHora)
    horaSalida = datetime.strptime("15:45:56", formatoHora)
    tiempo = fechaSalida - fechaEntrada

    fechaActual = datetime.today()
    fecha = fechaEntrada.strftime(formatoFecha)
    print(fecha)

    print("fecha actual: ", fechaActual)
    if (fechaSalida > fechaEntrada):
        print("fechaSalida>fechaEntrada")

    if fechaActual > fechaSalida and fechaActual > fechaEntrada:
        print("fechas ingresadas estan mal")
    tiempo = tiempo.days * 24
    total = horaSalida - horaEntrada + timedelta(hours=tiempo)
    print(total)
    print(tiempo)
    horaEntrada = "13:45:56"
    cadena = str(total).split(",")
    cadena2 = cadena[1]
    numero = cadena[0].split(" ")
    print(numero[0], "dias")
    cadena = str(cadena2).split(":")
    numero = int(cadena[0])
    print(numero, " horas")
    numero = int(cadena[1])
    print(numero, " minutos")
    numero = int(cadena[2])
    print(numero, " segundos")

    l = [[1, 2, 3, 4], [5, 6, 7, 8]]
    datos = np.asarray(l)
    # np.savetxt("output.csv",  # Archivo de salida
    #         datos.T,  # Trasponemos los datos
    #         fmt="%d",  # Usamos números enteros
    #         delimiter=",")

