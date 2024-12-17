import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
        elif event.type == pygame.KEYUP:
            print(f"Key released: {pygame.key.name(event.key)}")

pygame.quit()