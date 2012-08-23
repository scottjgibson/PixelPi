

import RPi.GPIO as GPIO
import Image
import time
import argparse
import csv
import socket

#3 bytes per pixel
PIXEL_SIZE = 3

OFF = bytearray(b'\x00\x00\x00')
WHITE = bytearray(b'\xFF\xFF\xFF')
RED = bytearray(b'\xFF\x00\x00')
ORANGE = bytearray(b'\xFF\x8c\x00')
YELLOW = bytearray(b'\xFF\xFF\x00')
G2 = bytearray(b'\8F\xFF\x00')
GREEN = bytearray(b'\00\xFF\x00')
T2 = bytearray(b'\x00\xFF\x8F')
TEAL = bytearray(b'\x00\xFF\xFF')
BLUE = bytearray(b'\x00\x00\xFF')
B2 = bytearray(b'\x8F\x00\xFF')
VIOLET = bytearray(b'\xFF\x00\xFF')
V2 = bytearray(b'\xFF\x00\x8F')
rainbow = [RED, ORANGE, YELLOW, G2, GREEN, T2, TEAL, BLUE, B2, VIOLET, V2]

gamma = bytearray(256)

# Apply Gamma Correction and RGB / GRB reordering
# Optionally perform brightness adjustment
def filter_pixel(input_pixel, brightness):
    input_pixel[0] = int(brightness * input_pixel[0])
    input_pixel[1] = int(brightness * input_pixel[1])
    input_pixel[2] = int(brightness * input_pixel[2])
    output_pixel = bytearray(PIXEL_SIZE)
    if args.chip_type == "LDP8806":
        # Convert RGB into GRB bytearray list.
        output_pixel[0] = gamma[input_pixel[1]]
        output_pixel[1] = gamma[input_pixel[0]]
        output_pixel[2] = gamma[input_pixel[2]]
    else:
        output_pixel[0] = gamma[input_pixel[0]]
        output_pixel[1] = gamma[input_pixel[1]]
        output_pixel[2] = gamma[input_pixel[2]]
    return output_pixel


parser = argparse.ArgumentParser(add_help=True,version='1.0')
parser.add_argument('--chip',
        action='store',
        dest='chip_type',
        default='WS2801',
        choices=['WS2801', 'LDP8806'],
        help='Specify chip type LDP8806 or WS2801')
parser.add_argument('--filename',
        action='store',
        dest='filename',
        required=False,
        help='Specify the image file eg: hello.png')
parser.add_argument('--mode',
        action='store',
        dest='mode',
        required=True,
        choices=['pixelinvaders', 'all_off', 'all_on', 'strip', 'array', 'fade', 'chase'],
        help='Choose the display mode, either POV strip or 2D array, color, chase')
parser.add_argument('--verbose',
        action='store_true',
        dest='verbose',
        default=True,
        help='enable verbose mode')
parser.add_argument('--array_width',
        action='store',
        dest='array_width',
        required=False,
        type=int,
        default='7',
        help='Set the X dimension of your pixel array (width)')
parser.add_argument('--array_height',
        action='store',
        dest='array_height',
        required=False,
        type=int,
        default='7',
        help='Set the Y dimension of your pixel array (height)')
parser.add_argument('--spi_dev',
        action='store',
        dest='spi_dev_name',
        required=False,
        default='/dev/spidev0.0',
        help='Set the SPI device descriptor')
parser.add_argument('--refresh_rate',
        action='store',
        dest='refresh_rate',
        required=False,
        default=500,
        type=int,
        help='Set the refresh rate in ms (default 500ms)')
parser.add_argument('--num_leds',
        action='store',
        dest='num_leds',
        required=False,
        default=50,
        type=int,  help='Set the  number of LEDs in the string (used in fade and chase mode)')
parser.add_argument('--udp-ip',
	action='store',
	dest='UDP_IP',
	required=False,
	default='192.168.1.1',
	help='Used for PixelInvaders mode, listening address')
parser.add_argument('--udp-port',
	action='store',
	dest='UDP_PORT',
	required=False,
	default=6803,
	type=int,
	help='Used for PixelInvaders mode, listening port')
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
    for i in range(256):
        gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

if args.chip_type == "WS2801":
    for i in range(256):
        gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0 )

if args.mode == 'pixelinvaders':
	print ("Start PixelInvaders listener "+args.UDP_IP+":"+str(args.UDP_PORT))
	sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
    sock.bind( (UDP_IP,UDP_PORT) )
    while True:
        data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes blocking call
        spidev.write(data)
        spidev.flush()
=======
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
        column[x] = bytearray(height * PIXEL_SIZE + 1)


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
    pixel_output = bytearray(width * height * PIXEL_SIZE + 1)
    for array_index in range(len(pixel_map)):
        value = pixels[int(pixel_map[array_index][0]), int(pixel_map[array_index][1])]
	pixel_output[(array_index * PIXEL_SIZE)] = filter_pixel[value:, 1]
    print "Displaying..."
    while True:
        spidev.write(pixel_output)
        spidev.flush()
        time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'all_off':
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    spidev.write(pixel_output)
    spidev.flush()
    time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'all_on':
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    
    for led in range(args.num_leds):
        pixel_output[led*PIXEL_SIZE:] = WHITE
    
    spidev.write(pixel_output)
    spidev.flush()
    time.sleep((args.refresh_rate)/1000.0)


if args.mode == 'fade':
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    current_color = bytearray(PIXEL_SIZE)

    while True:
        for color in rainbow:
            for brightness in [x*0.01 for x in range(0,100)]:
                current_color[:] = filter_pixel(color[:], brightness)
                for pixel_offset in [(x * 3) for x in range(args.num_leds)]:
			pixel_output[pixel_offset:] = current_color[:]
                spidev.write(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)
            for brightness in [x*0.01 for x in range(100,0, -1)]:
                current_color[:] = filter_pixel(color[:], brightness)
                for pixel_offset in [(x * 3) for x in range(args.num_leds)]:
			pixel_output[pixel_offset:] = current_color[:]
                spidev.write(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)

if args.mode == 'chase':
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    current_color = bytearray(PIXEL_SIZE)
    pixel_index = 0
    while True:
        for current_color[:] in rainbow:
	    for pixel_index in range(args.num_leds+1):
                pixel_output[((pixel_index-2)*PIXEL_SIZE):] = filter_pixel(current_color[:],0.2) 
                pixel_output[((pixel_index-1)*PIXEL_SIZE):] = filter_pixel(current_color[:],0.4) 
                pixel_output[((pixel_index)*PIXEL_SIZE):] = filter_pixel(current_color[:], 1)
		pixel_output += '\x00'* ((args.num_leds+1-pixel_index)*PIXEL_SIZE)
                spidev.write(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)
                pixel_output[((pixel_index-2)*PIXEL_SIZE):] = filter_pixel(current_color[:], 0)


