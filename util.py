from pyzbar import pyzbar
import cv2
from PIL import Image, ImageDraw, ImageFilter

def blurQRCodes(fileName, data):
  img = Image.open(fileName)
  qr_data = pyzbar.decode(cv2.imread(fileName))

  if len(qr_data) == 0:
    print("No QR code found")
    return
  img1 = ImageDraw.Draw(img)  

  for qr in qr_data:
    if data and qr.data.decode('utf-8') != data:
      continue
    shape = [(qr.polygon[0].x, qr.polygon[0].y), (qr.polygon[2].x, qr.polygon[2].y)]
    shape2 = [(qr.polygon[1].x, qr.polygon[1].y), (qr.polygon[3].x, qr.polygon[3].y)]
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle(shape, fill=255);
    draw.rectangle(shape2, fill=255)
    blurred = img.filter(ImageFilter.GaussianBlur(10))

    # Paste blurred region and save result
    img.paste(blurred, mask=mask)
  return img