from figurageometrica import *
class Rectangulo(figurageometrica):
    def init(self, alto, ancho):
        super().init(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def str(self):
        return f"Rectángulo - alto: {self.alto}, ancho: {self.ancho}, área: {self.area()}"