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
STEM_GREEN = (60, 160, 60)  # Darker green for stems
LIGHT_GREEN = (144, 238, 144)
PINK = (255, 182, 193)
BABY_PINK = (255, 209, 220)
PURPLE = (147, 112, 219)
BLUE = (100, 149, 237)
YELLOW = (255, 255, 153)
ORANGE = (255, 165, 0)
ORANGE_CAT = (255, 165, 80)
STRIPE_ORANGE = (220, 140, 60)
LIGHT_PURPLE = (230, 230, 250)  # For daisy flowers

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
    {"question": "Amazon Q Developer can suggest code optimizations", "answer": True},
    {"question": "Amazon Q Developer cannot help with infrastructure as code", "answer": False},
    {"question": "Amazon Q Developer can explain complex code snippets", "answer": True},
    {"question": "Amazon Q Developer is limited to AWS services only", "answer": False},
    {"question": "Amazon Q Developer can help with unit test generation", "answer": True},
    {"question": "Amazon Q Developer cannot provide security recommendations", "answer": False},
    {"question": "Amazon Q Developer can assist with API usage examples", "answer": True},
    {"question": "Amazon Q Developer is not integrated with IDEs", "answer": False},
    {"question": "Amazon Q Developer can help debug runtime errors", "answer": True},
    {"question": "Amazon Q Developer cannot generate documentation", "answer": False},
    {"question": "Amazon Q Developer can provide best practices for your code", "answer": True},
    {"question": "Amazon Q Developer can help you refactor your code", "answer": True},
    {"question": "Amazon Q Developer is only available in English", "answer": False},
    {"question": "Amazon Q Developer can help with database query optimization", "answer": True},
    {"question": "Amazon Q Developer cannot understand code context", "answer": False},
    {"question": "Amazon Q Developer can suggest more efficient algorithms", "answer": True},
    {"question": "Amazon Q Developer cannot help with debugging CI/CD pipelines", "answer": False},
    {"question": "Amazon Q Developer can help you learn new programming languages", "answer": True},
    {"question": "Amazon Q Developer is only available for AWS customers", "answer": False},
    {"question": "Amazon Q Developer can help with code reviews", "answer": True},
    {"question": "Amazon Q Developer cannot explain AWS service concepts", "answer": False},
    {"question": "Amazon Q Developer can help you implement design patterns", "answer": True},
    {"question": "Amazon Q Developer cannot generate test data", "answer": False},
    {"question": "Amazon Q Developer can help with serverless application development", "answer": True},
    {"question": "Amazon Q Developer is not available in VS Code", "answer": False},
    {"question": "Amazon Q Developer can help you understand complex error messages", "answer": True},
    {"question": "Amazon Q Developer cannot help with cloud architecture decisions", "answer": False},
    {"question": "Amazon Q Developer can help you write more secure code", "answer": True},
    {"question": "Amazon Q Developer cannot help with performance optimization", "answer": False},
    {"question": "Amazon Q Developer can help you implement accessibility features", "answer": True},
    {"question": "Amazon Q Developer cannot generate code comments", "answer": False},
    {"question": "Amazon Q Developer can help you understand third-party libraries", "answer": True},
    {"question": "Amazon Q Developer is not available in JetBrains IDEs", "answer": False},
    {"question": "Amazon Q Developer can help you implement RESTful APIs", "answer": True},
    {"question": "Amazon Q Developer cannot help with mobile app development", "answer": False},
    {"question": "Amazon Q Developer can help you write more maintainable code", "answer": True},
    {"question": "Amazon Q Developer can help with database schema design", "answer": True},
    {"question": "Amazon Q Developer cannot analyze log files", "answer": False},
    {"question": "Amazon Q Developer can suggest AWS service configurations", "answer": True},
    {"question": "Amazon Q Developer is not capable of explaining algorithms", "answer": False},
    {"question": "Amazon Q Developer can help with Docker containerization", "answer": True},
    {"question": "Amazon Q Developer cannot assist with Kubernetes configurations", "answer": False},
    {"question": "Amazon Q Developer can help optimize cloud costs", "answer": True},
    {"question": "Amazon Q Developer is not able to generate unit tests", "answer": False},
    {"question": "Amazon Q Developer can help with API gateway setup", "answer": True},
    {"question": "Amazon Q Developer cannot assist with CI/CD workflows", "answer": False},
    {"question": "Amazon Q Developer can help with data modeling", "answer": True},
    {"question": "Amazon Q Developer is not capable of suggesting security improvements", "answer": False},
    {"question": "Amazon Q Developer can help with microservice architecture", "answer": True},
    {"question": "Amazon Q Developer cannot assist with frontend development", "answer": False},
    {"question": "Amazon Q Developer can help with serverless function optimization", "answer": True},
    {"question": "Amazon Q Developer is not able to explain error messages", "answer": False},
    {"question": "Amazon Q Developer can help with database query performance", "answer": True},
    {"question": "Amazon Q Developer cannot assist with code refactoring", "answer": False},
    {"question": "Amazon Q Developer can help with AWS CDK implementations", "answer": True},
    {"question": "Amazon Q Developer is not capable of generating CloudFormation templates", "answer": False}
]

