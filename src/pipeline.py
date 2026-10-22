import re
from src.modelos import Producto


def convertir_entero(valor):
    texto = str(valor).strip()
    if not texto.isdigit():
        raise ValueError("Talle y cantidades deben ser números enteros no negativos.")
    return int(texto)


def preparar_productos(filas):
    productos = []
    rechazos = []
    normalizados = []
    codigos = set()

    for numero, fila in enumerate(filas, start=1):
        try:
            codigo = fila["codigo"].strip().upper()
            marca = fila["marca"].strip()
            modelo = fila["modelo"].strip()
            talle = convertir_entero(fila["talle"])
            stock = convertir_entero(fila["stock"])
            minimo = convertir_entero(fila["stock_minimo"])

            if not re.fullmatch(r"ZAP-\d{3}", codigo):
                raise ValueError("Código incorrecto.")
            if not marca or not modelo:
                raise ValueError("Marca o modelo vacío.")
            if codigo in codigos:
                raise ValueError("Código duplicado.")
            if not (30 <= talle <= 50 and 0 <= stock <= 5000 and 0 <= minimo <= 5000):
                raise ValueError("Talle o stock fuera de rango.")

            productos.append(Producto(codigo, marca, modelo, talle, stock, minimo))
            codigos.add(codigo)

            if codigo != fila["codigo"] or marca != fila["marca"] or modelo != fila["modelo"]:
                normalizados.append(numero)

        except (KeyError, ValueError, TypeError, AttributeError) as error:
            rechazos.append({"fila": numero, "motivo": str(error)})

    return productos, rechazos, normalizados