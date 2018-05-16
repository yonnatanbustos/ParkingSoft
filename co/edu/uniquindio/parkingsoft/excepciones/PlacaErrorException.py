
class PlacaErrorException(Exception):
    def __init__(self, mensaje):
        super(PlacaErrorException, self).__init__(self, mensaje)
