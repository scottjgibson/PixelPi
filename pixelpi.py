import cwiid
import sys
import RPi.GPIO as GPIO
import Image
import time
import argparse
import csv
import socket

#3 bytes per pixel
PIXEL_SIZE = 3

AQUA = bytearray(b'\x00\xff\xff')
AQUAMARINE = bytearray(b'\x7f\xff\xd4')
AZURE = bytearray(b'\xf0\xff\xff')
BEIGE = bytearray(b'\xf5\xf5\xdc')
BISQUE = bytearray(b'\xff\xe4\xc4')
BLANCHEDALMOND = bytearray(b'\xff\xeb\xcd')
BLUE = bytearray(b'\x00\x00\xff')
BLUEVIOLET = bytearray(b'\x8a\x2b\xe2')
BROWN = bytearray(b'\xa5\x2a\x2a')
BURLYWOOD = bytearray(b'\xde\xb8\x87')
CADETBLUE = bytearray(b'\x5f\x9e\xa0')
CHARTREUSE = bytearray(b'\x7f\xff\x00')
CHOCOLATE = bytearray(b'\xd2\x69\x1e')
CORAL = bytearray(b'\xff\x7f\x50')
CORNFLOWERBLUE = bytearray(b'\x64\x95\xed')
CORNSILK = bytearray(b'\xff\xf8\xdc')
CRIMSON = bytearray(b'\xdc\x14\x3c')
CYAN = bytearray(b'\x00\xff\xff')
DARKBLUE = bytearray(b'\x00\x00\x8b')
DARKCYAN = bytearray(b'\x00\x8b\x8b')
DARKGOLDENROD = bytearray(b'\xb8\x86\x0b')
DARKGRAY = bytearray(b'\xa9\xa9\xa9')
DARKGREY = bytearray(b'\xa9\xa9\xa9')
DARKGREEN = bytearray(b'\x00\x64\x00')
DARKKHAKI = bytearray(b'\xbd\xb7\x6b')
DARKMAGENTA = bytearray(b'\x8b\x00\x8b')
DARKOLIVEGREEN = bytearray(b'\x55\x6b\x2f')
DARKORANGE = bytearray(b'\xff\x8c\x00')
DARKORCHID = bytearray(b'\x99\x32\xcc')
DARKRED = bytearray(b'\x8b\x00\x00')
DARKSALMON = bytearray(b'\xe9\x96\x7a')
DARKSEAGREEN = bytearray(b'\x8f\xbc\x8f')
DARKSLATEBLUE = bytearray(b'\x48\x3d\x8b')
DARKSLATEGRAY = bytearray(b'\x2f\x4f\x4f')
DARKSLATEGREY = bytearray(b'\x2f\x4f\x4f')
DARKTURQUOISE = bytearray(b'\x00\xce\xd1')
DARKVIOLET = bytearray(b'\x94\x00\xd3')
DEEPPINK = bytearray(b'\xff\x14\x93')
DEEPSKYBLUE = bytearray(b'\x00\xbf\xff')
DIMGRAY = bytearray(b'\x69\x69\x69')
DIMGREY = bytearray(b'\x69\x69\x69')
DODGERBLUE = bytearray(b'\x1e\x90\xff')
FIREBRICK = bytearray(b'\xb2\x22\x22')
FLORALWHITE = bytearray(b'\xff\xfa\xf0')
FORESTGREEN = bytearray(b'\x22\x8b\x22')
FUCHSIA = bytearray(b'\xff\x00\xff')
GAINSBORO = bytearray(b'\xdc\xdc\xdc')
GHOSTWHITE = bytearray(b'\xf8\xf8\xff')
GOLD = bytearray(b'\xff\xd7\x00')
GOLDENROD = bytearray(b'\xda\xa5\x20')
GRAY = bytearray(b'\x80\x80\x80')
GREY = bytearray(b'\x80\x80\x80')
GREEN = bytearray(b'\x00\x80\x00')
GREENYELLOW = bytearray(b'\xad\xff\x2f')
HONEYDEW = bytearray(b'\xf0\xff\xf0')
HOTPINK = bytearray(b'\xff\x69\xb4')
INDIANRED = bytearray(b'\xcd\x5c\x5c')
INDIGO = bytearray(b'\x4b\x00\x82')
IVORY = bytearray(b'\xff\xff\xf0')
KHAKI = bytearray(b'\xf0\xe6\x8c')
LAVENDER = bytearray(b'\xe6\xe6\xfa')
LAVENDERBLUSH = bytearray(b'\xff\xf0\xf5')
LAWNGREEN = bytearray(b'\x7c\xfc\x00')
LEMONCHIFFON = bytearray(b'\xff\xfa\xcd')
LIGHTBLUE = bytearray(b'\xad\xd8\xe6')
LIGHTCORAL = bytearray(b'\xf0\x80\x80')
LIGHTCYAN = bytearray(b'\xe0\xff\xff')
LIGHTGOLDENRODYELLOW = bytearray(b'\xfa\xfa\xd2')
LIGHTGRAY = bytearray(b'\xd3\xd3\xd3')
LIGHTGREY = bytearray(b'\xd3\xd3\xd3')
LIGHTGREEN = bytearray(b'\x90\xee\x90')
LIGHTPINK = bytearray(b'\xff\xb6\xc1')
LIGHTSALMON = bytearray(b'\xff\xa0\x7a')
LIGHTSEAGREEN = bytearray(b'\x20\xb2\xaa')
LIGHTSKYBLUE = bytearray(b'\x87\xce\xfa')
LIGHTSLATEGRAY = bytearray(b'\x77\x88\x99')
LIGHTSLATEGREY = bytearray(b'\x77\x88\x99')
LIGHTSTEELBLUE = bytearray(b'\xb0\xc4\xde')
LIGHTYELLOW = bytearray(b'\xff\xff\xe0')
LIME = bytearray(b'\x00\xff\x00')
LIMEGREEN = bytearray(b'\x32\xcd\x32')
LINEN = bytearray(b'\xfa\xf0\xe6')
MAGENTA = bytearray(b'\xff\x00\xff')
MAROON = bytearray(b'\x80\x00\x00')
MEDIUMAQUAMARINE = bytearray(b'\x66\xcd\xaa')
MEDIUMBLUE = bytearray(b'\x00\x00\xcd')
MEDIUMORCHID = bytearray(b'\xba\x55\xd3')
MEDIUMPURPLE = bytearray(b'\x93\x70\xd8')
MEDIUMSEAGREEN = bytearray(b'\x3c\xb3\x71')
MEDIUMSLATEBLUE = bytearray(b'\x7b\x68\xee')
MEDIUMSPRINGGREEN = bytearray(b'\x00\xfa\x9a')
MEDIUMTURQUOISE = bytearray(b'\x48\xd1\xcc')
MEDIUMVIOLETRED = bytearray(b'\xc7\x15\x85')
MIDNIGHTBLUE = bytearray(b'\x19\x19\x70')
MINTCREAM = bytearray(b'\xf5\xff\xfa')
MISTYROSE = bytearray(b'\xff\xe4\xe1')
MOCCASIN = bytearray(b'\xff\xe4\xb5')
NAVAJOWHITE = bytearray(b'\xff\xde\xad')
NAVY = bytearray(b'\x00\x00\x80')
OLDLACE = bytearray(b'\xfd\xf5\xe6')
OLIVE = bytearray(b'\x80\x80\x00')
OLIVEDRAB = bytearray(b'\x6b\x8e\x23')
ORANGE = bytearray(b'\xff\xa5\x00')
ORANGERED = bytearray(b'\xff\x45\x00')
ORCHID = bytearray(b'\xda\x70\xd6')
PALEGOLDENROD = bytearray(b'\xee\xe8\xaa')
PALEGREEN = bytearray(b'\x98\xfb\x98')
PALETURQUOISE = bytearray(b'\xaf\xee\xee')
PALEVIOLETRED = bytearray(b'\xd8\x70\x93')
PAPAYAWHIP = bytearray(b'\xff\xef\xd5')
PEACHPUFF = bytearray(b'\xff\xda\xb9')
PERU = bytearray(b'\xcd\x85\x3f')
PINK = bytearray(b'\xff\xc0\xcb')
PLUM = bytearray(b'\xdd\xa0\xdd')
POWDERBLUE = bytearray(b'\xb0\xe0\xe6')
PURPLE = bytearray(b'\x80\x00\x80')
RED = bytearray(b'\xff\x00\x00')
ROSYBROWN = bytearray(b'\xbc\x8f\x8f')
ROYALBLUE = bytearray(b'\x41\x69\xe1')
SADDLEBROWN = bytearray(b'\x8b\x45\x13')
SALMON = bytearray(b'\xfa\x80\x72')
SANDYBROWN = bytearray(b'\xf4\xa4\x60')
SEAGREEN = bytearray(b'\x2e\x8b\x57')
SEASHELL = bytearray(b'\xff\xf5\xee')
SIENNA = bytearray(b'\xa0\x52\x2d')
SILVER = bytearray(b'\xc0\xc0\xc0')
SKYBLUE = bytearray(b'\x87\xce\xeb')
SLATEBLUE = bytearray(b'\x6a\x5a\xcd')
SLATEGRAY = bytearray(b'\x70\x80\x90')
SLATEGREY = bytearray(b'\x70\x80\x90')
SNOW = bytearray(b'\xff\xfa\xfa')
SPRINGGREEN = bytearray(b'\x00\xff\x7f')
STEELBLUE = bytearray(b'\x46\x82\xb4')
TAN = bytearray(b'\xd2\xb4\x8c')
TEAL = bytearray(b'\x00\x80\x80')
THISTLE = bytearray(b'\xd8\xbf\xd8')
TOMATO = bytearray(b'\xff\x63\x47')
TURQUOISE = bytearray(b'\x40\xe0\xd0')
VIOLET = bytearray(b'\xee\x82\xee')
WHEAT = bytearray(b'\xf5\xde\xb3')
WHITE = bytearray(b'\xff\xff\xff')
WHITESMOKE = bytearray(b'\xf5\xf5\xf5')
YELLOW = bytearray(b'\xff\xff\x00')
YELLOWGREEN = bytearray(b'\x9a\xcd\x32')
RAINBOW = [AQUA, AQUAMARINE, AZURE, BEIGE, BISQUE, BLANCHEDALMOND, BLUE, BLUEVIOLET, BROWN, BURLYWOOD, CADETBLUE, CHARTREUSE, CHOCOLATE, CORAL, CORNFLOWERBLUE, CORNSILK, CRIMSON, CYAN, DARKBLUE, DARKCYAN, DARKGOLDENROD, DARKGRAY, DARKGREY, DARKGREEN, DARKKHAKI, DARKMAGENTA, DARKOLIVEGREEN, DARKORANGE, DARKORCHID, DARKRED, DARKSALMON, DARKSEAGREEN, DARKSLATEBLUE, DARKSLATEGRAY, DARKSLATEGREY, DARKTURQUOISE, DARKVIOLET, DEEPPINK, DEEPSKYBLUE, DIMGRAY, DIMGREY, DODGERBLUE, FIREBRICK, FLORALWHITE, FORESTGREEN, FUCHSIA, GAINSBORO, GHOSTWHITE, GOLD, GOLDENROD, GRAY, GREY, GREEN, GREENYELLOW, HONEYDEW, HOTPINK, INDIANRED, INDIGO, IVORY, KHAKI, LAVENDER, LAVENDERBLUSH, LAWNGREEN, LEMONCHIFFON, LIGHTBLUE, LIGHTCORAL, LIGHTCYAN, LIGHTGOLDENRODYELLOW, LIGHTGRAY, LIGHTGREY, LIGHTGREEN, LIGHTPINK, LIGHTSALMON, LIGHTSEAGREEN, LIGHTSKYBLUE, LIGHTSLATEGRAY, LIGHTSLATEGREY, LIGHTSTEELBLUE, LIGHTYELLOW, LIME, LIMEGREEN, LINEN, MAGENTA, MAROON, MEDIUMAQUAMARINE, MEDIUMBLUE, MEDIUMORCHID, MEDIUMPURPLE, MEDIUMSEAGREEN, MEDIUMSLATEBLUE, MEDIUMSPRINGGREEN, MEDIUMTURQUOISE, MEDIUMVIOLETRED, MIDNIGHTBLUE, MINTCREAM, MISTYROSE, MOCCASIN, NAVAJOWHITE, NAVY, OLDLACE, OLIVE, OLIVEDRAB, ORANGE, ORANGERED, ORCHID, PALEGOLDENROD, PALEGREEN, PALETURQUOISE, PALEVIOLETRED, PAPAYAWHIP, PEACHPUFF, PERU, PINK, PLUM, POWDERBLUE, PURPLE, RED, ROSYBROWN, ROYALBLUE, SADDLEBROWN, SALMON, SANDYBROWN, SEAGREEN, SEASHELL, SIENNA, SILVER, SKYBLUE, SLATEBLUE, SLATEGRAY, SLATEGREY, SNOW, SPRINGGREEN, STEELBLUE, TAN, TEAL, THISTLE, TOMATO, TURQUOISE, VIOLET, WHEAT, WHITE, WHITESMOKE, YELLOW, YELLOWGREEN, YELLOWGREEN]

