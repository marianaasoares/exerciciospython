import pygame

pygame.init()

azul_pantone = (167,198,237)
screen.fill(255,167,145)

tela = pygame.display.set_mode((800, 600))

terminou = False

while not terminou:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()

pygame.quit()