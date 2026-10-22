from src.fuentes import FuenteCSV
from src.pipeline import preparar_productos


def mostrar_productos(productos):
    for p in productos:
        print(f"{p.codigo} | {p.marca} | {p.modelo} | Talle {p.talle} | Stock: {p.stock}")
    print(f"Total de productos: {len(productos)}")

def buscar_productos(productos, texto, talle):
    encontrados = []

    for p in productos:
        coincide_texto = (
            not texto
            or texto.lower() in p.marca.lower()
            or texto.lower() in p.modelo.lower()
            or texto.lower() in p.codigo.lower()
        )

        coincide_talle = not talle or str(p.talle) == talle

        if coincide_texto and coincide_talle:
            encontrados.append(p)

    return encontrados

def main():
    filas = FuenteCSV().cargar("data/zapatillas.csv")
    productos, rechazos, normalizados = preparar_productos(filas)

    print(f"Productos cargados: {len(productos)}")
    print(f"Productos rechazados: {len(rechazos)}")

    while True:
        print("\nSISTEMA DE STOCK DE ZAPATILLAS")
        print("1. Consultar inventario")
        print("2. Buscar zapatillas")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            texto = input("Marca, modelo o código: ").strip()
            talle = input("Talle (Enter para omitir): ").strip()
            encontrados = buscar_productos(productos, texto, talle)
            mostrar_productos(encontrados)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    main()