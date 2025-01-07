import board
import displayio
import time
import busio
import random
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351
import pygame

# Initialize pygame
pygame.init()

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

# Load the background image
odb = displayio.OnDiskBitmap('/forestbackground.bmp')
face = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
splash.append(face)

# Load the cat sprite sheet
cat_sheet = displayio.OnDiskBitmap("cat-Sheet.bmp")

# Define the tile size (width and height of each frame)
tile_width = 32
tile_height = 32

# Create a TileGrid for the cat sprite
cat_sprite = displayio.TileGrid(
    cat_sheet,
    pixel_shader=cat_sheet.pixel_shader,
    width=1,
    height=1,
    tile_width=tile_width,
    tile_height=tile_height,
    default_tile=0,
    x=(display.width - tile_width) // 2,
    y=display.height - tile_height - 16
)

# Add the cat sprite to the group
splash.append(cat_sprite)

# Load the fireball image
fireball_bitmap = displayio.OnDiskBitmap("fireball.bmp")

# List to hold active fireballs
fireballs = []

# Function to spawn a fireball at a random position at the top
def spawn_fireball():
    x_position = random.randint(0, display.width - fireball_bitmap.width)
    fireball = displayio.TileGrid(
        fireball_bitmap,
        pixel_shader=fireball_bitmap.pixel_shader,
        width=1,
        height=1,
        tile_width=fireball_bitmap.width,
        tile_height=fireball_bitmap.height,
        x=x_position,
        y=0
    )
    fireballs.append(fireball)
    splash.append(fireball)

# Function to check for collisions
def check_collision(sprite1, sprite2):
    return (
        sprite1.x < sprite2.x + sprite2.width and
        sprite1.x + sprite1.width > sprite2.x and
        sprite1.y < sprite2.y + sprite2.height and
        sprite1.y + sprite1.height > sprite2.y
    )

# Function to display "You Died" message
def display_game_over():
    global death_hi
    text_area = label.Label(terminalio.FONT, text="You Died", color=0xFF0000)
    text_area.x = display.width // 2 - text_area.bounding_box[2] // 2
    text_area.y = display.height // 2 - text_area.bounding_box[3] // 2
    splash.append(text_area)
    death_hi = text_area

# Function to clear "You Died" message
def clear_game_over():
    global death_hi
    if death_hi and death_hi in splash:
        splash.remove(death_hi)
        death_hi = None

# Initialize global variable
death_hi = None

frame = 0
speed = 2  
game_over = False

while True:
    if display.check_quit():
        break

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cat_sprite.x -= speed
        if keys[pygame.K_RIGHT]:
            cat_sprite.x += speed

        if random.random() < 0.05:  # Adjust the spawn rate as needed
            spawn_fireball()

        for fireball in fireballs:
            fireball.y += 5  # Move the fireball down
            if fireball.y > display.height:
                splash.remove(fireball)
                fireballs.remove(fireball)
            elif check_collision(cat_sprite, fireball):
                game_over = True
                display_game_over()

        cat_sprite[0] = frame

    # Delay to control the update rate
    time.sleep(0.05)