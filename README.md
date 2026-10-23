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
6. Salir.

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