# import sys
# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 8)
color_palette = displayio.Palette(2)
color_palette[0] = 0x00FFFF
color_palette[1] = 0x0000FF  

for y in range(display.height):
    for x in range(display.width):
        if x % 3 == 0 or x % 4 == 0:
            color_bitmap[x, y] = 1
        else:
            color_bitmap[x, y] = 0

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

while True:
    if display.check_quit():
        break