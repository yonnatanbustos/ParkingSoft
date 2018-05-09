from co.edu.uniquindio.parkingsoft.logica import FacturaDia

# clase que contiene los datos de un vehiculo del parqueadero
class Vehiculo (object):
    placa: str  # placa del vehiculo
    tipo_vehiculo: str  # tipo de vehiculo (carro o moto)
    idTiquete : int  # id del tiquete asignado

    # constructor de la clase
    def __init__(self, placa, tipoVehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipoVehiculo
        self.idTiquete = -1

    # metodo que permite modificar el id del tiquete asignado
    # idTiquete: nuevo id a asignar
    def setIdTiquete(self, idTiquete):
        self.idTiquete = idTiquete
