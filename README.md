PixelPi
=======
RGB Pixel Array Driver for the Raspberry Pi

Project Page:
http://thegreatgeekery.blogspot.ca/2012/08/raspberry-pi-and-ws2801.html

- Originally based on http://learn.adafruit.com/light-painting-with-raspberry-pi/software

usage: pixelpi.py [-h] [-v] [--chip {WS2801,LDP8806}] [--filename FILENAME]
                  --mode {all_off,all_on,strip,array,fade,chase} [--verbose]
                  [--array_width ARRAY_WIDTH] [--array_height ARRAY_HEIGHT]
                  [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                  [--num_leds NUM_LEDS]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --filename FILENAME   Specify the image file eg: hello.png
  --mode {all_off,all_on,strip,array,fade,chase}
                        Choose the display mode, either POV strip or 2D array,
                        color, chase
  --verbose             enable verbose mode
  --array_width ARRAY_WIDTH
                        Set the X dimension of your pixel array (width)
  --array_height ARRAY_HEIGHT
                        Set the Y dimension of your pixel array (height)
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string (used in fade and
                        chase mode)

