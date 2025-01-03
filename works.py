import board
import displayio
import time
import busio
import pulseio
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351


displayio.release_displays()
spi = busio.SPI(clock=board.SCK, MISO=board.MOSI, MOSI=board.MISO)
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
# Wait for the image to load.
display.refresh(target_frames_per_second=60)

# Wait forever
while True:
    pass