from figurageometrica import *
class Cuadrado(figurageometrica):
    def init(self, lado):
        super().init(lado, lado)

    def area(self):
        return self.alto * self.ancho

    def str(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"



