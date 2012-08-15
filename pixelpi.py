#!/usr/bin/python

import RPi.GPIO as GPIO
import Image
import time
import argparse
import csv

parser = argparse.ArgumentParser(add_help=True, version='1.0')
parser.add_argument('--chip', action='store', dest='chip_type', default='WS2801', choices=['WS2801', 'LDP8806'], help='Specify chip type LDP8806 or WS2801')
parser.add_argument('--filename', action='store', dest='filename', required=True, help='Specify the image file eg: hello.png')
parser.add_argument('--mode', action='store', dest='mode', required=True, choices=['strip', 'array'], help='Choose the display mode, either POV strip or 2D array')
parser.add_argument('--verbose', action='store_true', dest='verbose', default=True, help='enable verbose mode')
parser.add_argument('--array_width', action='store', dest='array_width', required=False,  type=int, default='7', help='Set the X dimension of your pixel array (width)')
parser.add_argument('--array_height', action='store', dest='array_height', required=False,  type=int, default='7', help='Set the Y dimension of your pixel array (height)')
parser.add_argument('--spi_dev', action='store', dest='spi_dev_name', required=False, default='/dev/spidev0.0', help='Set the SPI device descriptor')
parser.add_argument('--refresh_rate', action='store', dest='refresh_rate', required=False, default=0.5, type=int,  help='Set the refresh rate (default 0.5 seconds)')
args = parser.parse_args()

print "Chip Type             = %s" % args.chip_type
print "File Name             = %s" % args.filename
print "Display Mode          = %s" % args.mode
print "SPI Device Descriptor = %s" % args.spi_dev_name
print "Refresh Rate          = %s" % args.refresh_rate
print "Array Dimensions      = %dx%d" % (args.array_width, args.array_height)

# Open SPI device, load image in RGB format and get dimensions:
spidev = file(args.spi_dev_name, "wb")
print "Loading..."
img = Image.open(args.filename).convert("RGB")
pixels = img.load()
width = img.size[0]
height = img.size[1]
print "%dx%d pixels" % img.size

# To do: add resize here if image is not desired height

# Calculate gamma correction table. This includes
# LPD8806-specific conversion (7-bit color w/high bit set).
if args.chip_type == "LDP8806":
	gamma = bytearray(256)
	for i in range(256):
		gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)


if args.mode == 'strip':
	# Create bytearray for the entire image
	# R, G, B byte per pixel, plus extra '0' byte at end for latch.
	print "Allocating Strip..."
	column = [0 for x in range(width)]
	for x in range(width):
		column[x] = bytearray(height * 3 + 1)


	print "Converting..."
	for x in range(width):
		for y in range(height):
			value = pixels[x, y]
			y3 = y * 3
			if args.chip_type == "LDP8806":
				# Convert RGB into column-wise GRB bytearray list.
				column[x][y3] = gamma[value[1]]
				column[x][y3 + 1] = gamma[value[0]]
				column[x][y3 + 2] = gamma[value[2]]
			else:
				column[x][y3] = value[0]
				column[x][y3 + 1] = value[1]
				column[x][y3 + 2] = value[2]

	print "Displaying..."
	while True:
		for x in range(width):
			spidev.write(column[x])
			spidev.flush()
			time.sleep(0.001)
		time.sleep(args.refresh_rate)

if args.mode == 'array':
	print "Reading in array map"

	pixel_map_csv = csv.reader(open("pixel_map.csv", "rb"))
	pixel_map = []
	for p in pixel_map_csv:
		pixel_map.append(p)

	if len(pixel_map) != args.array_width * args.array_height:
		print "Map size error"
	
	print "Remapping"
	# Create a byte array ordered according to the pixel map file
	pixel_output = bytearray(width * height * 3 + 1)
	for array_index in range(len(pixel_map)):
		value = pixels[int(pixel_map[array_index][0]), int(pixel_map[array_index][1])]
		if args.chip_type == "LDP8806":
			# Convert RGB into column-wise GRB bytearray list.
			pixel_output[array_index * 3] = gamma[value[1]]
			pixel_output[array_index * 3 + 1] = gamma[value[0]]
			pixel_output[array_index * 3+ 2] = gamma[value[2]]
		else:
			pixel_output[array_index * 3] = value[0]
			pixel_output[array_index * 3 + 1] = value[1]
			pixel_output[array_index * 3 + 2] = value[2]
	

	print "Displaying..."
	while True:
		spidev.write(pixel_output)
		spidev.flush()
		time.sleep(0.001)
		time.sleep(args.refresh_rate)




