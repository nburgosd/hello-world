#!/usr/bin/env python3
"""
Ejemplo simple de lectura de código de barras
"""

import cv2
from pyzbar import pyzbar


def read_barcode(image_path):
    """
    Función simple para leer códigos de barras
    """
    # Cargar imagen
    image = cv2.imread(image_path)

    # Decodificar códigos de barras
    barcodes = pyzbar.decode(image)

    # Mostrar resultados
    for barcode in barcodes:
        # Convertir datos a string
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type

        print(f"Tipo: {barcode_type}")
        print(f"Datos: {barcode_data}")
        print("-" * 30)


# Ejemplo de uso
if __name__ == "__main__":
    # Reemplaza 'ruta_imagen.jpg' con la ruta a tu imagen
    read_barcode('ejemplo.jpg')
