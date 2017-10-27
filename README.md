PixelPi
=======
RGB Pixel Array Driver for the Raspberry Pi

Project Page:
http://thegreatgeekery.blogspot.ca/2012/08/raspberry-pi-and-ws2801.html

- Originally based on http://learn.adafruit.com/light-painting-with-raspberry-pi/software

Changelog:
- Version 20171026, enhancements by Alois Hockenschlohe:
   * enhanced documentation (this file)
   * added some png files for testing purposes (16x10 pixel, see directory 'images')
   * function 'array':
     - fixed a major (!) bug, works now
     - added some output
     - added some maybe useful debugging output (formerly unused option '--verbose')
   * added example file 'pixel_map_16x10.csv'

Supported Chips:
- WS2801
- LPD8806
- LPD6803
- SM16716

                  sudo python pixelpi.py --help
                  usage: pixelpi.py [-h] [-v]
                                    {strip,array,pixelinvaders,fade,chase,pan,all_on,all_off,wiimote}
                                    ...

                  positional arguments:
                                    {strip,array,pixelinvaders,fade,chase,pan,all_on,all_off,wiimote}
                                    sub command help?
                                    strip               Stip Mode - Display an image using POV and a LED strip
                                    array               Array Mode - Display an image on a pixel array
                                    pixelinvaders       Pixelinvaders Mode - setup pixelpi as a Pixelinvaders slave
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
                                    usage: pixelpi.py strip [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                                                            [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                                                           [--filename FILENAME] --array_height ARRAY_HEIGHT

                                    optional arguments:
                                      -h, --help            show this help message and exit
                                      --chip {WS2801,LPD8806,LPD6803,SM16716} Specify chip type
                                      --verbose             enable verbose mode
                                      --spi_dev SPI_DEV_NAME Set the SPI device descriptor
                                      --refresh_rate REFRESH_RATE  Set the refresh rate in ms (default 500ms)
                                      --filename FILENAME   Specify the image file eg: hello.png
                                      --array_height ARRAY_HEIGHT   Set the Y dimension of your pixel array (height)


                  sudo python pixelpi.py array --help 
                  usage: pixelpi.py array [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                        [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                        [--filename FILENAME] --array_width ARRAY_WIDTH
                        --array_height ARRAY_HEIGHT

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
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
                  usage: pixelpi.py pixelinvaders [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                                [--spi_dev SPI_DEV_NAME]
                                [--refresh_rate REFRESH_RATE] --udp-ip UDP_IP
                                --udp-port UDP_PORT

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                    --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --udp-ip UDP_IP       Used for PixelInvaders mode, listening address
                    --udp-port UDP_PORT   Used for PixelInvaders mode, listening port


                  sudo python pixelpi.py fade --help 
                  usage: pixelpi.py fade [-h] [--chip {WS2801,LPD8806}] [--verbose]
                       [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                       --num_leds NUM_LEDS

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                    --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --num_leds NUM_LEDS   Set the number of LEDs in the string



                  sudo python pixelpi.py chase --help 
                  usage: pixelpi.py chase [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                        [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                        --num_leds NUM_LEDS

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                    --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --num_leds NUM_LEDS   Set the number of LEDs in the string



                  sudo python pixelpi.py pan --help 
                  usage: pixelpi.py pan [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                      [--spi_dev SPI_DEV_NAME] [--refresh_rate REFRESH_RATE]
                      [--filename FILENAME] --array_width ARRAY_WIDTH
                      --array_height ARRAY_HEIGHT

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
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
                  usage: pixelpi.py all_on [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                         [--spi_dev SPI_DEV_NAME]
                         [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type 
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                    --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --num_leds NUM_LEDS   Set the number of LEDs in the string



                  sudo python pixelpi.py all_off --help 
                  usage: pixelpi.py all_off [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                          [--spi_dev SPI_DEV_NAME]
                          [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                   --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --num_leds NUM_LEDS   Set the number of LEDs in the string



                  sudo python pixelpi.py wiimote --help 
                  usage: pixelpi.py wiimote [-h] [--chip {WS2801,LPD8806,LPD6803,SM16716}] [--verbose]
                          [--spi_dev SPI_DEV_NAME]
                          [--refresh_rate REFRESH_RATE] --num_leds NUM_LEDS

                  optional arguments:
                    -h, --help            show this help message and exit
                    --chip {WS2801,LPD8806,LPD6803,SM16716}
                        Specify chip type
                    --verbose             enable verbose mode
                    --spi_dev SPI_DEV_NAME
                        Set the SPI device descriptor
                    --refresh_rate REFRESH_RATE
                        Set the refresh rate in ms (default 500ms)
                    --num_leds NUM_LEDS   Set the number of LEDs in the string

pixel_map.csv format
===================
Each line of this file pertains to a pixel, the first line is the
first pixel in the LED string (closest to the RaspberryPi).
Each line has two entries (x and y location)

Closer explanation:

Each pixel of a png image is mapped with x and y coordinates,
starting in the upper left corner of the image

    /======> X
    ||  
    ||  0/0  1/0  2/0  3/0  4/0  ...
    ||  0/1  1/1  2/1  3/1  4/1  ...
    \/  0/2  1/2  2/2  3/2  4/2  ...
     Y  0/3  1/3  2/3  3/3  4/3  ...
        ...  ...  ...  ...  ...  ...

The file pixel_map.csv describes, which LED represents which pixel of the png,
where the line number in the file adresses the LED and the values written in
the line for the x/y coordinates of the pixel

 line number -> x/y coordinates

Here is an example:

Let's take a look at a home-made 16x10 matrix.
The matrix is made out of 2 rows with 4 panels (crates) each.
Each panel (crate) consists of 20 LED's (bottles) each.

Here the wiring layout of a crate (bottom/lights are facing toward the viewer):

          /---------------\
          | O---O   O---O |
          | |   |   |   | |
          | O   O   O   O |
          | |   |   |   | |
          | O   O   O   O |
          | |   |   |   | |
          | O   O   O   O |
          | |   |   |   | |
    in >--+-O   O---O   O-+--> out
          \---------------/

In our setup the Raspberry is located at the lower left corner and all
LED's (bottles) are connected with a single line.

The wiring for all the 160 LED's looks like this
(notice the connection between the LED's (bottle) 79 and 80):


    /======> X
    ||
    ||       /-----------------\/-----------------\/-----------------\/-----------------\
    ||       |  84--85  94--95 || 104-105 114-115 || 124-125 134-135 || 144-145 154-155 |
    \/       |  83  86  93  96 || 103 106 113 116 || 123 126 133 136 || 143 146 153 156 |
             |  82  87  92  97 || 102 107 112 117 || 122 127 132 137 || 142 147 152 157 |
     Y       |  81  88  91  98 || 101 108 111 118 || 121 128 131 138 || 141 148 151 158 |
         /---+--80  89--90  99-++-100 109-110 119-++-120 129-130 139-++-140 149-150 159 |
         |    \-----------------/\-----------------/\-----------------/\-----------------/
         |
         \----------------------------------------------------------------------------------\    
                                                                                            |
             /-----------------\/-----------------\/-----------------\/-----------------\   |
             |   4---5  14--15 ||  24--25  34--35 ||  44--45  54--55 ||  64--65  74--75 |   |
             |   3   6  13  16 ||  23  26  33  36 ||  43  46  53  56 ||  63  66  73  76 |   |
             |   2   7  12  17 ||  22  27  32  37 ||  42  47  52  57 ||  62  67  72  77 |   |
    +-----+  |   1   8  11  18 ||  21  28  31  38 ||  41  48  51  58 ||  61  68  71  78 |   |
    | RPi |--+---0   9--10  19-++--20  29--30  39-++--40  49--50  59-++--60  69--70  79-+---/
    +-----+  \-----------------/\-----------------/\-----------------/\-----------------/
    
For a propper mapping, the file pixel_map.csv should look like this
(without the comments, of course):

    +-- START ---
    |0,9    # Line   0: LED  0 (closest to the raspberry) represents the pixel with the x/y coordinates 0/9
    |0,8    # Line   1: LED  1 represents the pixel with the x/y coordinates 0/8
    |0,7    # Line   2: LED  2 represents the pixel with the x/y coordinates 0/7
    |...
    |14,9   # Line  78: LED  78 represents the pixel with the x/y coordinates 14/9
    |15,9   # Line  79: LED  79 represents the pixel with the x/y coordinates 15/9
    |0,4    # Line  80: LED  80 represents the pixel with the x/y coordinates  0/4
    |0,3    # Line  81: LED  81 represents the pixel with the x/y coordinates  0/3
    |...
    |15,2   # Line 157: LED 157 represents the pixel with the x/y coordinates 15/2
    |15,3   # Line 158: LED 158 represents the pixel with the x/y coordinates 15/3
    |15,4   # Line 159: LED 159 (the last one in the line) represents the pixel with the x/y coordinates 15/3
    +--- END ---

You can find the whole mapping of the example in file "pixel_map_16x10.csv".
