import pygame

#inicia game
pygame.init()

#define tamanho da tela
tela = pygame.display.set_mode((800, 600))

terminou = False

#cria relógio
clock = pygame.time.Clock()

#definição de cor 
azul_pantone = (167,198,237)
rosa_pantone = (255,128,139)

#desenha um quadrado com a cor azul e espessura 3
pygame.draw.rect(tela, azul_pantone, (100,100,30,30))
#desenha um quadrado com a cor rosa preenchido
pygame.draw.rect(tela, rosa_pantone, (200,200,30,30))

while not terminou:
    #checa os eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            
    #atualiza o desenho na tela
    pygame.display.update()
    
    #Configura 50 atualizações de tela por segundo
        clock.tick(50)
            
#finaliza a tela do jogo
pygame.display.quit()
#finaliza o pygame
pygame.quit()
