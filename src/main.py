from src.fuentes import FuenteCSV
from src.pipeline import preparar_productos


def mostrar_productos(productos):
    for p in productos:
        print(f"{p.codigo} | {p.marca} | {p.modelo} | Talle {p.talle} | Stock: {p.stock}")
    print(f"Total de productos: {len(productos)}")


def main():
    filas = FuenteCSV().cargar("data/zapatillas.csv")
    productos, rechazos, normalizados = preparar_productos(filas)

    print(f"Productos cargados: {len(productos)}")
    print(f"Productos rechazados: {len(rechazos)}")

    while True:
        print("\nSISTEMA DE STOCK DE ZAPATILLAS")
        print("1. Consultar inventario")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    main()