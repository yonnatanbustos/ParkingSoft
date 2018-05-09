# excepcion propia cuando hay errores en las mensualidades.
class MensualidadException(Exception):
    def __init__(self, mensaje):
        super(MensualidadException, self).__init__(self, mensaje)
