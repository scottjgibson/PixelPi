

import RPi.GPIO as GPIO
import Image
import time
import argparse
import csv
import socket

parser = argparse.ArgumentParser(add_help=True, version='1.0')
parser.add_argument('--chip', action='store', dest='chip_type', default='WS2801', choices=['WS2801', 'LDP8806'], help='Specify chip type LDP8806 or WS2801')
parser.add_argument('--filename', action='store', dest='filename', required=False, help='Specify the image file eg: hello.png')
parser.add_argument('--mode', action='store', dest='mode', required=True, choices=['pixelinvaders', 'all_off', 'all_on', 'strip', 'array', 'fade', 'chase', 'chase_fancy'], help='Choose the display mode, either POV strip or 2D array, color, chase, chase_fancy')
parser.add_argument('--verbose', action='store_true', dest='verbose', default=True, help='enable verbose mode')
parser.add_argument('--array_width', action='store', dest='array_width', required=False,  type=int, default='7', help='Set the X dimension of your pixel array (width)')
parser.add_argument('--array_height', action='store', dest='array_height', required=False,  type=int, default='7', help='Set the Y dimension of your pixel array (height)')
parser.add_argument('--spi_dev', action='store', dest='spi_dev_name', required=False, default='/dev/spidev0.0', help='Set the SPI device descriptor')
parser.add_argument('--refresh_rate', action='store', dest='refresh_rate', required=False, default=500, type=int,  help='Set the refresh rate in ms (default 500ms)')
parser.add_argument('--num_leds', action='store', dest='num_leds', required=False, default=50, type=int,  help='Set the  number of LEDs in the string (used in fade and chase mode)')
parser.add_argument('--udp-ip', action='store', dest='UDP_IP', required=False, default='192.168.1.1', help='Used for PixelInvaders mode, listening address')
parser.add_argument('--udp-port', action='store', dest='UDP_PORT', required=False, default=6803, type=int, help='Used for PixelInvaders mode, listening port')
args = parser.parse_args()

print "Chip Type             = %s" % args.chip_type
print "File Name             = %s" % args.filename
print "Display Mode          = %s" % args.mode
print "SPI Device Descriptor = %s" % args.spi_dev_name
print "Refresh Rate          = %s" % args.refresh_rate
print "Array Dimensions      = %dx%d" % (args.array_width, args.array_height)

# Open SPI device, load image in RGB format and get dimensions:
spidev = file(args.spi_dev_name, "wb")
if args.mode == ('array', 'strip'):
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

if args.chip_type == "WS2801":
	gamma = bytearray(256)
	for i in range(256):
		gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0 )

if args.mode == 'pixelinvaders':
	print ("Start PixelInvaders listener "+args.UDP_IP+":"+str(args.UDP_PORT))
	sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
	sock.bind( (args.UDP_IP,args.UDP_PORT) )
	while True:
		data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes blocking call
		spidev.write(data)
		spidev.flush()


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
		time.sleep((args.refresh_rate/100.0))

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
			pixel_output[array_index * 3] = gamma[value[0]]
			pixel_output[array_index * 3 + 1] = gamma[value[1]]
			pixel_output[array_index * 3 + 2] = gamma[value[2]]
	print "Displaying..."
	while True:
		spidev.write(pixel_output)
		spidev.flush()
		time.sleep((args.refresh_rate)/1000.0)
if args.mode == 'all_off':
	pixel_output = bytearray(args.num_leds * 3 + 3)
	print "Displaying..."
	current_color = bytearray(3)

	spidev.write(pixel_output)
	spidev.flush()
	time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'all_on':
	pixel_output = bytearray(args.num_leds * 3 + 3)
	print "Displaying..."
	current_color = bytearray(3)
	current_color[0] = 255
	current_color[1] = 255
	current_color[2] = 255
	
	for led in range(args.num_leds):
		pixel_output[led*3] = current_color[0]
		pixel_output[led*3 + 1] = current_color[1]
		pixel_output[led*3 + 2] = current_color[2]
	

	spidev.write(pixel_output)
	spidev.flush()
	time.sleep((args.refresh_rate)/1000.0)


