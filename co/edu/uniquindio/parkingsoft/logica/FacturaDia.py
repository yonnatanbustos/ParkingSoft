from co.edu.uniquindio.parkingsoft.logica import Parqueadero


class FacturaDia():
    idTiquete: int
    horaEntrada: str
    fechaEntrada: str
    horaSalida: str
    fechaSalida: str
    tiempo: str
    cobro: int
    descuento: bool
    parqueadero: Parqueadero

    def __init__(self, parqueadero: Parqueadero, idTiquete, horaEntrada, fechaEntrada):
        self.parqueadero = parqueadero
        self.horaEntrada = horaEntrada
        self.fechaEntrada = fechaEntrada
        self.descuento = False
        self.idTiquete = idTiquete
