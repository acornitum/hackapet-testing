import board
import displayio
import time
import busio
import pulseio
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351


displayio.release_displays()
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
tft_cs = board.GP3
tft_dc = board.GP4
reset_pin = board.GP5

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=reset_pin, baudrate=16000000
)

display = SSD1351(display_bus, width=128, height=128)
display.rotation = 180

splash = displayio.Group()
display.root_group = splash
color_bitmap = displayio.Bitmap(128, 128, 128)

odb = displayio.OnDiskBitmap('/forestbackground.bmp')
face = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
splash.append(face)

# CAT CAT CAT CAT CAT !!!! 

# define colour palette here

cat_palette=displayio.Palette(5)

cat_palette[0] = 0xFF0000 # red
cat_palette[1] = 0x00FF00 # green
cat_palette[2] = 0x0000FF # blue
cat_palette[3] = 0x0000FF # blue
cat_palette[4] = 0x0000FF # blue

## end def

cat_bitmap = displayio.Bitmap(32, 32, 5)




cat_sheet = displayio.OnDiskBitmap("/cat-spritesheet.bmp")

tile_width = 32
tile_height = 32

cat_sprite = displayio.TileGrid(
    cat_sheet,
    pixel_shader=cat_sheet.pixel_shader,
    width=1,
    height=1,
    tile_width=tile_width,
    tile_height=tile_height,
    default_tile=0,
    x=(display.width - tile_width) // 2,  # Initial x position (centered)
    y=display.height - tile_height        # Initial y position (bottom)
)

splash.append(cat_sprite)

# Animation loop
frame = 0
speed = 2  # Speed of movement

display.refresh(target_frames_per_second=24)

# Wait forever
while True:
    cat_sprite[0] = frame
    frame = (frame + 1) % (cat_sheet.width // tile_width)

    # Delay to control animation speed
    time.sleep(0.1)