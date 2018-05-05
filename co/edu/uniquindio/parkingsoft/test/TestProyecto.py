import unittest

from PyQt5.QtSql import QSqlDatabase

from co.edu.uniquindio.parkingsoft.logica import Parqueadero, Usuario


class TestProyecto(unittest.TestCase):
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('parqueadero')
    db.setUserName('root')
    db.setPassword('12345')
    db.open()
    parqueadero = Parqueadero.Parqueadero(db)

    def test_ingresoVehico(self):
        usuario = Usuario.Usuario("123", "yonnatan", "bustos", "yonnatan_bustos", "123", "EMPLEADO")
        self.parqueadero.usuario = usuario
        placa = "ZRM032"
        tipoVehiculo = "CARRO"
        (mensaje, resultado) = Parqueadero.Parqueadero.ingresoVehicular(self.parqueadero, placa, tipoVehiculo)
        self.assertEqual(resultado, True)
        self.db.rollback()

    def test_registrarUsuario(self):
        cedula = "1094960469"
        nombres = "YONNATAN EDUARDO"
        apellidos = "BUSTOS RODRIGUEZ"
        nombre_usuario = "YEBUSTOSR"
        password = "123"
        tipo = "EMPLEADO"
        resultado = self.parqueadero.registrarUsuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
        self.assertEqual(resultado, True)
        self.db.rollback()

    def test_salidaVehiculo(self):
        placa = "ZRM032"
        (tiquete, estado) = Parqueadero.Parqueadero.salidaVehiculo(self.parqueadero, placa, True)
        self.assertEqual(estado, False)
        self.db.rollback()

    def test_ingresarMensualida(self):
        placa = "RBR198"
        tipoVehiculo = "CARRO"
        propietario = "JUAN MANUEL PARRA"
        telefono = "3214034659"
        fechaEntrada = "04/05/2018"
        fechaSalida = "04/06/2018"
        resultado = Parqueadero.Parqueadero.ingresarMensualida(self.parqueadero, placa, tipoVehiculo, propietario,
                                                               telefono,
                                                               fechaEntrada, fechaSalida)
        self.assertEqual(resultado, 1)
        self.db.rollback()

    def test_pagarSalida(self):
        placa = "ZRM032"
        (tiquete, estado) = Parqueadero.Parqueadero.salidaVehiculo(self.parqueadero, placa, True)
        self.parqueadero.tiquete = tiquete
        valorIngresado = 1700
        (resultado, mensaje) = Parqueadero.Parqueadero.pagarSalida(self.parqueadero, valorIngresado)
        self.assertEqual(resultado, 1)
        self.db.rollback()
