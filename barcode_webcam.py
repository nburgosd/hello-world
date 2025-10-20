#!/usr/bin/env python3
"""
Lector de códigos de barras en tiempo real desde webcam
"""

import cv2
from pyzbar import pyzbar


def read_barcode_webcam():
    """
    Lee códigos de barras en tiempo real desde la webcam
    Presiona 'q' para salir
    """
    # Inicializar la webcam
    cap = cv2.VideoCapture(0)

    print("Iniciando webcam...")
    print("Presiona 'q' para salir")

    detected_codes = set()  # Para evitar múltiples detecciones del mismo código

    while True:
        # Capturar frame por frame
        ret, frame = cap.read()

        if not ret:
            print("Error: No se pudo leer de la webcam")
            break

        # Decodificar códigos de barras en el frame actual
        barcodes = pyzbar.decode(frame)

        # Procesar cada código de barras detectado
        for barcode in barcodes:
            # Extraer datos
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Obtener coordenadas
            x, y, w, h = barcode.rect

            # Dibujar rectángulo
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Añadir texto
            text = f"{barcode_type}: {barcode_data}"
            cv2.putText(frame, text, (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Imprimir en consola (solo una vez por código)
            code_id = f"{barcode_type}:{barcode_data}"
            if code_id not in detected_codes:
                print(f"\n[Nuevo código detectado]")
                print(f"  Tipo: {barcode_type}")
                print(f"  Datos: {barcode_data}")
                detected_codes.add(code_id)

        # Mostrar el frame
        cv2.imshow('Lector de Codigos de Barras - Presiona Q para salir', frame)

        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Limpiar
    cap.release()
    cv2.destroyAllWindows()

    print(f"\nTotal de códigos únicos detectados: {len(detected_codes)}")


if __name__ == "__main__":
    read_barcode_webcam()