def write_stream(pixels):
    if args.chip_type == "LPD6803":
        pixel_out_bytes = bytearray(2)
        spidev.write(bytearray(b'\x00\x00'))
        pixel_count = len(pixels) / PIXEL_SIZE
        for pixel_index in range(pixel_count):
            
            pixel_in = bytearray(pixels[(pixel_index * PIXEL_SIZE):((pixel_index * PIXEL_SIZE) + PIXEL_SIZE)])

            pixel_out = 0b1000000000000000 # bit 16 must be ON
            pixel_out |= (pixel_in[0] & 0x00F8) << 7 # RED is bits 11-15
            pixel_out |= (pixel_in[1] & 0x00F8) << 2 # GREEN is bits 6-10
            pixel_out |= (pixel_in[2] & 0x00F8) >> 3 # BLUE is bits 1-5

            pixel_out_bytes[0] = (pixel_out & 0xFF00) >> 8
            pixel_out_bytes[1] = (pixel_out & 0x00FF) >> 0
            spidev.write(pixel_out_bytes)
    else:
        spidev.write(pixels)

    return

def correct_pixel_brightness(pixel):

	corrected_pixel = bytearray(3)	
	corrected_pixel[0] = int(pixel[0] / 1.1)
	corrected_pixel[1] = int(pixel[1] / 1.1)
	corrected_pixel[2] = int(pixel[2] / 1.3)
	
	return corrected_pixel

	
