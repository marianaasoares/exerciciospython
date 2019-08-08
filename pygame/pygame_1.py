import pygame
import random

#inicia game
pygame.init()
largura_tela = 800
altura_tela = 600
quadrados_iniciais = 20
#define tamanho da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

#cria relógio
clock = pygame.time.Clock()

#classe Quadradinho
class Quadradinho():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela-self.largura)
        self.y = random.randint(0, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
         
lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)


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
