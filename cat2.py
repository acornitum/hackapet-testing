import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

# Initialize pygame
pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

# Load the background image
forest_background = displayio.OnDiskBitmap("forestbackground.bmp")
bg_sprite = displayio.TileGrid(forest_background, pixel_shader=forest_background.pixel_shader)
splash.append(bg_sprite)

# Load the sprite sheet
cat_sheet = displayio.OnDiskBitmap("cat-Sheet.bmp")

# Define the tile size (width and height of each frame)
tile_width = 32
tile_height = 32

# Create a TileGrid for the sprite sheet
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

# Add the sprite to the group
splash.append(cat_sprite)

# Animation loop
frame = 0
speed = 2  # Speed of movement

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat_sprite.x -= speed
            elif event.key == pygame.K_RIGHT:
                cat_sprite.x += speed

    # Update the tile index to animate the sprite
    cat_sprite[0] = frame
    frame = (frame + 1) % (cat_sheet.width // tile_width)

    # Delay to control animation speed
    time.sleep(0.1)