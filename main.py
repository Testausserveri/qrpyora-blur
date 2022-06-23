from util import blurQRCodes
import argparse
import cv2

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', required=True, dest='filename', help='Input image')
parser.add_argument('-o', '--output', required=True, dest='outputfile', help='Output file')
parser.add_argument('-d', '--data', dest='data', help='Specific data to blur')

args = parser.parse_args()
imageName = args.filename
outputName = args.outputfile
dataFilter = ''
if args.data: dataFilter = args.data

img = blurQRCodes(imageName, dataFilter)
if len(img) == 0:
  print("Blurred image is None")
else:
  cv2.imwrite(outputName, img)