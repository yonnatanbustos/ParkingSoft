from co.edu.uniquindio.parkingsoft.logica import Vehiculo, Parqueadero


class Mensualidad():
    vehiculo: Vehiculo
    propietario: str
    telefono: str
    fechaEntrada: str
    fechaSalida: str
    estado: int
    parqueadero: Parqueadero
    valor: int

    def __init__(self, parqueadero, vehiculo, propietario, telefono, fechaEntrada, fechaSalida, estado):
        self.parqueadero = parqueadero
        self.vehiculo = vehiculo
        self.propietario = propietario
        self.telefono = telefono
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.estado = estado
        if vehiculo.tipo_vehiculo == "CARRO_MENS":
            self.valor = parqueadero.CARRO_MENS
        else:
            self.valor = parqueadero.MOTO_MENS
