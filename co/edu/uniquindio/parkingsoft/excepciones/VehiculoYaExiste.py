# excepcion propia que se usa para validar si una placa de un vehiculo ya esta en el parqueadero
class VehiculoYaExiste(Exception):
    mensaje = "El vehicilo ya se encuentra registrado en el parqueadero"

    def __init__(self):
        super(VehiculoYaExiste, self).__init__(self, self.mensaje)
