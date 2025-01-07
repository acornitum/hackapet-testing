import board
import displayio
import digitalio
import busio
import time
import adafruit_imageload
from adafruit_ssd1351 import SSD1351

displayio.release_displays()
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
tft_cs = board.GP3
tft_dc = board.GP4
reset_pin = board.GP5

rbtn = digitalio.DigitalInOut(board.BTNR)
rbtn.pull = digitalio.Pull.UP

lbtn = digitalio.DigitalInOut(board.BTNL)
lbtn.pull = digitalio.Pull.UP

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=reset_pin, baudrate=16000000
)

display = SSD1351(display_bus, width=128, height=128)
display.rotation=180

# Make the display context
group = displayio.Group()
display.root_group = group
# group.x = 128
# group.y = 128

forest_bg_file = open("/images/bg_forest.bmp", "rb")
forest_bg = displayio.OnDiskBitmap(forest_bg_file)
forest_bg_sprite = displayio.TileGrid(forest_bg, pixel_shader=getattr(forest_bg, 'pixel_shader', displayio.ColorConverter()))

group.append(forest_bg_sprite)

cat_filename = "/images/cat_sheet_pbg.bmp"

cat_img, cat_pal = adafruit_imageload.load(cat_filename)
cat_pal.make_transparent(1)

cat_tilegrid = displayio.TileGrid(
    cat_img,
    pixel_shader=cat_pal,
    width=1,
    height=1,
    tile_width=32,
    tile_height=32,
    default_tile=0,
    x=(display.width - 32) // 2,  
    y=display.height - 32 - 10     
)

group.append(cat_tilegrid)

frame = 0
speed = 2

frame_time = 0

while True:
    if not lbtn.value:
        cat_tilegrid.x -= speed
    elif not rbtn.value:
        cat_tilegrid.x += speed

    frame_time += 1
    if frame_time >= 10:
        cat_tilegrid[0] = frame
        frame = (frame + 1) % 9
        frame_time = 0

    time.sleep(0.01)
    pass