def pixelinvaders():
	print ("Start PixelInvaders listener "+args.UDP_IP+":"+str(args.UDP_PORT))
	sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
	sock.bind( (args.UDP_IP,args.UDP_PORT) )
	UDP_BUFFER_SIZE = 1024
	while True:
		data, addr = sock.recvfrom( UDP_BUFFER_SIZE ) # blocking call
		
		pixels_in_buffer = len(data) / PIXEL_SIZE
		pixels = bytearray(pixels_in_buffer * PIXEL_SIZE)
		
		for pixel_index in range(pixels_in_buffer):
			pixel_to_adjust = bytearray(data[(pixel_index * PIXEL_SIZE):((pixel_index * PIXEL_SIZE) + PIXEL_SIZE)])
			
			pixel_to_filter = correct_pixel_brightness(pixel_to_adjust)
			
			pixels[((pixel_index)*PIXEL_SIZE):] = filter_pixel(pixel_to_filter[:], 1)
        		
		write_stream(pixels)
		spidev.flush()

def strip():
    img = Image.open(args.filename).convert("RGB")
    input_image = img.load()
    image_width = img.size[0]
    image_height = img.size[1]
    print "%dx%d pixels" % img.size
    # Create bytearray for the entire image
    # R, G, B byte per pixel, plus extra '0' byte at end for latch. 
    print "Allocating..."
    column = [0 for x in range(image_width)]
    for x in range(image_width):
        column[x] = bytearray(args.array_height * PIXEL_SIZE + 1)

    print "Process Image..."
    for x in range(image_width):
        for y in range(args.array_height):
            value = input_image[x, y]
            y3 = y * 3
            if args.chip_type == "LPD8806":
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
        for x in range(image_width):
            write_stream(column[x])
            spidev.flush()
            time.sleep(0.001)
        time.sleep((args.refresh_rate/1000.0))

