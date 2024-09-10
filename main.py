import pygame, sys, math
from packages import engine

# Static Variables
display = {
    "scale": (500, 500)
}

# Package initialization
pygame.init()
win = pygame.display.set_mode(display["scale"])

# Game Functions


# Game Initialization



# Scene initialization
sceneManager = engine.sceneManager()

menu = 

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()