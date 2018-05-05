class VehiculoYaExiste(Exception):
    mensaje = "El vehicilo ya se encuentra registrado en el parqueadero"

    def __init__(self):
        super(VehiculoYaExiste, self).__init__(self, self.mensaje)
