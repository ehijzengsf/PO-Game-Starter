
import pygame
import sys

# Initialisatie
pygame.init()

# Instellingen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mijn Eerste Game")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (30, 30, 30)

def main():
    running = True
    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Tekenen
        screen.fill(BG_COLOR)
        
        # Hier kun je straks je eigen code toevoegen!

        # 3. Update scherm
        pygame.display.flip()
        
        # 4. Framerate begrenzen (60 FPS)
        clock.tick(60)

    # Afsluiten
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