def array():
    img = Image.open(args.filename).convert("RGB")
    input_image = img.load()
    image_width = img.size[0]
    image_height = img.size[1]
    print "%dx%d pixels" % img.size
    print "Reading in array map"
    pixel_map_csv = csv.reader(open("pixel_map.csv", "rb"))
    pixel_map = []
    for p in pixel_map_csv:
        pixel_map.append(p)
    if len(pixel_map) != args.array_width * args.array_height:
        print "Map size error"
    print "Remapping"
    value = bytearray(PIXEL_SIZE)

    # Create a byte array ordered according to the pixel map file
    pixel_output = bytearray(args.array_width * args.array_height * PIXEL_SIZE + 1)
    for array_index in range(len(pixel_map)):
        value = bytearray(input_image[int(pixel_map[array_index][0]), int(pixel_map[array_index][1])])
	pixel_output[(array_index * PIXEL_SIZE):] = filter_pixel(value[:], 1)
    print "Displaying..."
    write_stream(pixel_output)
    spidev.flush()

def pan():
    img = Image.open(args.filename).convert("RGB")
    input_image = img.load()
    image_width = img.size[0]
    image_height = img.size[1]
    print "%dx%d pixels" % img.size
    print "Reading in array map"
    pixel_map_csv = csv.reader(open("pixel_map.csv", "rb"))
    pixel_map = []
    for p in pixel_map_csv:
        pixel_map.append(p)
    if len(pixel_map) != args.array_width * args.array_height:
        print "Map size error"
    print "Remapping"

    # Create a byte array ordered according to the pixel map file
    pixel_output = bytearray(args.array_width * args.array_height * PIXEL_SIZE + 1)
    while True:
        for x_offset in range(image_width - args.array_width):
