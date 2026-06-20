import pygame
from src.dados import carregar_historico
from src.funcoes import (desenhar_historico)
from src.config import (LARGURA_TELA, ALTURA_TELA, CAMINHO_FUNDO_INICIAL, CAMINHO_FUNDO_HISTORICO, CAMINHO_FUNDO_FIM, CAMINHO_LOGO, CAMINHO_TITULO_PAUSE, CAMINHO_BTN_HISTORICO, CAMINHO_START, CAMINHO_RESUME, CAMINHO_EXIT, CAMINHO_BACK)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

logo = pygame.image.load(CAMINHO_LOGO).convert_alpha()
logo = pygame.transform.scale(logo, (700, 350))
titulo_pause = pygame.image.load(CAMINHO_TITULO_PAUSE).convert_alpha()
titulo_pause = pygame.transform.scale(titulo_pause, (600, 171))
start_img = pygame.image.load(CAMINHO_START).convert_alpha()
resume_img = pygame.image.load(CAMINHO_RESUME).convert_alpha()
exit_img = pygame.image.load(CAMINHO_EXIT).convert_alpha()
back_img = pygame.image.load(CAMINHO_BACK).convert_alpha()
historico_img = pygame.image.load(CAMINHO_BTN_HISTORICO).convert_alpha()
fundo_inicial = pygame.image.load(CAMINHO_FUNDO_INICIAL).convert_alpha()
fundo_inicial = pygame.transform.scale(fundo_inicial, (1400, 600))
fundo_historico = pygame.image.load(CAMINHO_FUNDO_HISTORICO).convert_alpha()
fundo_historico = pygame.transform.scale(fundo_historico, (1400, 600))
fundo_fim = pygame.image.load(CAMINHO_FUNDO_FIM).convert_alpha()
fundo_fim = pygame.transform.scale(fundo_fim, (1400, 600))

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), (int(height*scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def is_clicked(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos)
        )
    def draw(self):
        tela.blit(self.image, (self.rect.x, self.rect.y))

def tela_inicio(tela):

    pygame.mixer.init()
    som_titulo = pygame.mixer.Sound("assets/sons/Logo.wav")
    som_titulo.set_volume(0.7)
    som_titulo.play()

    pygame.mixer.music.load("assets/sons/Menu.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    start_button = Button(0, 360, start_img, 0.18)
    start_button.rect.x = LARGURA_TELA // 2 - start_button.rect.width // 2
    historic_button = Button(0, 420, historico_img, 0.23)
    historic_button.rect.x = LARGURA_TELA // 2 - historic_button.rect.width // 2
    exit_button = Button(0, 480, exit_img, 0.15)
    exit_button.rect.x = LARGURA_TELA // 2 - exit_button.rect.width // 2

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT or exit_button.is_clicked(evento):
                pygame.mixer.music.stop()
                return "exit"
            
            if start_button.is_clicked(evento):
                pygame.mixer.music.stop()
                return "start"
            
            if historic_button.is_clicked(evento):
                return "historico"
            
        tela.blit(fundo_inicial, (0, 0))
        tela.blit(logo, (LARGURA_TELA // 2 - logo.get_width() // 2, 0))
        start_button.draw()
        exit_button.draw()
        historic_button.draw()
        pygame.display.flip()

def tela_historico(tela):

    back_button = Button(0, 530, back_img, 0.14)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    partidas = carregar_historico()
    fonte = pygame.font.SysFont("Arial", 24, True)

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return "exit"
            
            if back_button.is_clicked(evento):
                return "menu"

        tela.blit(fundo_historico, (0, 0))
        tela.blit(fonte.render("DATA", True, (255,255,255)),(360, 205))
        tela.blit(fonte.render("CAMPEÃO", True, (255,255,255)),(650, 205))
        tela.blit(fonte.render("DURAÇÃO", True, (255,255,255)),(980, 205))
        desenhar_historico(tela, partidas, fonte)
        back_button.draw()
        pygame.display.flip()

def tela_pause(tela):
    resume_button = Button(0, 410, resume_img, 0.2)
    resume_button.rect.x = LARGURA_TELA // 2 - resume_button.rect.width // 2
    exit_button = Button(0, 480, exit_img, 0.15)
    exit_button.rect.x = LARGURA_TELA // 2 - exit_button.rect.width // 2

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return "exit"

            if exit_button.is_clicked(evento):
                return "menu"
            
            if resume_button.is_clicked(evento):
                return "continuar"

        tela.blit(fundo_inicial, (0, 0))
        tela.blit(titulo_pause, (LARGURA_TELA // 2 - titulo_pause.get_width() // 2, 40))
        resume_button.draw()
        exit_button.draw()
        pygame.display.flip()

def tela_fim(tela, mensagem):

    back_button = Button(0, 530, back_img, 0.14)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    fonte = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 36)
    fonte_sub = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 26)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "exit"
            if back_button.is_clicked(evento):
                return "menu"
        tela.blit(fundo_fim, (0, 0))
        texto = fonte.render(mensagem, True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(LARGURA_TELA // 2 + 15, ALTURA_TELA // 2 + 35))
        tela.blit(texto, texto_rect)
        subtexto = fonte_sub.render("CAMPEÃO", True, (255, 215, 0))
        tela.blit(subtexto, (LARGURA_TELA // 2 - subtexto.get_width() // 2, ALTURA_TELA // 2 - 60))
        back_button.draw()
        pygame.display.flip()