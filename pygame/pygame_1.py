import pygame
import random


# Inicia som:
pygame.mixer.init()
# Inicia fonte:
pygame.font.init()

# Dimensões da tela:
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Quantidade de quadradinhos iniciais:
quadrados_iniciais = 20

# Outras inicializações:
terminou = False
tempo_inicial = 10
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
     
def mostra_pontuacao_final(tela, pontos):
    tela.fill(preto) # Limpa tela
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " quadradinhos", 1, branco)
    textpos = text.get_rect(center=(tela.get_width()/2, tela.get_height()/2))
    tela.blit(text, textpos)
    
# Início do programa

# Desenhar os quadrados iniciais    
lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)
    
# Indica o relógio de aparecimento de quadros do jogo
clock = pygame.time.Clock()    

#variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

# Variável contar quantos quadradinhos clicou
pontos = 0

# variável para contar quantos segundos se passaram
conta_segundos = tempo_inicial

# Inserindo efeito sonoro
efeito = pygame.mixer.Sound('click.wav')

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
                    efeito.play()
                    lista.remove(q)
                    pontos = pontos + 1
                    
        if event.type == pygame.QUIT:
            terminou = True
            
    conta_clocks = conta_clocks + 1
    
    # A cada 50 conta_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        if conta_segundos >= 0:
            conta_segundos = conta_segundos - 1
        conta_clocks = 0                  
    # cria um novo quadradinho a cada segundo
        q = Quadradinho()
        lista.append(q)
    
    if conta_segundos >= 0: # Neste caso, ainda tem tempo
        #limpar tela e atualizar texto
        tela.fill(preto)       
    #tela foi apagada, desenha os quadrados novamente
        for i in lista:
            i.desenha(tela)        
        #mostra tempo atualizado
        mostra_tempo(conta_segundos, pontos)
    else: # Acabou o tempo de 10s
        #Exibe a tela final
        mostra_pontuacao_final(tela, pontos)
        #Remover todos os quadrados da lista
        for q in lista:
            lista.remove(q)
            
            
    #atualiza o desenho na tela
    pygame.display.update()
    
    #Configura 50 atualizações de tela por segundo
    clock.tick(50)
            
#finaliza a tela do jogo
pygame.display.quit()