#		import pdb
#		pdb.set_trace()
		for array_index in range(len(pixel_map)):
		    value = bytearray(input_image[int(int(pixel_map[array_index][0])+ x_offset), int(pixel_map[array_index][1])])
		    pixel_output[(array_index * PIXEL_SIZE):] = filter_pixel(value[:], 1)
		print "Displaying..."
		write_stream(pixel_output)
		spidev.flush()
		time.sleep((args.refresh_rate)/1000.0)

def all_off():
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Turning all LEDs Off"
    write_stream(pixel_output)
    spidev.flush()

def all_on():
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Turning all LEDs On"
    for led in range(args.num_leds):
        pixel_output[led*PIXEL_SIZE:] = filter_pixel(WHITE, 1)
    write_stream(pixel_output)
    spidev.flush()

def fade():
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    current_color = bytearray(PIXEL_SIZE)

    while True:
        for color in RAINBOW:
            for brightness in [x*0.01 for x in range(0,100)]:
                current_color[:] = filter_pixel(color[:], brightness)
                for pixel_offset in [(x * 3) for x in range(args.num_leds)]:
			pixel_output[pixel_offset:] = current_color[:]
                write_stream(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)
            for brightness in [x*0.01 for x in range(100,0, -1)]:
                current_color[:] = filter_pixel(color[:], brightness)
                for pixel_offset in [(x * 3) for x in range(args.num_leds)]:
			pixel_output[pixel_offset:] = current_color[:]
                write_stream(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)


def wiimote():
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print 'Put Wiimote in discoverable mode now (press 1+2)...'
    global wiimote
    global wii_movetimeout
    global wii_movedir
    global wii_color 
    wii_color = bytearray(PIXEL_SIZE)
    wiimote = cwiid.Wiimote()
    wiimote.mesg_callback = callback
    print "Displaying..."
    pixel_index = 0
    wiimote.rpt_mode = cwiid.RPT_ACC
    move_timeout = 0;
    while True:
	if move_timeout >= wii_movetime:
            move_timeout = 0
            if wii_movedir == 1:
                pixel_index = (pixel_index + 1)%args.num_leds
            else:
                pixel_index = pixel_index - 1
		if pixel_index == -1:
                    pixel_index = args.num_leds
        move_timeout = move_timeout + 1

#is this needed; poling?
	wiimote.request_status()

	pixel_output[((pixel_index)*PIXEL_SIZE):] = filter_pixel(wii_color[:], 1)
	pixel_output += '\x00'* ((args.num_leds+1-pixel_index)*PIXEL_SIZE)
	write_stream(pixel_output)
	spidev.flush()
	time.sleep(wii_move_timeout)



