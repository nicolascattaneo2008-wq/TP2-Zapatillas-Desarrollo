import csv
from pathlib import Path
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

def registrar_movimiento(productos, tipo):
    codigo = input("Código de zapatilla: ").strip().upper()

    producto = None
    for p in productos:
        if p.codigo == codigo:
            producto = p
            break

    if producto is None:
        print("No se encontró ese producto.")
        return

    try:
        cantidad = int(input("Cantidad de pares: "))

        if tipo == "entrada":
            producto.registrar_entrada(cantidad)
        else:
            producto.registrar_salida(cantidad)

        guardar_stock(productos)
        print(f"Stock actual: {producto.stock} pares")

    except ValueError as error:
        print(f"Movimiento rechazado: {error}")

def guardar_stock(productos):
    carpeta = Path("outputs")
    carpeta.mkdir(exist_ok=True)

    with open(carpeta / "stock_actual.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["codigo", "marca", "modelo", "talle", "stock", "stock_minimo"])

        for p in productos:
            escritor.writerow([p.codigo, p.marca, p.modelo, p.talle, p.stock, p.stock_minimo])

def main():
    archivo_stock = Path("outputs/stock_actual.csv")
    ruta = archivo_stock if archivo_stock.exists() else Path("data/zapatillas.csv")
    filas = FuenteCSV().cargar(ruta)
    productos, rechazos, normalizados = preparar_productos(filas)

    print(f"Productos cargados: {len(productos)}")
    print(f"Productos rechazados: {len(rechazos)}")

    while True:
        print("\nSISTEMA DE STOCK DE ZAPATILLAS")
        print("1. Consultar inventario")
        print("2. Buscar zapatillas")
        print("3. Registrar entrada de pares")
        print("4. Registrar salida de pares")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_productos(productos)

        elif opcion == "2":
            texto = input("Marca, modelo o código: ").strip()
            talle = input("Talle (Enter para omitir): ").strip()
            encontrados = buscar_productos(productos, texto, talle)
            mostrar_productos(encontrados)

        elif opcion == "3":
            registrar_movimiento(productos, "entrada")

        elif opcion == "4":
            registrar_movimiento(productos, "salida")

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    main()