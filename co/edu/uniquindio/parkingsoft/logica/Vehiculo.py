from co.edu.uniquindio.parkingsoft.logica import FacturaDia

# clase que contiene los datos de un vehiculo del parqueadero
class Vehiculo (object):
    placa: str
    tipo_vehiculo: str
    idTiquete : int

    def __init__(self, placa, tipoVehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipoVehiculo
        self.idTiquete = -1

    def setIdTiquete(self, idTiquete):
        self.idTiquete = idTiquete
