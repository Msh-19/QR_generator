import segno
from PIL import Image

# Generate QR
qr = segno.make(
    'https://scan-choose.vercel.app/menu/tropical-cafe',
    error='h'
)
qr.save('qr.png', scale=10)

# Open QR and logo
qr_img = Image.open('qr.png').convert('RGBA')
logo = Image.open('TropicalLogo.jpg').convert('RGBA')

# Resize logo (25% of QR size)
qr_w, qr_h = qr_img.size
logo_size = qr_w // 4
logo = logo.resize((logo_size, logo_size))

# Center position
pos = (
    (qr_w - logo_size) // 2,
    (qr_h - logo_size) // 2
)

# Paste logo
qr_img.paste(logo, pos, mask=logo)
qr_img.save('qr_with_logo.png')
