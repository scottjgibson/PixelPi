PixelPi
=======
RGB Pixel Array Driver for the Raspberry Pi

Project Page:
http://thegreatgeekery.blogspot.ca/2012/08/raspberry-pi-and-ws2801.html

- Originally based on http://learn.adafruit.com/light-painting-with-raspberry-pi/software


sudo python pixelpi.py --help
usage: pixelpi.py [-h] [-v]
                  
                  {strip,array,pixelinvaders,fade,chase,pan,all_on,all_off,wiimote}
                  ...

positional arguments:
  {strip,array,pixelinvaders,fade,chase,pan,all_on,all_off,wiimote}
                        sub command help?
    strip               Stip Mode - Display an image using POV and a LED strip
    array               Array Mode - Display an image on a pixel array
    pixelinvaders       Pixelinvaders Mode - setup pixelpi as a Pixelinvaders
                        slave
    fade                Fade Mode - Fade colors on all LEDs
    chase               Chase Mode - Chase display test mode
    pan                 Pan Mode - Pan an image across an array
    all_on              All On Mode - Turn all LEDs On
    all_off             All Off Mode - Turn all LEDs Off
    wiimote             Wiimote Mode - move and LED witht he Wiimote

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit


sudo python pixelpi.py strip --help 
usage: pixelpi.py strip [-h] [--chip {WS2801,LDP8806}] [--verbose]
                        [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                        [--filename FILENAME] --array_height ARRAY_HEIGHT

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --filename FILENAME   Specify the image file eg: hello.png
  --array_height ARRAY_HEIGHT
                        Set the Y dimension of your pixel array (height)


sudo python pixelpi.py array --help 
usage: pixelpi.py array [-h] [--chip {WS2801,LDP8806}] [--verbose]
                        [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                        [--filename FILENAME] --array_width ARRAY_WIDTH
                        --array_height ARRAY_HEIGHT

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --filename FILENAME   Specify the image file eg: hello.png
  --array_width ARRAY_WIDTH
                        Set the X dimension of your pixel array (width)
  --array_height ARRAY_HEIGHT
                        Set the Y dimension of your pixel array (height)



sudo python pixelpi.py pixelinvaders --help 
usage: pixelpi.py pixelinvaders [-h] [--chip {WS2801,LDP8806}] [--verbose]
                                [--spi_dev SPI_DEV_NAME]
                                [--refresh_rate REFRESH_RATE] --udp-ip UDP_IP
                                --udp-port UDP_PORT

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --udp-ip UDP_IP       Used for PixelInvaders mode, listening address
  --udp-port UDP_PORT   Used for PixelInvaders mode, listening port


sudo python pixelpi.py fade --help 
usage: pixelpi.py fade [-h] [--chip {WS2801,LDP8806}] [--verbose]
                       [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                       --num_leds NUM_LEDS

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string



sudo python pixelpi.py chase --help 
usage: pixelpi.py chase [-h] [--chip {WS2801,LDP8806}] [--verbose]
                        [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                        --num_leds NUM_LEDS

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string



sudo python pixelpi.py pan --help 
usage: pixelpi.py pan [-h] [--chip {WS2801,LDP8806}] [--verbose]
                      [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                      [--filename FILENAME] --array_width ARRAY_WIDTH
                      --array_height ARRAY_HEIGHT

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --filename FILENAME   Specify the image file eg: hello.png
  --array_width ARRAY_WIDTH
                        Set the X dimension of your pixel array (width)
  --array_height ARRAY_HEIGHT
                        Set the Y dimension of your pixel array (height)



sudo python pixelpi.py all_on --help 
usage: pixelpi.py all_on [-h] [--chip {WS2801,LDP8806}] [--verbose]
                         [--spi_dev SPI_DEV_NAME]
                         [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string



sudo python pixelpi.py all_off --help 
usage: pixelpi.py all_off [-h] [--chip {WS2801,LDP8806}] [--verbose]
                          [--spi_dev SPI_DEV_NAME]
                          [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string



sudo python pixelpi.py wiimote --help 
usage: pixelpi.py wiimote [-h] [--chip {WS2801,LDP8806}] [--verbose]
                          [--spi_dev SPI_DEV_NAME]
                          [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

optional arguments:
  -h, --help            show this help message and exit
  --chip {WS2801,LDP8806}
                        Specify chip type LDP8806 or WS2801
  --verbose             enable verbose mode
  --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
  --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
  --num_leds NUM_LEDS   Set the number of LEDs in the string



