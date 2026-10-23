# Sistema de control de stock de zapatillas

Autor: Nicolás Cattáneo

Materia: Programación Orientada a Datos

## Problema

Una tienda de zapatillas necesita controlar la cantidad de pares disponibles de cada modelo y talle, para evitar faltantes de mercadería.

## Objetivo

Desarrollar un programa en Python que permita consultar el inventario, registrar entradas y salidas de pares y detectar productos que necesitan reposición.

## Funcionalidades previstas

- Consultar el inventario.
- Buscar zapatillas por modelo o talle.
- Registrar entradas de mercadería.
- Registrar salidas de mercadería.
- Generar un informe de reposición.

## Alcance

La primera versión se limitará al control de stock. No incluirá facturación, clientes ni proveedores.

## Usuario

El programa está destinado al encargado de una tienda de zapatillas, que necesita consultar las existencias y controlar la reposición de mercadería.

## Resultados esperados

El programa mostrará las cantidades disponibles de cada producto y generará un informe con las zapatillas que necesitan reposición.

Este informe permitirá identificar los modelos y talles con stock insuficiente y calcular cuántos pares faltan para alcanzar el mínimo establecido.

## Datos utilizados

El programa utiliza un conjunto de 60 registros simulados de zapatillas, preparados para este trabajo práctico.

Los datos están disponibles en dos formatos:
- data/zapatillas.csv
- data/zapatillas.json

Cada registro representa un producto identificado por su modelo y talle, y contiene seis variables:
- codigo: identificador del producto.
- marca: marca de la zapatilla.
- modelo: nombre del modelo.
- talle: número de calzado.
- stock: cantidad de pares disponibles.
- stock_minimo: cantidad mínima de pares requerida.

Origen: datos simulados para uso académico, no obtenidos de una tienda real.

Responsable del trabajo: Nicolás Cattáneo.
Fecha de documentación: octubre de 2026.
Condiciones de uso: datos de ejemplo para fines educativos, sin fuentes externas ni información personal.

Limitaciones: los valores son ficticios y no representan las ventas, existencias ni preferencias reales de los consumidores. Por lo tanto, no deben utilizarse para sacar conclusiones comerciales reales.

## Requisitos para ejecutar el programa

Se necesita tener instalado Python 3.

El programa utiliza solamente bibliotecas estándar de Python, por lo que no requiere instalar paquetes adicionales.

## Cómo ejecutar el programa

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

    py -m src.main

El programa presenta un menú con las siguientes opciones:

1. Consultar el inventario.
2. Buscar zapatillas por marca, modelo o talle.
3. Registrar entradas de pares.
4. Registrar salidas de pares.
5. Consultar el informe de reposición.
0. Salir.

Los cambios de stock se guardan en outputs/stock_actual.csv para conservarlos entre ejecuciones.

Si todavía no existe ese archivo, el programa carga los datos originales desde data/zapatillas.csv.

También genera outputs/incidencias.csv para registrar los datos rechazados y normalizados.

Los archivos de la carpeta outputs son resultados de ejecución y no se incluyen en GitHub.

## Pruebas automáticas

Para ejecutar las pruebas, abrir una terminal en la carpeta principal del proyecto y escribir:

    py -m unittest discover -s tests -v

Las pruebas verifican:

- Que las entradas de mercadería aumenten correctamente el stock.
- Que una salida con stock insuficiente sea rechazada sin modificar las existencias.
- Que los archivos CSV y JSON produzcan el mismo inventario de 60 productos.

Las pruebas utilizan unittest, incluido en Python.

## Organización del código

El proyecto está organizado en carpetas y archivos con diferentes responsabilidades:

- data/: contiene los 60 productos simulados en archivos CSV y JSON.
- src/fuentes.py: contiene las clases encargadas de leer los archivos CSV y JSON mediante una interfaz común.
- src/modelos.py: define la clase Producto y sus métodos para registrar entradas, salidas y calcular faltantes.
- src/pipeline.py: valida, limpia y transforma los datos antes de utilizarlos.
- src/main.py: ejecuta el menú principal, permite consultar y modificar el inventario y muestra el informe de reposición.
- tests/test_aplicacion.py: contiene las pruebas automáticas del programa.
- README.md: explica el proyecto y cómo utilizarlo.
- requirements.txt: indica las dependencias necesarias.
- .gitignore: evita incluir archivos temporales en GitHub.

Durante la ejecución se crea la carpeta outputs/, donde se guarda el stock actualizado y el registro de incidencias.

Esta organización permite separar la lectura de datos, las validaciones, las operaciones de stock y las pruebas.

## Decisiones de limpieza y validación de datos

Antes de utilizar los datos, el programa realiza las siguientes operaciones:

- Elimina espacios innecesarios al principio y al final de los códigos, marcas y modelos.
- Convierte los códigos de productos a mayúsculas para mantener un formato uniforme.
- Comprueba mediante una expresión regular que los códigos tengan el formato ZAP- seguido de tres números.
- Verifica que los códigos no estén duplicados. Si un código aparece repetido, se conserva el primero y se rechazan los siguientes.
- Comprueba que la marca y el modelo no estén vacíos.
- Convierte los talles y las cantidades de stock a números enteros.
- Controla que los talles estén entre 30 y 50 y que las cantidades de stock y stock mínimo estén entre 0 y 5000.
- Rechaza los registros con datos faltantes, incorrectos o fuera de los rangos establecidos.

El programa separa los productos válidos de los rechazados.

Los registros rechazados se identifican mediante su número de fila y el motivo del error.

También se identifican las filas cuyos textos fueron normalizados.

Esta información se guarda en outputs/incidencias.csv, lo que permite revisar las decisiones tomadas durante el procesamiento.

Los datos originales de la carpeta data/ no se modifican.

## Ejemplo de resultado e interpretación

El programa permite identificar las zapatillas cuyo stock está por debajo del mínimo establecido.

Por ejemplo, si una zapatilla tiene:
- Stock actual: 2 pares.
- Stock mínimo: 5 pares.

El programa calcula que faltan 3 pares para alcanzar el mínimo.

En una de las ejecuciones de prueba, el informe de reposición mostró:

- Productos a reponer: 35.
- Total de pares a reponer: 103.

Esto significa que 35 productos tenían existencias inferiores a su stock mínimo y que, en conjunto, se necesitaban 103 pares para alcanzar los mínimos establecidos.

El informe ayuda al encargado de la tienda a identificar qué productos necesitan reposición y en qué cantidades.

Los resultados pueden cambiar cuando se registran entradas o salidas de mercadería.

Como los datos son simulados, las cantidades no representan el inventario de una tienda real.