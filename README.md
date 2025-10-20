# Lector de Códigos de Barras - Python + pyzbar + OpenCV

Herramienta para leer y decodificar códigos de barras desde imágenes o webcam en tiempo real.

## Características

- Lee códigos de barras desde imágenes
- Soporte para múltiples formatos (QR, EAN, UPC, Code128, etc.)
- Lectura en tiempo real desde webcam
- Visualización de códigos detectados
- Exportación de resultados

## Instalación rápida

```bash
# Instalar dependencias del sistema (Linux)
sudo apt-get install libzbar0

# Instalar paquetes Python
pip install -r requirements.txt
```

Ver [INSTALL.md](INSTALL.md) para instrucciones detalladas.

## Uso

### 1. Leer desde imagen

```bash
# Básico
python3 barcode_reader.py imagen.jpg

# Con visualización
python3 barcode_reader.py imagen.jpg --show
```

### 2. Webcam en tiempo real

```bash
python3 barcode_webcam.py
```

### 3. Ejemplo simple en código

```python
import cv2
from pyzbar import pyzbar

# Cargar imagen
image = cv2.imread('imagen.jpg')

# Decodificar códigos
barcodes = pyzbar.decode(image)

# Mostrar resultados
for barcode in barcodes:
    print(f"Tipo: {barcode.type}")
    print(f"Datos: {barcode.data.decode('utf-8')}")
```

## Archivos del proyecto

- `barcode_reader.py` - Script principal con argumentos CLI
- `barcode_reader_simple.py` - Ejemplo simple y minimalista
- `barcode_webcam.py` - Lectura en tiempo real desde webcam
- `example_usage.py` - Múltiples ejemplos de uso
- `requirements.txt` - Dependencias Python
- `INSTALL.md` - Instrucciones de instalación detalladas

## Formatos soportados

QR Code, EAN-13, EAN-8, UPC-A, UPC-E, Code 39, Code 128, ITF, Codabar, DataBar, PDF417

## Requisitos

- Python 3.7+
- OpenCV (opencv-python)
- pyzbar
- libzbar (librería del sistema)
