#!/usr/bin/env python3
"""
Lector de códigos de barras usando pyzbar y OpenCV
Soporta múltiples formatos: QR, EAN, UPC, Code128, etc.
"""

import cv2
from pyzbar import pyzbar
import argparse
import sys


def decode_barcodes(image_path, show_image=False):
    """
    Lee y decodifica códigos de barras desde una imagen

    Args:
        image_path (str): Ruta a la imagen
        show_image (bool): Si True, muestra la imagen con los códigos detectados

    Returns:
        list: Lista de diccionarios con la información de los códigos detectados
    """
    # Cargar la imagen
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: No se pudo cargar la imagen desde {image_path}")
        return []

    # Decodificar los códigos de barras en la imagen
    barcodes = pyzbar.decode(image)

    results = []

    # Procesar cada código de barras detectado
    for barcode in barcodes:
        # Extraer la información del código de barras
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type

        # Obtener las coordenadas del rectángulo que rodea el código
        x, y, w, h = barcode.rect

        # Guardar información
        results.append({
            'data': barcode_data,
            'type': barcode_type,
            'rect': (x, y, w, h)
        })

        # Imprimir la información
        print(f"\n[Código detectado]")
        print(f"  Tipo: {barcode_type}")
        print(f"  Datos: {barcode_data}")
        print(f"  Posición: x={x}, y={y}, ancho={w}, alto={h}")

        if show_image:
            # Dibujar un rectángulo alrededor del código de barras
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Agregar el texto del código de barras
            text = f"{barcode_type}: {barcode_data}"
            cv2.putText(image, text, (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar la imagen con los códigos detectados
    if show_image and len(results) > 0:
        cv2.imshow('Codigos de Barras Detectados', image)
        print("\nPresiona cualquier tecla para cerrar la ventana...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Lector de códigos de barras desde imágenes'
    )
    parser.add_argument(
        'image',
        help='Ruta a la imagen con el código de barras'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='Mostrar la imagen con los códigos detectados'
    )

    args = parser.parse_args()

    print(f"Analizando imagen: {args.image}")
    print("-" * 50)

    results = decode_barcodes(args.image, args.show)

    if not results:
        print("\nNo se detectaron códigos de barras en la imagen.")
        sys.exit(1)
    else:
        print(f"\n{'='*50}")
        print(f"Total de códigos detectados: {len(results)}")


if __name__ == "__main__":
    main()
