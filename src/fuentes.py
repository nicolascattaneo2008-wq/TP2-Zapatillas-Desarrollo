import csv
import json
from abc import ABC, abstractmethod


class FuenteDatos(ABC):

    @abstractmethod
    def cargar(self, ruta):
        pass


class FuenteCSV(FuenteDatos):

    def cargar(self, ruta):
        with open(ruta, newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)

            if not lector.fieldnames:
                raise ValueError("El archivo CSV no tiene encabezados.")

            return list(lector)


class FuenteJSON(FuenteDatos):

    def cargar(self, ruta):
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de productos.")

        return datos