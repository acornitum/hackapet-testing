import board
import terminalio
import displayio
import busio
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

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(108, 108, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
splash.append(inner_sprite)

# Draw a label
text = "HACKAPET!!!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=30, y=64)
splash.append(text_area)

while True:
    pass