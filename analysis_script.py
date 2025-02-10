"""
Este script analiza archivos JSON de ventas y valida la información de productos.
"""

import json

# Cargar archivos corregidos
corrected_paths = [
    "/content/TC1.Sales_cleaned.json",
    "/content/TC2.Sales_cleaned.json",
    "/content/TC3.Sales_cleaned.json"
]

for path in corrected_paths:
    try:
        with open(path, 'r', encoding="utf-8") as file:
            sales_data = json.load(file)
            print(f"✅ Archivo {path} cargado correctamente con {len(sales_data)} registros.")
    except FileNotFoundError:
        print(f"❌ Error: Archivo {path} no encontrado.")