def chase():
    pixel_output = bytearray(args.num_leds * PIXEL_SIZE + 3)
    print "Displaying..."
    current_color = bytearray(PIXEL_SIZE)
    pixel_index = 0
    while True:
        for current_color[:] in RAINBOW:
	    for pixel_index in range(args.num_leds):
                pixel_output[((pixel_index-2)*PIXEL_SIZE):] = filter_pixel(current_color[:],0.2) 
                pixel_output[((pixel_index-1)*PIXEL_SIZE):] = filter_pixel(current_color[:],0.4) 
                pixel_output[((pixel_index)*PIXEL_SIZE):] = filter_pixel(current_color[:], 1)
		pixel_output += '\x00'* ((args.num_leds-1-pixel_index)*PIXEL_SIZE)
                write_stream(pixel_output)
                spidev.flush()
                time.sleep((args.refresh_rate)/1000.0)
                pixel_output[((pixel_index-2)*PIXEL_SIZE):] = filter_pixel(current_color[:], 0)



gamma = bytearray(256)

# Open SPI device, load image in RGB format and get dimensions:
def load_image():
    print "Loading..."

# Apply Gamma Correction and RGB / GRB reordering
# Optionally perform brightness adjustment
def filter_pixel(input_pixel, brightness):
    input_pixel[0] = int(brightness * input_pixel[0])
    input_pixel[1] = int(brightness * input_pixel[1])
    input_pixel[2] = int(brightness * input_pixel[2])
    output_pixel = bytearray(PIXEL_SIZE)
    if args.chip_type == "LPD8806":
        # Convert RGB into GRB bytearray list.
        output_pixel[0] = gamma[input_pixel[1]]
        output_pixel[1] = gamma[input_pixel[0]]
        output_pixel[2] = gamma[input_pixel[2]]
    else:
        output_pixel[0] = gamma[input_pixel[0]]
        output_pixel[1] = gamma[input_pixel[1]]
        output_pixel[2] = gamma[input_pixel[2]]
    return output_pixel


parser = argparse.ArgumentParser(add_help=True,version='1.0', prog='pixelpi.py')
subparsers = parser.add_subparsers(help='sub command help?')
common_parser = argparse.ArgumentParser(add_help=False)
common_parser.add_argument('--chip', action='store', dest='chip_type', default='WS2801', choices=['WS2801', 'LDP8806', 'LPD6803'], help='Specify chip type LPD6803, LDP8806 or WS2801')
common_parser.add_argument('--verbose', action='store_true', dest='verbose', default=True, help='enable verbose mode')
common_parser.add_argument('--spi_dev', action='store', dest='spi_dev_name', required=False, default='/dev/spidev0.0', help='Set the SPI device descriptor')
common_parser.add_argument('--refresh_rate', action='store', dest='refresh_rate', required=False, default=500, type=int, help='Set the refresh rate in ms (default 500ms)')
parser_strip = subparsers.add_parser('strip', parents=[common_parser], help='Stip Mode - Display an image using POV and a LED strip')
parser_strip.set_defaults(func=strip)
parser_strip.add_argument('--filename', action='store', dest='filename', required=False, help='Specify the image file eg: hello.png')
parser_strip.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7', help='Set the Y dimension of your pixel array (height)')
parser_array = subparsers.add_parser('array', parents=[common_parser], help='Array Mode - Display an image on a pixel array')
parser_array.set_defaults(func=array)
parser_array.add_argument('--filename', action='store', dest='filename', required=False, help='Specify the image file eg: hello.png')
parser_array.add_argument('--array_width', action='store', dest='array_width', required=True, type=int, default='7', help='Set the X dimension of your pixel array (width)')
parser_array.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7', help='Set the Y dimension of your pixel array (height)')
parser_pixelinvaders = subparsers.add_parser('pixelinvaders', parents=[common_parser], help='Pixelinvaders Mode - setup pixelpi as a Pixelinvaders slave')
parser_pixelinvaders.set_defaults(func=pixelinvaders)
parser_pixelinvaders.add_argument('--udp-ip', action='store', dest='UDP_IP', required=True, help='Used for PixelInvaders mode, listening address')
parser_pixelinvaders.add_argument('--udp-port', action='store', dest='UDP_PORT', required=True, default=6803, type=int, help='Used for PixelInvaders mode, listening port')
parser_fade = subparsers.add_parser('fade', parents=[common_parser], help='Fade Mode - Fade colors on all LEDs')
parser_fade.set_defaults(func=fade)
parser_fade.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,  help='Set the  number of LEDs in the string')
parser_chase = subparsers.add_parser('chase', parents=[common_parser], help='Chase Mode - Chase display test mode')
parser_chase.set_defaults(func=chase)
parser_chase.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,  help='Set the  number of LEDs in the string')
parser_pan = subparsers.add_parser('pan', parents=[common_parser], help='Pan Mode - Pan an image across an array')
parser_pan.set_defaults(func=pan)
parser_pan.add_argument('--filename', action='store', dest='filename', required=False, help='Specify the image file eg: hello.png')
parser_pan.add_argument('--array_width', action='store', dest='array_width', required=True, type=int, default='7', help='Set the X dimension of your pixel array (width)')
parser_pan.add_argument('--array_height', action='store', dest='array_height', required=True, type=int, default='7', help='Set the Y dimension of your pixel array (height)')
parser_all_on = subparsers.add_parser('all_on', parents=[common_parser], help='All On Mode - Turn all LEDs On')
parser_all_on.set_defaults(func=all_on)
parser_all_on.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,  help='Set the  number of LEDs in the string')
parser_all_off = subparsers.add_parser('all_off', parents=[common_parser], help='All Off Mode - Turn all LEDs Off')
parser_all_off.set_defaults(func=all_off)
parser_all_off.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,  help='Set the  number of LEDs in the string')
parser_wiimote = subparsers.add_parser('wiimote', parents=[common_parser], help='Wiimote Mode - move and LED witht he Wiimote')
parser_wiimote.set_defaults(func=wiimote)
parser_wiimote.add_argument('--num_leds', action='store', dest='num_leds', required=True, default=50, type=int,  help='Set the  number of LEDs in the string')

