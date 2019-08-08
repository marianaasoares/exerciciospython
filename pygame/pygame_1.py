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

preto = (0, 0, 0)
branco = (255, 255, 255)

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
         
def mostra_tempo(tempo):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s", 1, branco)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)
         
lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)

#variavel para contar quantas esperas de 50Hz ou 0,02s
    conta_clocks = 0

# variável para contar quantos segundos se passaram
conta_segundos = 0
mostra_tempo(conta_segundos)

while not terminou:
    #checa os eventos do mouse
    for event in pygame.event.get():
        #Clicando...
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # obtém as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()
            # checa se clicou em algum quadradinho
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                    pontos = pontos + 1
                    
        if event.type == pygame.QUIT:
            terminou = True
            
    conta_clocks = conta_clocks + 1
    
    # A casa 50 conta_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        conta_segundos = conta_segundos + 1
        conta_clocks = 0
    # cria um novo quadradinho a cada segundo
    q = Quadradinho()
    lista.append(q)
    
    #limpar tela e atualizar texto
    tela.fill(preto)
    
    #tela foi apagada, desenha os quadrados novamente
    for q in lista:
        q.desenha(tela)
    
    #mostra tempo atualizado
    mostra_tempo(conta_segundos)
    
    #atualiza o desenho na tela
    pygame.display.update()
    
    #Configura 50 atualizações de tela por segundo
    clock.tick(50)
            
#finaliza a tela do jogo
pygame.display.quit()
#finaliza o pygame
pygame.quit()
