from dataclasses import dataclass


@dataclass
class Producto:
    codigo: str
    marca: str
    modelo: str
    talle: int
    stock: int
    stock_minimo: int

    def faltantes(self):
        return max(0, self.stock_minimo - self.stock)

    def registrar_entrada(self, cantidad):
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        self.stock += cantidad

    def registrar_salida(self, cantidad):
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        if cantidad > self.stock:
            raise ValueError("No hay suficientes pares disponibles.")
        self.stock -= cantidad