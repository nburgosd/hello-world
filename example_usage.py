#!/usr/bin/env python3
"""
Ejemplos de uso del lector de códigos de barras
"""

import cv2
from pyzbar import pyzbar
import numpy as np


def ejemplo_basico():
    """Ejemplo básico de lectura"""
    print("=" * 60)
    print("EJEMPLO 1: Lectura básica de código de barras")
    print("=" * 60)

    image = cv2.imread('ejemplo.jpg')
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        print(f"Datos: {barcode.data.decode('utf-8')}")
        print(f"Tipo: {barcode.type}")


def ejemplo_con_procesamiento():
    """Ejemplo con preprocesamiento de imagen para mejorar detección"""
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Con preprocesamiento de imagen")
    print("=" * 60)

    image = cv2.imread('ejemplo.jpg')

    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización para mejorar contraste
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Decodificar desde imagen procesada
    barcodes = pyzbar.decode(thresh)

    print(f"Códigos detectados: {len(barcodes)}")
    for barcode in barcodes:
        print(f"  - {barcode.type}: {barcode.data.decode('utf-8')}")


def ejemplo_multiples_codigos():
    """Ejemplo procesando múltiples imágenes"""
    print("\n" + "=" * 60)
    print("EJEMPLO 3: Procesamiento de múltiples imágenes")
    print("=" * 60)

    import os

    # Lista de imágenes a procesar
    image_files = [f for f in os.listdir('.') if f.endswith(('.jpg', '.png', '.jpeg'))]

    all_results = {}

    for image_file in image_files:
        image = cv2.imread(image_file)
        if image is not None:
            barcodes = pyzbar.decode(image)
            if barcodes:
                all_results[image_file] = [
                    {
                        'type': b.type,
                        'data': b.data.decode('utf-8')
                    }
                    for b in barcodes
                ]

    print(f"Imágenes procesadas: {len(image_files)}")
    print(f"Imágenes con códigos: {len(all_results)}")

    for filename, codes in all_results.items():
        print(f"\n{filename}:")
        for code in codes:
            print(f"  {code['type']}: {code['data']}")


def ejemplo_guardar_resultados():
    """Ejemplo guardando resultados en archivo"""
    print("\n" + "=" * 60)
    print("EJEMPLO 4: Guardar resultados en archivo")
    print("=" * 60)

    import json

    image = cv2.imread('ejemplo.jpg')
    barcodes = pyzbar.decode(image)

    results = []
    for barcode in barcodes:
        results.append({
            'type': barcode.type,
            'data': barcode.data.decode('utf-8'),
            'quality': barcode.quality,
            'rect': {
                'x': barcode.rect.left,
                'y': barcode.rect.top,
                'width': barcode.rect.width,
                'height': barcode.rect.height
            }
        })

    # Guardar como JSON
    with open('barcode_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("Resultados guardados en: barcode_results.json")
    print(f"Total de códigos: {len(results)}")


def ejemplo_filtrar_por_tipo():
    """Ejemplo filtrando por tipo de código"""
    print("\n" + "=" * 60)
    print("EJEMPLO 5: Filtrar por tipo de código de barras")
    print("=" * 60)

    image = cv2.imread('ejemplo.jpg')
    barcodes = pyzbar.decode(image)

    # Filtrar solo códigos QR
    qr_codes = [b for b in barcodes if b.type == 'QRCODE']

    # Filtrar códigos EAN
    ean_codes = [b for b in barcodes if b.type in ['EAN13', 'EAN8']]

    print(f"Códigos QR: {len(qr_codes)}")
    for qr in qr_codes:
        print(f"  {qr.data.decode('utf-8')}")

    print(f"\nCódigos EAN: {len(ean_codes)}")
    for ean in ean_codes:
        print(f"  {ean.data.decode('utf-8')}")


if __name__ == "__main__":
    print("\nEJEMPLOS DE USO - Lector de Códigos de Barras")
    print("=" * 60)
    print("\nNOTA: Estos ejemplos requieren una imagen llamada 'ejemplo.jpg'")
    print("con códigos de barras para funcionar correctamente.\n")

    try:
        ejemplo_basico()
        ejemplo_con_procesamiento()
        ejemplo_multiples_codigos()
        ejemplo_guardar_resultados()
        ejemplo_filtrar_por_tipo()

        print("\n" + "=" * 60)
        print("Todos los ejemplos ejecutados correctamente")
        print("=" * 60)

    except FileNotFoundError:
        print("\nError: No se encontró la imagen 'ejemplo.jpg'")
        print("Por favor, coloca una imagen con códigos de barras en el directorio actual")
    except Exception as e:
        print(f"\nError: {e}")
