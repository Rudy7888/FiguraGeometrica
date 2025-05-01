class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    @property
    def alto(self):
        return self.alto
    @alto.setter
    def alto(self, valor):
        self.alto = valor
    @property
    def ancho(self):
        return self.ancho
    @ancho.setter
    def ancho(self, valor):
        self.ancho = valor
    def __str__(self):
        return f'alto: {self.alto}, ancho: {self.ancho}'