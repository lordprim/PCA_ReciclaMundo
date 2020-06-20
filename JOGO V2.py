# Biblioteca usada para o desenvolvimento do jogo:
import pygame

# Randint utilizado para gerar números aleatórios:
from random import randint

# Inicialização da biblioteca:
pygame.init()

# Class das lixeiras:
class lixeiro(object):
    def __init__(self,x,y,velocidade,lix):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.lix = lix

# Classe da Fase:
class fase(object):
    def __init__(self):
        self.imagem = pygame.image.load('fundojogo.jpg')
        self.numero = 1

# Classe dos Objetos:
class objeto(object):
    def __init__(self,objetoImagem,pos_x,pos_y,objetoVelocidade):
        self.objetoImagem = objetoImagem
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.objetoVelocidade = objetoVelocidade

# Instancias das classes:
# Classe da Lixeira:
lixeira = lixeiro(350,450,30,pygame.image.load('LixeiraVerde.png'))
# Classe do fundo de tela:
fundo = fase()
# Classe do objeto:
lixo = objeto(pygame.image.load('GarrafaPCA.png'),randint(1,350),randint(-350,-100),randint(8,11))
lixo2 = objeto(pygame.image.load('GarrafaPCA.png'),randint(450,600),randint(-800,-550),randint(8,11))

# Variavel dos pontos:
ponto = 0

# Contagem de pontos:
# Fonte:
font = pygame.font.SysFont('arial black',30)
# Texto/Cor:
texto = font.render('Pontos: ',True,(0,0,0),(255,255,255))
# Posição:
pos_texto = texto.get_rect()
pos_texto.center = (400,15)

# Resolução da tela:
janela = pygame.display.set_mode((800,600))

# Nome na barra do jogo:
pygame.display.set_caption("ReciclaMundo")

# Imagem Inicio e Fim:
# Imagem tela inicio:
TelaInicio = pygame.image.load('InicioTela.png')
# Imagem tela final:
TelaFinal = pygame.image.load('TelaFinal.png')

# Definição de cor:
azul = (0, 0, 255)
verde = (0, 155, 155)
vermelho = (255, 0, 0)

# Inicio da tela:
intro = True

# Inicio do Jogo:
janela_aberta = True
while janela_aberta:
    #Tela de Inicio do Jogo:
    while intro:
        # Opção para fechar o jogo pelo X:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Opções para começar e fechar o jogo:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_s:
                    pygame.quit()
                    quit()

        # Carregando a imagem de começo do jogo:
        janela.blit(TelaInicio, (0, 0))
        # Fonte da tela:
        myfont = pygame.font.SysFont("arial", 20)
        # Texto na tela:
        nlabel = myfont.render("Pressione C para começar, ou S para sair", 1, verde)
        # Posição do texto na tela:
        janela.blit(nlabel, (220, 545))
        # Atualização das informações na tela:
        pygame.display.flip()
        pygame.display.update()

# Frames do jogo:
    pygame.time.delay(50)

# Evento de finalização do programa:
    for event in pygame.event.get():
        #  Opção para fechar o jogo pelo X:
        if event.type == pygame.QUIT:
            janela_aberta = False

# Configuração das teclas:
    comandos = pygame.key.get_pressed()
    # Movimento para a direita:
    if comandos[pygame.K_RIGHT] and lixeira.x <= 680:
        lixeira.x += lixeira.velocidade
    # Movimento para a esquerda:
    if comandos[pygame.K_LEFT] and lixeira.x >= 20:
        lixeira.x -= lixeira.velocidade

# Funções/posição do objeto 1:
    if (lixo.pos_y >= 460):
        lixo.pos_y = randint(-350,-100)
        lixo.pos_x = randint(1,350)
# Funções/posição do objeto 1:
    if (lixo2.pos_y >= 460):
        lixo2.pos_y = randint(-800,-550)
        lixo2.pos_x = randint(450,600)

# Detecta colisão com objeto 1:
    if (lixeira.x <= lixo.pos_x <= (lixeira.x + 110)) and (lixeira.y <= lixo.pos_y):
        # Contabilizando os pontos:
        ponto += 1
        texto = font.render('Pontos: ' + str(ponto), True, (0, 0, 0), (255, 255, 255))