if args.mode == 'fade':
	pixel_output = bytearray(args.num_leds * 3 + 3)
	print "Displaying..."
	current_color = bytearray(3)


	while True:
		for color in ('red', 'green', 'blue'):
			for brightness in range(255):
				if color == 'red':
					current_color[0] = brightness
					current_color[1] = 0
					current_color[2] = 0
				if color == 'green':
					current_color[0] = 0
					current_color[1] = brightness
					current_color[2] = 0
				if color == 'blue':
					current_color[0] = 0
					current_color[1] = 0
					current_color[2] = brightness

				for pixel in range(args.num_leds):
					if args.chip_type == "LDP8806":
						# Convert RGB into column-wise GRB bytearray list.
						pixel_output[pixel * 3] = gamma[current_color[1]]
						pixel_output[pixel * 3 + 1] = gamma[current_color[0]]
						pixel_output[pixel * 3 + 2] = gamma[current_color[2]]
					else:
						pixel_output[pixel * 3] = gamma[current_color[0]]
						pixel_output[pixel * 3 + 1] = gamma[current_color[1]]
						pixel_output[pixel * 3 + 2] = gamma[current_color[2]]
				spidev.write(pixel_output)
				spidev.flush()
				time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'chase':
	pixel_output = bytearray(args.num_leds * 3 + 3)
	print "Displaying..."
	a = 0
	dir = 0
	current_color = bytearray(3)

	while True:
		for color in ('red', 'green', 'blue'):
			if color == 'red':
				current_color[0] = 255
				current_color[1] = 0
				current_color[2] = 0
			if color == 'green':
				current_color[0] = 0
				current_color[1] = 255
				current_color[2] = 0
			if color == 'blue':
				current_color[0] = 0
				current_color[1] = 0
				current_color[2] = 255

			while True:
				if dir == 0:
					if a != 49:
						a = a+1
					else:
						dir = 1
				else:
					if a != 0:
						a = a - 1
					else:
						dir = 0
						break

				for pixel in range(50):
					pixel_output[pixel * 3] = 0
					pixel_output[pixel * 3 + 1] = 0
					pixel_output[pixel * 3 + 2] = 0
				if args.chip_type == "LDP8806":
					# Convert RGB into column-wise GRB bytearray list.
					pixel_output[a * 3] = gamma[current_color[1]]
					pixel_output[a * 3 + 1] = gamma[current_color[0]]
					pixel_output[a * 3 + 2] = gamma[current_color[2]]
				else:
					pixel_output[a * 3] = gamma[current_color[0]]
					pixel_output[a * 3 + 1] = gamma[current_color[1]]
					pixel_output[a * 3 + 2] = gamma[current_color[2]]
				spidev.write(pixel_output)
				spidev.flush()
				time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'chase_fancy':
	pixel_output = bytearray(args.num_leds * 3 + 3)
	print "Displaying..."
	a = 0
	flame = bytearray(4*3)
	flame[0]= 255;
	flame[1] = 255
	flame[2] = 0
	flame[3]= 255;
	flame[4] = 45
	flame[5] = 0
	flame[6]= 255;
	flame[7] = 0
	flame[2] = 0
	flame[9]= 0;
	flame[10] = 0
	flame[11] = 0

	while True:
#		for color in ('red', 'green', 'blue'):
#			if color == 'red':
#				current_color[0] = 255
#				current_color[1] = 0
#				current_color[2] = 0
#			if color == 'green':
#				current_color[0] = 0
#				current_color[1] = 255
#				current_color[2] = 0
#			if color == 'blue':
#				current_color[0] = 0
#				current_color[1] = 0
#				current_color[2] = 255

			while True:
				#turn off 
				pixel_output[pixel * 3] = 0
				pixel_output[pixel * 3 + 1] = 0
				pixel_output[pixel * 3 + 2] = 0

				if a != 49:
					a = a+1
				else:
					a = 0

				for pixel in range(50):
					pixel_output[pixel * 3] = 0
					pixel_output[pixel * 3 + 1] = 0
					pixel_output[pixel * 3 + 2] = 0
				if args.chip_type == "LDP8806":
					# Convert RGB into column-wise GRB bytearray list.
					pixel_output[a * 3] = gamma[current_color[1]]
					pixel_output[a * 3 + 1] = gamma[current_color[0]]
					pixel_output[a * 3 + 2] = gamma[current_color[2]]
				else:
					pixel_output[a * 3] = gamma[current_color[0]]
					pixel_output[a * 3 + 1] = gamma[current_color[1]]
					pixel_output[a * 3 + 2] = gamma[current_color[2]]
				spidev.write(pixel_output)
				spidev.flush()
				time.sleep((args.refresh_rate)/1000.0)




