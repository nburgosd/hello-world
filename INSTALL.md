# Instalación - Lector de Códigos de Barras

## Requisitos previos

### Linux (Ubuntu/Debian)
```bash
# Instalar dependencias del sistema
sudo apt-get update
sudo apt-get install -y python3 python3-pip libzbar0
```

### macOS
```bash
# Instalar usando Homebrew
brew install zbar
```

### Windows
Descarga e instala zbar desde: http://zbar.sourceforge.net/

O usa conda:
```bash
conda install -c conda-forge zbar
```

## Instalación de paquetes Python

```bash
# Instalar las dependencias
pip install -r requirements.txt

# O instalar manualmente
pip install opencv-python pyzbar pillow
```

## Verificar instalación

```bash
python3 -c "import cv2; import pyzbar; print('Instalación exitosa!')"
```

## Uso

### 1. Leer código de barras desde una imagen

```bash
# Básico
python3 barcode_reader.py imagen.jpg

# Con visualización
python3 barcode_reader.py imagen.jpg --show
```

### 2. Ejemplo simple

```bash
python3 barcode_reader_simple.py
```

### 3. Lectura desde webcam (tiempo real)

```bash
python3 barcode_webcam.py
```

## Formatos soportados

- QR Code
- EAN-13
- EAN-8
- UPC-A
- UPC-E
- Code 39
- Code 128
- ITF
- Codabar
- DataBar
- PDF417

## Solución de problemas

### Error: "No module named 'pyzbar'"
```bash
pip install pyzbar
```

### Error: "libzbar.so.0: cannot open shared object file"
```bash
# Linux
sudo apt-get install libzbar0

# macOS
brew install zbar
```

### La webcam no funciona
- Verifica que no esté siendo usada por otra aplicación
- Prueba cambiar el índice: `cv2.VideoCapture(1)` en lugar de `cv2.VideoCapture(0)`
