import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

forest_background = displayio.OnDiskBitmap("forestbackground.bmp")

bg_sprite = displayio.TileGrid(forest_background, pixel_shader=forest_background.pixel_shader)

splash.append(bg_sprite)

display.show(splash)

while True:
    if display.check_quit():
        break
