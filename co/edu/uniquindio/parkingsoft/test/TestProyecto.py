import unittest

from pymysql import connect
from pymysql.cursors import Cursor

from co.edu.uniquindio.parkingsoft.logica import Parqueadero, Usuario

# clase donde se implementan las pruebas unitarias
class TestProyecto(unittest.TestCase):
    # variables necesarias para usar la base de datos en las pruebas
    conect: connect
    cursor: Cursor
    host: str = 'localhost'
    nameDataBase: str = 'parqueadero'
    nameUser: str = 'root'
    password: str = '12345'

    # estebloque permite establecer la conexion a la base de datos.
    conect = connect(host=host,
                     user=nameUser,
                     password=password,
                     database=nameDataBase)
    print(conect.open)

    cursor = conect.cursor()
    print(conect.cursor().connection)

    # instancia de un parqueadero.
    parqueadero = Parqueadero.Parqueadero(conect)

    # test del ingreso de un vehiculo al parqueadero.
    def test_ingresoVehico(self):
        usuario = Usuario.Usuario("1234", "yonnatan", "bustos", "yonnatan_bustos", "123", "EMPLEADO")
        self.parqueadero.usuario = usuario
        placa = "ZRM032"
        tipoVehiculo = "CARRO"
        (mensaje, resultado) = Parqueadero.Parqueadero.ingresoVehicular(self.parqueadero, placa, tipoVehiculo)
        print("test_ingresoVehiculo ", resultado)
        self.assertEqual(resultado, True)
        self.conect.rollback()

    # test del registro de un usuario.
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

    # test de la salida de un vehiculo del parqueadero.
    def test_salidaVehiculo(self):
        placa = "ZRM032"
        descuento = True
        (tiquete, estado) = Parqueadero.Parqueadero.salidaVehiculo(self.parqueadero, placa, descuento)
        print("test_salidaVehiculo ", estado)

        self.assertEqual(estado, True)
        self.conect.rollback()

    # test del ingreso de un vehiculo a una mensualidad.
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

    # test del total a pagar por un vehiculo que estaba en el parqueadero.
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

    # test del cierre de caja de un dia.
    def test_calcularCierreCaja(self):
        (resultado, estado) = Parqueadero.Parqueadero.calcularCierreCaja(self.parqueadero)
        print("test_calcularCierreCaja", resultado)
        self.assertEqual(estado, True)


