import pygame
import random
import sys

pygame.init()

# visualizer Window settings here
WIDTH = 900
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GG")

# Colors use in the window
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont("arial", 20)

# Generate random array
def generate_array(size):
    return [random.randint(50, 500) for i in range(size)]

# Draw bars
def draw_array(arr, color_positions={}, speed=60):
    WIN.fill(WHITE)
    bar_width = WIDTH // len(arr)

    for i, val in enumerate(arr):
        x = i * bar_width
        y = HEIGHT - val
        color = color_positions.get(i, BLUE)
        pygame.draw.rect(WIN, color, (x, y, bar_width, val))

    # Display instructions
    text = FONT.render("SPACE: Start | R: Reset | UP/DOWN: Speed", True, BLACK)
    WIN.blit(text, (10, 10))

    pygame.display.update()

# Bubble sort generator
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):

            #Show comparison
            yield arr, {j: RED, j + 1: RED}

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                #Show swap
                yield arr, {j: GREEN, j + 1: GREEN}

    yield arr, {}

# Main loop
def main():
    clock = pygame.time.Clock()
    size = 80
    arr = generate_array(size)

    sorting = False
    generator = None
    speed = 60

    running = True
    while running:
        clock.tick(speed)

        if sorting:
            try:
                arr, color_positions = next(generator)
                draw_array(arr, color_positions)
            except StopIteration:
                sorting = False
        else:
            draw_array(arr)
# Hardware Control codes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    generator = bubble_sort(arr)

                if event.key == pygame.K_r:
                    arr = generate_array(size)
                    sorting = False

                if event.key == pygame.K_UP:
                    speed += 10

                if event.key == pygame.K_DOWN:
                    speed = max(10, speed - 10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
