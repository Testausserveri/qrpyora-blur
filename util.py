from pyzbar import pyzbar
import cv2
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def blurQRCodes(fileName, data):
  img = Image.open(fileName)
  qr_data = pyzbar.decode(cv2.imread(fileName))

  if len(qr_data) == 0:
    print("No QR code found")
    return []

  image = cv2.imread(fileName)
  blurred_image = cv2.GaussianBlur(image,(43, 43), 30)
  listOfCorners = []
  for qr in qr_data:
    if data and qr.data.decode('utf-8') != data:
      continue
    listOfCorners.append([(qr.polygon[0].x, qr.polygon[0].y), (qr.polygon[1].x, qr.polygon[1].y),(qr.polygon[2].x, qr.polygon[2].y), (qr.polygon[3].x, qr.polygon[3].y)])
  roi_corners = np.array(listOfCorners,dtype = np.int32)
  mask = np.zeros(image.shape, dtype=np.uint8)
  channel_count = image.shape[2]
  ignore_mask_color = (255,)*channel_count
  cv2.fillPoly(mask, roi_corners, ignore_mask_color)
  mask_inverse = np.ones(mask.shape).astype(np.uint8)*255 - mask
  final_image = cv2.bitwise_and(blurred_image, mask) + cv2.bitwise_and(image, mask_inverse)
  return final_image