args = parser.parse_args()
spidev = file(args.spi_dev_name, "wb")
# Calculate gamma correction table. This includes
# LPD8806-specific conversion (7-bit color w/high bit set).
if args.chip_type == "LPD8806":
    for i in range(256):
        gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

if args.chip_type == "WS2801":
    for i in range(256):
        gamma[i] = int(pow(float(i) / 255.0, 2.5) * 255.0 )
        
# LPD6803 has 5 bit color, this seems to work but is not exact.
if args.chip_type == "LPD6803":
    for i in range(256):
        gamma[i] = int(pow(float(i) / 255.0, 2.0) * 255.0 + 0.5)
args.func()

#print "Chip Type             = %s" % args.chip_type
#print "File Name             = %s" % args.filename
#print "Display Mode          = %s" % args.mode
#print "SPI Device Descriptor = %s" % args.spi_dev_name
#print "Refresh Rate          = %s" % args.refresh_rate
#print "Array Dimensions      = %dx%d" % (args.array_width, args.array_height)
def print_state(state):
	print 'Report Mode:',
	for r in ['STATUS', 'BTN', 'ACC', 'IR', 'NUNCHUK', 'CLASSIC', 'BALANCE', 'MOTIONPLUS']:
		if state['rpt_mode'] & eval('cwiid.RPT_' + r):
			print r,
	print

	print 'Active LEDs:',
	for led in ['1','2','3','4']:
		if state['led'] & eval('cwiid.LED' + led + '_ON'):
			print led,
	print

	print 'Rumble:', state['rumble'] and 'On' or 'Off'

	print 'Battery:', int(100.0 * state['battery'] / cwiid.BATTERY_MAX)

	if 'buttons' in state:
		print 'Buttons:', state['buttons']

	if 'acc' in state:
		print 'Acc: x=%d y=%d z=%d' % (state['acc'][cwiid.X],
		                               state['acc'][cwiid.Y],
		                               state['acc'][cwiid.Z])

	if 'ir_src' in state:
		valid_src = False
		print 'IR:',
		for src in state['ir_src']:
			if src:
				valid_src = True
				print src['pos'],

		if not valid_src:
			print 'no sources detected'
		else:
			print

	if state['ext_type'] == cwiid.EXT_NONE:
		print 'No extension'
	elif state['ext_type'] == cwiid.EXT_UNKNOWN:
		print 'Unknown extension attached'
	elif state['ext_type'] == cwiid.EXT_NUNCHUK:
		if state.has_key('nunchuk'):
			print 'Nunchuk: btns=%.2X stick=%r acc.x=%d acc.y=%d acc.z=%d' % \
			  (state['nunchuk']['buttons'], state['nunchuk']['stick'],
			   state['nunchuk']['acc'][cwiid.X],
			   state['nunchuk']['acc'][cwiid.Y],
			   state['nunchuk']['acc'][cwiid.Z])
	elif state['ext_type'] == cwiid.EXT_CLASSIC:
		if state.has_key('classic'):
			print 'Classic: btns=%.4X l_stick=%r r_stick=%r l=%d r=%d' % \
			  (state['classic']['buttons'],
			   state['classic']['l_stick'], state['classic']['r_stick'],
			   state['classic']['l'], state['classic']['r'])
	elif state['ext_type'] == cwiid.EXT_BALANCE:
		if state.has_key('balance'):
			print 'Balance: right_top=%d right_bottom=%d left_top=%d left_bottom=%d' % \
			  (state['balance']['right_top'], state['balance']['right_bottom'],
			   state['balance']['left_top'], state['balance']['left_bottom'])
	elif state['ext_type'] == cwiid.EXT_MOTIONPLUS:
		if state.has_key('motionplus'):
			print 'MotionPlus: angle_rate=(%d,%d,%d)' % state['motionplus']['angle_rate']

