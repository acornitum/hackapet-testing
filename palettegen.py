from PIL import Image

# Open the image
image = Image.open("cat-Sheet.bmp")

# Convert to P mode (palette mode)
image = image.convert("P", palette=Image.ADAPTIVE, colors=256)

# Save the palette
palette = image.getpalette()

# Create a new image to show the palette
palette_image = Image.new("P", (256, 1))  # One row, 256 colors
palette_image.putpalette(palette)
palette_image.save("palette.png")

