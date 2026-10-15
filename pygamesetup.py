import pygame
import time
import pygame.font

pygame.init()

WIDTH = 640
HEIGHT = 480
BG = ("green")
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame test game")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("newtimesroman",50)


def spawn_coins():
    coins = [
        pygame.Rect(40, 220, 40, 40),
        pygame.Rect(100, 200, 20, 20),
        pygame.Rect(500, 100, 20, 20),
    ]
    return coins


def draw_text(surface, font, message, x, y, color="yellow"):
    """Render a message on a pygame surface."""
    text = font.render(str(message), True, color)
    return surface.blit(text, (x, y))

player = pygame.Rect(80, 200, 50, 50)
base_speed = 4
sprint_speed = 10
coins = spawn_coins()

score = 0
won = False
running = True


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    shift_down = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    if not won:
        move_speed = sprint_speed if shift_down else base_speed

        if keys[pygame.K_LEFT]:
            player.x -= move_speed
        if keys[pygame.K_RIGHT]:
            player.x += move_speed
        if keys[pygame.K_UP]:
            player.y -= move_speed
        if keys[pygame.K_DOWN]:
            player.y += move_speed

        bounds = screen.get_rect()
        player.clamp_ip(bounds)
        
    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
        if score == 10:
            won = True
        if len(coins) == 0:
            coins = spawn_coins()
    screen.fill(BG)

    for coin in coins:
        pygame.draw.rect(screen, "gold", coin)
        
    pygame.draw.rect(screen, "red", player)
    
    draw_text(screen, FONT, f"score: {score}/10", 15, 15)
    
    if won: draw_text(
        screen,
        FONT,
        "you won and you suck lol",
        150,
        220
    )
    

    pygame.display.flip()

pygame.quit()