# Detecta colisão com objeto 2:
    if (lixeira.x <= lixo2.pos_x <= (lixeira.x + 100)) and (lixeira.y <= lixo2.pos_y):
        # Contabilizando os pontos:
        ponto += 1
        texto = font.render('Pontos: ' + str(ponto), True, (0, 0, 0), (255, 255, 255))

# Passagem de fases:
    # Fase 1:
    if ponto == 5:
        ponto = 0
        fundo.numero += 1
        # Fase 2:
        if fundo.numero == 2:
            # Carregando as imagens da segunda fase:
            lixo.objetoImagem = pygame.image.load('Papel.png')
            lixo2.objetoImagem = pygame.image.load('Papel.png')
            lixeira.lix = pygame.image.load('LixeiraAzul.png')
        # Fase 3:
        if fundo.numero == 3:
            # Carregando as imagens da terceira fase:
            lixo.objetoImagem = pygame.image.load('Metais.png')
            lixo2.objetoImagem = pygame.image.load('Metais.png')
            lixeira.lix = pygame.image.load('LixeiraAmarela.png')
        # Fase 4:
        if fundo.numero == 4:
            # Carregando as imagens da quarta fase:
            lixo.objetoImagem = pygame.image.load('Plastico.png')
            lixo2.objetoImagem = pygame.image.load('Plastico.png')
            lixeira.lix = pygame.image.load('LixeiraVermelha.png')
        # Fase 5:
        if fundo.numero == 5:
            # Carregando as imagens da quinta fase:
            lixo.objetoImagem = pygame.image.load('NaoRecicla.png')
            lixo2.objetoImagem = pygame.image.load('NaoRecicla.png')
            lixeira.lix = pygame.image.load('LixeiraCinza.png')
        # Tela de fim de jogo:
        if fundo.numero == 6:
            final = True
            # Abertura da tela de fim de jogo:
            while final:
                # Opção para fechar o jogo pelo X:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    # Opções para recomeçar e fechar o jogo:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            # Chamada da tela inicial:
                            intro = True
                            # Finalizando a tela de fim de jogo:
                            final = False
                            # Recarregando as imagens da primeira fase:
                            ponto = 0
                            fundo.numero = 1
                            lixeira = lixeiro(350, 450, 30, pygame.image.load('LixeiraVerde.png'))
                            lixo = objeto(pygame.image.load('GarrafaPCA.png'), randint(1, 350), randint(-350, -100),
                                          randint(8, 11))
                            lixo2 = objeto(pygame.image.load('GarrafaPCA.png'), randint(450, 600), randint(-800, -550),
                                           randint(8, 11))
                        # Função para fechar o jogo com a tecla S:
                        if event.key == pygame.K_s:
                            pygame.quit()
                            quit()

                # Carregando a imagem de fim de jogo:
                janela.blit(TelaFinal, (0, 0))
                # Fontes da tela de fim de jogo:
                myfont1 = pygame.font.SysFont("arial", 20)
                myfont2 = pygame.font.SysFont("arial", 20)
                # Textos na tela de fim de jogo:
                nlabel1 = myfont1.render("Você conseguiu!!", 1, vermelho)
                nlabel2 = myfont2.render("Toque R para recomeçar, ou S para sair!", 1, azul)
                # Posição das frases na tela de fim de jogo:
                janela.blit(nlabel1, (315, 500))
                janela.blit(nlabel2, (220, 520))
                # Atualização das informações na tela:
                pygame.display.flip()
                pygame.display.update()

# Velocidade dos objetos:
    lixo.pos_y += lixo.objetoVelocidade
    lixo2.pos_y += lixo2.objetoVelocidade

# Adicionando os objetos na tela:
    janela.blit(fundo.imagem, (0,0))
    janela.blit(lixeira.lix, (lixeira.x,lixeira.y))
    janela.blit(lixo.objetoImagem, (lixo.pos_x, lixo.pos_y))
    janela.blit(lixo2.objetoImagem, (lixo2.pos_x, lixo2.pos_y))
    janela.blit(texto,pos_texto)
    pygame.display.update()
pygame.quit()