import pygame
import random
import time
import math
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eat the Flower Garden")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 200, 100)
DARK_GREEN = (34, 139, 34)
STEM_GREEN = (60, 160, 60)
LIGHT_GREEN = (144, 238, 144)
PINK = (255, 182, 193)
BABY_PINK = (255, 209, 220)
PURPLE = (147, 112, 219)
BLUE = (100, 149, 237)
YELLOW = (255, 255, 153)
ORANGE = (255, 165, 0)
ORANGE_CAT = (255, 165, 80)
STRIPE_ORANGE = (220, 140, 60)
LIGHT_PURPLE = (230, 230, 250)

# Fonts
font = pygame.font.SysFont('Calibri', 24)
small_font = pygame.font.SysFont('Calibri', 18)
large_font = pygame.font.SysFont('Calibri', 32)

# Amazon Q Developer facts for the quiz
amazon_q_facts = [
    {"question": "Amazon Q Developer can help with code generation", "answer": True},
    {"question": "Amazon Q Developer cannot analyze your existing codebase", "answer": False},
    {"question": "Amazon Q Developer can help troubleshoot errors in your code", "answer": True},
    {"question": "Amazon Q Developer is only available for Java developers", "answer": False},
    {"question": "Amazon Q Developer can suggest code optimizations", "answer": True}
]

def main():
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        
        title = large_font.render("Flower Garden Game - Extended Version", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()