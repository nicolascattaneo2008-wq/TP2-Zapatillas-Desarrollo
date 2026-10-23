import unittest
from src.modelos import Producto


class TestAplicacion(unittest.TestCase):

    def test_entrada_stock(self):
        producto = Producto("ZAP-001", "Nike", "Air Max", 40, 2, 5)

        producto.registrar_entrada(3)

        self.assertEqual(producto.stock, 5)

    def test_salida_stock_insuficiente(self):
        producto = Producto("ZAP-001", "Nike", "Air Max", 40, 2, 5)

        with self.assertRaises(ValueError):
            producto.registrar_salida(5)

        self.assertEqual(producto.stock, 2)

    def test_csv_json_equivalentes(self):
        from src.fuentes import FuenteCSV, FuenteJSON
        from src.pipeline import preparar_productos

        filas_csv = FuenteCSV().cargar("data/zapatillas.csv")
        filas_json = FuenteJSON().cargar("data/zapatillas.json")

        productos_csv, _, _ = preparar_productos(filas_csv)
        productos_json, _, _ = preparar_productos(filas_json)

        inventario_csv = sorted(
            [vars(p) for p in productos_csv],
            key=lambda p: p["codigo"]
        )
        inventario_json = sorted(
            [vars(p) for p in productos_json],
            key=lambda p: p["codigo"]
        )

        self.assertEqual(inventario_csv, inventario_json)
        self.assertEqual(len(inventario_csv), 60)
