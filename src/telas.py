import pygame
from src.dados import carregar_historico
from src.funcoes import (desenhar_historico, desenhar_elementos_telas_sec)
from src.config import (LARGURA_TELA, ALTURA_TELA)

# Inicializa a janela do jogo e carrega todos os elementos gráficos utilizados nas telas secundárias
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
elementos_telas_sec = desenhar_elementos_telas_sec();

class Button():
    def __init__(self, x, y, image, scale):
        """
        Inicializa um botão.

        Parâmetros:
            x (int): Posição horizontal do botão.
            y (int): Posição vertical do botão.
            image (pygame.Surface): Imagem utilizada como botão.
            scale (float): Escala aplicada à imagem do botão.

        Retorno:
            Não retorna nada
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), (int(height*scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def is_clicked(self, evento):
        """
        Verifica se o botão foi clicado.

        Parâmetros:
            evento (pygame.event.Event): Evento capturado pelo Pygame.

        Retorno:
            bool: True caso o botão tenha sido clicado com o botão esquerdo
            do mouse e False caso contrário.
        """
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos)
        )
    def draw(self):
        """
        Desenha o botão na tela.

        Parâmetros:
            Nenhum (apenas o self).

        Retorno:
            Não retorna nada.
        """
        tela.blit(self.image, (self.rect.x, self.rect.y))

def tela_inicio(tela):
    """
    Exibe o menu principal do jogo com seus elementos visuais e permite ao jogador iniciar uma partida, visualizar o histórico
    de partidas ou encerrar a aplicação.

    Parâmetros:
        tela (pygame.Surface): Superfície onde os elementos serão desenhados.

    Retorno:
        str: Uma das seguintes ações:
            - "start": iniciar uma partida.
            - "historico": abrir a tela de histórico.
            - "exit": encerrar o jogo.
    """

    pygame.mixer.init()
    som_titulo = pygame.mixer.Sound("assets/sons/Logo.wav")
    som_titulo.set_volume(0.7)
    som_titulo.play()

    pygame.mixer.music.load("assets/sons/Menu.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    start_button = Button(0, 360, elementos_telas_sec["btn_start"], 0.18)
    start_button.rect.x = LARGURA_TELA // 2 - start_button.rect.width // 2
    historic_button = Button(0, 420, elementos_telas_sec["btn_historico"], 0.23)
    historic_button.rect.x = LARGURA_TELA // 2 - historic_button.rect.width // 2
    exit_button = Button(0, 480, elementos_telas_sec["btn_exit"], 0.15)
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
            
        tela.blit(elementos_telas_sec["fundo_inicial"], (0, 0))
        tela.blit(elementos_telas_sec["logo"], (LARGURA_TELA // 2 - elementos_telas_sec["logo"].get_width() // 2, 0))
        start_button.draw()
        exit_button.draw()
        historic_button.draw()
        pygame.display.flip()

def tela_historico(tela):
    """
    Exibe a tela de histórico de partidas com seus elementos visuais e carrega os registros salvos (os cinco último) e apresenta suas informações na tela. Também permite ao jogador voltar ao menu inicial ou encerrar a aplicação.

    Parâmetros:
        tela (pygame.Surface): Superfície onde os elementos serão desenhados.

    Retorno:
        str: Uma das seguintes ações:
            - "menu": retornar ao menu principal.
            - "exit": encerrar o jogo.
    """

    back_button = Button(0, 530, elementos_telas_sec["btn_back"], 0.14)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    partidas = carregar_historico()
    fonte = pygame.font.SysFont("Arial", 24, True)

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return "exit"
            
            if back_button.is_clicked(evento):
                return "menu"

        tela.blit(elementos_telas_sec["fundo_historico"], (0, 0))
        tela.blit(fonte.render("DATA", True, (255,255,255)),(360, 205))
        tela.blit(fonte.render("CAMPEÃO", True, (255,255,255)),(650, 205))
        tela.blit(fonte.render("DURAÇÃO", True, (255,255,255)),(980, 205))
        desenhar_historico(tela, partidas, fonte)
        back_button.draw()
        pygame.display.flip()

def tela_pause(tela):
    """
    Exibe a tela de pausa da partida com seus elementos visuais e permite ao jogador continuar a partida ou retornar ao menu principal.

    Parâmetros:
        tela (pygame.Surface): Superfície onde os elementos serão desenhados.

    Retorno:
        str: Uma das seguintes ações:
            - "continuar": retomar a partida.
            - "menu": voltar ao menu principal.
            - "exit": encerrar o jogo.
    """
    resume_button = Button(0, 410, elementos_telas_sec["btn_resume"], 0.2)
    resume_button.rect.x = LARGURA_TELA // 2 - resume_button.rect.width // 2
    exit_button = Button(0, 480, elementos_telas_sec["btn_exit"], 0.15)
    exit_button.rect.x = LARGURA_TELA // 2 - exit_button.rect.width // 2

    while True:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                return "exit"

            if exit_button.is_clicked(evento):
                return "menu"
            
            if resume_button.is_clicked(evento):
                return "continuar"

        tela.blit(elementos_telas_sec["fundo_inicial"], (0, 0))
        tela.blit(elementos_telas_sec["titulo_pause"], (LARGURA_TELA // 2 - elementos_telas_sec["titulo_pause"].get_width() // 2, 40))
        resume_button.draw()
        exit_button.draw()
        pygame.display.flip()

def tela_fim(tela, mensagem):
    """
    Exibe a tela de encerramento da partida com seus elementos visuais e apresenta a mensagem informando o campeão e permite retornar ao
    menu principal.

    Parâmetros:
        tela (pygame.Surface): Superfície onde os elementos serão desenhados.
        mensagem (str): Texto indicando o vencedor da partida.

    Retorno:
        str: Uma das seguintes ações:
            - "menu": retornar ao menu principal.
            - "exit": encerrar o jogo.
    """

    back_button = Button(0, 530, elementos_telas_sec["btn_back"], 0.14)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    fonte = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 36)
    fonte_sub = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 26)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "exit"
            if back_button.is_clicked(evento):
                return "menu"
        tela.blit(elementos_telas_sec["fundo_fim"], (0, 0))
        texto = fonte.render(mensagem, True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(LARGURA_TELA // 2 + 15, ALTURA_TELA // 2 + 35))
        tela.blit(texto, texto_rect)
        subtexto = fonte_sub.render("CAMPEÃO", True, (255, 215, 0))
        tela.blit(subtexto, (LARGURA_TELA // 2 - subtexto.get_width() // 2, ALTURA_TELA // 2 - 60))
        back_button.draw()
        pygame.display.flip()