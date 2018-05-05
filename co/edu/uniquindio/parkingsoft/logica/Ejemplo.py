from datetime import datetime, timedelta
from co.edu.uniquindio.parkingsoft.LogicaUI import Login
from PyQt5.QtSql import QSqlDatabase
import os.path



def createConection():
    Login.db = QSqlDatabase.addDatabase('QMYSQL')
    Login.db.setHostName(Login.host)
    Login.db.setDatabaseName(Login.nameDataBase)
    Login.db.setUserName(Login.nameUser)
    Login.db.setPassword(Login.password)
    Login.db.open()
    print(Login.db.lastError().text())
    return True

class Ejemplo():
    formatoHora = "%H:%M:%S"
    formatoFecha = "%d/%m/%Y"
    # fechaEntrada = datetime(2018, 4, 17).strftime(formatoFecha)
    # print(fechaEntrada)
    fechaEntrada = datetime.strptime("10/10/2018", formatoFecha)
    # salida = time.strptime(formatoFecha)
    fechaSalida = datetime.strptime("18/10/2018", formatoFecha)
    horaEntrada = datetime.strptime("13:42:56", formatoHora)
    horaSalida = datetime.strptime("15:45:56", formatoHora)
    tiempo = fechaSalida - fechaEntrada
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

    db = Login.Login.db.databaseName()
    print(db)
    estado = os.path.exists(db)
    print(estado)
