import unittest

from pymysql import connect
from pymysql.cursors import Cursor

from co.edu.uniquindio.parkingsoft.logica import Parqueadero, Usuario


class TestProyecto(unittest.TestCase):
    conect: connect
    cursor: Cursor
    host: str = 'localhost'
    nameDataBase: str = 'parqueadero'
    nameUser: str = 'root'
    password: str = '12345'

    conect = connect(host=host,
                     user=nameUser,
                     password=password,
                     database=nameDataBase)
    print(conect.open)

    cursor = conect.cursor()
    print(conect.cursor().connection)

    parqueadero = Parqueadero.Parqueadero(conect)

    def test_ingresoVehico(self):
        usuario = Usuario.Usuario("1234", "yonnatan", "bustos", "yonnatan_bustos", "123", "EMPLEADO")
        self.parqueadero.usuario = usuario
        placa = "ZRM032"
        tipoVehiculo = "CARRO"
        (mensaje, resultado) = Parqueadero.Parqueadero.ingresoVehicular(self.parqueadero, placa, tipoVehiculo)
        print("test_ingresoVehiculo ", resultado)
        self.assertEqual(resultado, True)
        self.conect.rollback()

    def test_registrarUsuario(self):
        cedula = "1094960469"
        nombres = "YONNATAN EDUARDO"
        apellidos = "BUSTOS RODRIGUEZ"
        nombre_usuario = "YEBUSTOSR"
        password = "123"
        tipo = "EMPLEADO"
        resultado = self.parqueadero.registrarUsuario(cedula, nombres, apellidos, nombre_usuario, password, tipo)
        print("test_registrarUsuario ", resultado)

        self.assertEqual(resultado, True)
        self.conect.rollback()

    def test_salidaVehiculo(self):
        placa = "ZRM032"
        descuento = True
        (tiquete, estado) = Parqueadero.Parqueadero.salidaVehiculo(self.parqueadero, placa, descuento)
        print("test_salidaVehiculo ", estado)

        self.assertEqual(estado, True)
        self.conect.rollback()

    def test_ingresarMensualida(self):
        placa = "RBR198"
        tipoVehiculo = "CARRO_MENS"
        propietario = "JUAN MANUEL PARRA"
        telefono = "3214034659"
        fechaEntrada = "09/05/2018"
        fechaSalida = "09/06/2018"
        resultado = Parqueadero.Parqueadero.ingresarMensualida(self.parqueadero, placa, tipoVehiculo, propietario,
                                                               telefono,
                                                               fechaEntrada, fechaSalida)
        print("test_ingresarMensualidad ", resultado)

        self.assertEqual(resultado, 1)
        self.conect.rollback()

    def test_pagarSalida(self):
        usuario = Usuario.Usuario("1234", "yonnatan", "bustos", "yonnatan_bustos", "123", "EMPLEADO")
        self.parqueadero.usuario = usuario
        placa = "ZRM032"
        (tiquete, estado) = Parqueadero.Parqueadero.salidaVehiculo(self.parqueadero, placa, True)
        self.parqueadero.tiquete = tiquete
        valorIngresado = 1700
        (resultado, mensaje) = Parqueadero.Parqueadero.pagarSalida(self.parqueadero, valorIngresado)
        print("test_pagarSalida ", resultado)

        self.assertEqual(resultado, 1)
        self.conect.rollback()

    def test_calcularCierreCaja(self):
        (resultado, estado) = Parqueadero.Parqueadero.calcularCierreCaja(self.parqueadero)
        print("test_calcularCierreCaja", resultado)
        self.assertEqual(estado, True)


