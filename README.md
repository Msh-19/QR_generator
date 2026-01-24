# QR Generator

Simple Python utility to generate QR codes as images. Useful for encoding URLs, text, contact info, etc.

## Features
- Generate PNG (or other image formats supported by Pillow)
- CLI and library usage
- Customize size, border, error correction, and output filename

## Requirements
- Python 3.7+
- Recommended packages: qrcode, pillow
    - Install: `pip install qrcode[pil] pillow`

## Installation
Clone the repo and install dependencies:
```bash
git clone <repo-url>
cd QR_generator
pip install -r requirements.txt   # if provided
```

## Usage

Library:
```python
from qrcode import QRCode

def make_qr(data, filename='qr.png', scale=10):
        qr = QRCode(border=4, box_size=scale, error_correction=2)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

make_qr("https://example.com", "example.png")
```

CLI (example):
```bash
python generate.py --text "https://example.com" --output example.png --size 10
```

Adjust flags/names to match the project's CLI implementation.

## Contributing
- Open an issue or PR
- Keep changes minimal and document new behavior
- Include tests where applicable

## License
MIT — see LICENSE file for details

## Notes
Customize error correction, colors, and formats via qrcode/Pillow options to suit your needs.