def callback(mesg_list, time):
	print 'time: %f' % time
	for mesg in mesg_list:
		if mesg[0] == cwiid.MESG_STATUS:
			print 'Status Report: battery=%d extension=' % \
			       mesg[1]['battery'],
			if mesg[1]['ext_type'] == cwiid.EXT_NONE:
				print 'none'
			elif mesg[1]['ext_type'] == cwiid.EXT_NUNCHUK:
				print 'Nunchuk'
			elif mesg[1]['ext_type'] == cwiid.EXT_CLASSIC:
				print 'Classic Controller'
			elif mesg[1]['ext_type'] == cwiid.EXT_BALANCE:
				print 'Balance Board'
			elif mesg[1]['ext_type'] == cwiid.EXT_MOTIONPLUS:
				print 'MotionPlus'
			else:
				print 'Unknown Extension'

		elif mesg[0] == cwiid.MESG_BTN:
			print 'Button Report: %.4X' % mesg[1]

		elif mesg[0] == cwiid.MESG_ACC:
			print 'Acc Report: x=%d, y=%d, z=%d' % \
			      (mesg[1][cwiid.X], mesg[1][cwiid.Y], mesg[1][cwiid.Z])
			if mesg[1][cwiid.X] > 512:
				wii_movedir = 1
			else:
				wii_movedir = 0
			if abs(mesg[1][cwiidX] - 512) > 50:
				wii_move_timeout = 0.02
			else:
				wii_move_timeout = 0.4

		elif mesg[0] == cwiid.MESG_IR:
			valid_src = False
			print 'IR Report: ',
			for src in mesg[1]:
				if src:
					valid_src = True
					print src['pos'],

			if not valid_src:
				print 'no sources detected'
			else:
				print

		elif mesg[0] == cwiid.MESG_NUNCHUK:
			print ('Nunchuk Report: btns=%.2X stick=%r ' + \
			       'acc.x=%d acc.y=%d acc.z=%d') % \
			      (mesg[1]['buttons'], mesg[1]['stick'],
			       mesg[1]['acc'][cwiid.X], mesg[1]['acc'][cwiid.Y],
			       mesg[1]['acc'][cwiid.Z])
		elif mesg[0] == cwiid.MESG_CLASSIC:
			print ('Classic Report: btns=%.4X l_stick=%r ' + \
			       'r_stick=%r l=%d r=%d') % \
			      (mesg[1]['buttons'], mesg[1]['l_stick'],
			       mesg[1]['r_stick'], mesg[1]['l'], mesg[1]['r'])
		elif mesg[0] ==  cwiid.MESG_BALANCE:
			print ('Balance Report: right_top=%d right_bottom=%d ' + \
			       'left_top=%d left_bottom=%d') % \
			      (mesg[1]['right_top'], mesg[1]['right_bottom'],
			       mesg[1]['left_top'], mesg[1]['left_bottom'])
		elif mesg[0] == cwiid.MESG_MOTIONPLUS:
			print 'MotionPlus Report: angle_rate=(%d,%d,%d)' % \
			      mesg[1]['angle_rate']
		elif mesg[0] ==  cwiid.MESG_ERROR:
			print "Error message received"
			global wiimote
			wiimote.close()
			exit(-1)
		else:
			print 'Unknown Report'