# Function to create ombre color
def create_ombre_color(base_color, intensity=0.5):
    r, g, b = base_color
    white_blend = 255 * (1 - intensity)
    return (int(r * intensity + white_blend), int(g * intensity + white_blend), int(b * intensity + white_blend))

def draw_bell_flower(surface, x, y, color=(65, 105, 225), size=30):
    points = []
    for i in range(180):
        angle = math.radians(i)
        px = x + size * 0.8 * math.sin(angle)
        py = y + size * math.cos(angle)
        points.append((px, py))

    if len(points) > 2:
        pygame.draw.polygon(surface, color, points)

    pygame.draw.line(surface, (0, 100, 0), (x, y), (x, y + size * 1.5), 3)

def draw_star_flower(surface, x, y, color=(148, 0, 211), size=30):
    points = []
    for i in range(5):
        angle = math.radians(i * 72)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        points.append((px, py))

        angle = math.radians(i * 72 + 36)
        px = x + size * 0.4 * math.cos(angle)
        py = y + size * 0.4 * math.sin(angle)
        points.append((px, py))

    if len(points) > 2:
        pygame.draw.polygon(surface, color, points)

    pygame.draw.circle(surface, (255, 255, 0), (x, y), int(size * 0.2))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

def draw_daisy_flower(surface, x, y, color=(230, 230, 250), size=30):
    for i in range(12):
        angle = math.radians(i * 30)
        px1 = x + size * 0.5 * math.cos(angle)
        py1 = y + size * 0.5 * math.sin(angle)

        pygame.draw.ellipse(surface, color, 
                           (px1 - size * 0.3, py1 - size * 0.3, 
                            size * 0.6, size * 0.6))

    pygame.draw.circle(surface, (255, 255, 0), (x, y), int(size * 0.3))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

def draw_trumpet_flower(surface, x, y, color=(255, 255, 255), size=30):
    for i in range(8):
        angle = math.radians(i * 45)
        px = x + size * 0.7 * math.cos(angle)
        py = y + size * 0.7 * math.sin(angle)
        
        pygame.draw.ellipse(surface, color, 
                           (px - size * 0.3, py - size * 0.3, 
                            size * 0.6, size * 0.6))
    
    pygame.draw.circle(surface, YELLOW, (x, y), int(size * 0.3))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

def draw_spike_flower(surface, x, y, color=(148, 0, 211), size=30):
    for i in range(12):
        angle = math.radians(i * 30)
        end_x = x + size * math.cos(angle)
        end_y = y + size * math.sin(angle)
        pygame.draw.line(surface, color, (x, y), (int(end_x), int(end_y)), 3)
    
    pygame.draw.circle(surface, YELLOW, (x, y), int(size * 0.2))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

def draw_cluster_flower(surface, x, y, color=(255, 165, 0), size=30):
    for i in range(7):
        angle = math.radians(i * 51)
        px = x + size * 0.5 * math.cos(angle)
        py = y + size * 0.5 * math.sin(angle)
        pygame.draw.circle(surface, color, (int(px), int(py)), int(size * 0.25))
    
    pygame.draw.circle(surface, YELLOW, (x, y), int(size * 0.15))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

def draw_orchid_flower(surface, x, y, color=(255, 182, 193), size=30):
    for i in range(5):
        angle = math.radians(i * 72)
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        
        if i % 2 == 0:
            petal_size = size * 0.6
        else:
            petal_size = size * 0.4
            
        pygame.draw.ellipse(surface, color, 
                           (px - petal_size, py - petal_size, 
                            petal_size * 2, petal_size * 2))
    
    pygame.draw.circle(surface, YELLOW, (x, y), int(size * 0.2))
    pygame.draw.line(surface, (0, 100, 0), (x, int(y + size * 0.5)), (x, int(y + size * 2)), 3)

flower_functions = {
    "bell": draw_bell_flower,
    "star": draw_star_flower,
    "trumpet": draw_trumpet_flower,
    "daisy": draw_daisy_flower,
    "spike": draw_spike_flower,
    "cluster": draw_cluster_flower,
    "orchid": draw_orchid_flower
}

def main():
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        
        draw_bell_flower(screen, 100, 300)
        draw_star_flower(screen, 200, 300)
        draw_trumpet_flower(screen, 300, 300)
        draw_daisy_flower(screen, 400, 300)
        draw_spike_flower(screen, 500, 300)
        draw_cluster_flower(screen, 600, 300)
        draw_orchid_flower(screen, 700, 300)
        
        title = large_font.render("Flower Garden Demo", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()