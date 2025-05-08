from figurageometrica import *
class Rectangulo(figurageometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Rectángulo -> {self.__dict__.__str__()}"

if __name__ == '__main__':
    rectangulo = Rectangulo (16, 6)
    print(rectangulo)
