import pygame
from src.config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, CAMINHO_CENARIO, CAMINHO_FUNDO_INICIAL, CAMINHO_FUNDO_HISTORICO, CAMINHO_LOGO, CAMINHO_BTN_HISTORICO, CAMINHO_ARQ_HISTORICO, CAMINO_START, CAMINHO_EXIT, CAMINHO_BACK)
from src.funcoes import ( desenhar_barra_vida, desenhar_barra_ultimate, verificar_ataque, limitar_valor, carregar_historico, desenhar_historico )
from src.personagem import Personagem
from datetime import datetime

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
logo = pygame.image.load(CAMINHO_LOGO).convert_alpha()
logo_redimensionada = pygame.transform.scale(logo, (700, 350))
start_img = pygame.image.load(CAMINO_START).convert_alpha()
exit_img = pygame.image.load(CAMINHO_EXIT).convert_alpha()
back_img = pygame.image.load(CAMINHO_BACK).convert_alpha()
historico_img = pygame.image.load(CAMINHO_BTN_HISTORICO).convert_alpha()


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

    start_button = Button(0, 360, start_img, 0.18)
    start_button.rect.x = LARGURA_TELA // 2 - start_button.rect.width // 2
    historic_button = Button(0, 420, historico_img, 0.23)
    historic_button.rect.x = LARGURA_TELA // 2 - historic_button.rect.width // 2
    exit_button = Button(0, 480, exit_img, 0.15)
    exit_button.rect.x = LARGURA_TELA // 2 - exit_button.rect.width // 2

    fundo_inicial = pygame.image.load(CAMINHO_FUNDO_INICIAL).convert_alpha()
    fundo_inicial = pygame.transform.scale(fundo_inicial, (1400, 600))

    esperando = True
    while esperando:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT or exit_button.is_clicked(evento):
                pygame.quit()
                return False
            
            if start_button.is_clicked(evento):
                return True
            
            if historic_button.is_clicked(evento):
                tela_historico(tela)
            
        tela.blit(fundo_inicial, (0, 0))
        tela.blit(logo_redimensionada, (LARGURA_TELA // 2 - logo_redimensionada.get_width() // 2, 0))
        start_button.draw()
        exit_button.draw()
        historic_button.draw()
        pygame.display.flip()

    return True

def tela_historico(tela):

    back_button = Button(0, 530, back_img, 0.14)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    fundo_historico = pygame.image.load(CAMINHO_FUNDO_HISTORICO).convert_alpha()
    fundo_historico = pygame.transform.scale(fundo_historico, (1400, 600))
    partidas = carregar_historico()
    fonte = pygame.font.SysFont("Arial", 24, True)
    esperando = True
    while esperando:

        tela.blit(fundo_historico, (0, 0))
        tela.blit(fonte.render("DATA", True, (255,255,255)),(360, 205))
        tela.blit(fonte.render("CAMPEÃO", True, (255,255,255)),(650, 205))
        tela.blit(fonte.render("DURAÇÃO", True, (255,255,255)),(980, 205))
        desenhar_historico(tela, partidas, fonte)
        back_button.draw()

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if back_button.is_clicked(evento):
                return True
        pygame.display.flip()

    return True

def tela_fim(tela):

    back_button = Button(0, 300, back_img, 0.18)
    back_button.rect.x = LARGURA_TELA // 2 - back_button.rect.width // 2

    fundo_inicial = pygame.image.load(CAMINHO_FUNDO_INICIAL).convert_alpha()
    fundo_inicial = pygame.transform.scale(fundo_inicial, (1400, 600))

    esperando = True
    while esperando:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if back_button.is_clicked(evento):
                return True
            
        tela.blit(fundo_inicial, (0, 0))
        back_button.draw()
        pygame.display.flip()

    return True



def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()

    pygame.display.set_caption(TITULO_JOGO)
    cenario = pygame.image.load(CAMINHO_CENARIO).convert()
    cenario = pygame.transform.scale(cenario, (1400, 600))
    tela.blit(cenario, (0, 0))

    if not tela_inicio(tela):
        return
    
    todas_sprites = pygame.sprite.Group()
    personagem1 = Personagem(100)
    personagem2 = Personagem(1100)
    personagem2.direcao = -1
    todas_sprites.add(personagem1)
    todas_sprites.add(personagem2)

    relogio = pygame.time.Clock()
    rodando = True
    vencedor = False
    velocidade = 5
    inicio_partida = datetime.now()
    inicio_luta = pygame.time.get_ticks() # Define o início do tempo de luta quando as animações são carregadas
    tempo_luta = 121 # Define o tempo de luta em segundos
    fonte = pygame.font.SysFont("Arial", 40, True) # Define o estilo da fonte do cronômetro
    

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:

        tempo_atual = pygame.time.get_ticks() # Define o tempo atual o mesmo do início da luta
        tempo_restante = tempo_luta - ((tempo_atual - inicio_luta) / 1000) # Defino o tempo_restante como o tempo de luta menos o tempo percorrido
        tempo_restante = max(0, tempo_restante) # Define o máximo do tempo restante (que só vai até 0)

        """ Trecho de código que formata o tempo para minutos e segundos """
        segundos = int(tempo_restante)
        minutos = segundos // 60
        segundos = segundos % 60
        tempo_formatado = f"{minutos:02}:{segundos:02}"

        """ Condição que define que se o tempo restante for menor ou igual a 0, o loop principal se encerra """
        if tempo_restante <= 0:
            rodando = False
            
        verificar_ataque(personagem1, personagem2) 
        verificar_ataque(personagem2, personagem1)

        # Envia o conteúdo desenhado (barra de vida) para a tela visível
        pygame.display.flip()

        relogio.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Ataques dos personagens
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    personagem1.atacar()
                if evento.key == pygame.K_UP:
                    personagem2.atacar()

        # Se alguum dos personagens atingir 0 de pontos de vida, o jogo acaba
        if personagem1.vida <= 0 or personagem2.vida <= 0:
            vencedor = True
            rodando = False
            

        teclas = pygame.key.get_pressed()
        personagem1.estado = "idle"
        personagem2.estado = "idle"
        # Movimentação alterando direto o eixo X do retângulo do jogador
        if teclas[pygame.K_LEFT]:
            personagem2.rect.x -= velocidade
            personagem2.estado = "run"
            personagem2.direcao = -1
        if teclas[pygame.K_RIGHT]:
            personagem2.rect.x += velocidade
            personagem2.estado = "run"
            personagem2.direcao = 1
        if teclas[pygame.K_a]:
            personagem1.rect.x -= velocidade
            personagem1.estado = "run"
            personagem1.direcao = -1
        if teclas[pygame.K_d]:
            personagem1.rect.x += velocidade
            personagem1.estado = "run"
            personagem1.direcao = 1

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        personagem1.rect.x = limitar_valor(personagem1.rect.x, 0, LARGURA_TELA - personagem1.rect.width)
        personagem1.rect.y = limitar_valor(personagem1.rect.y, 0, ALTURA_TELA - personagem1.rect.height)
        personagem2.rect.x = limitar_valor(personagem2.rect.x, 0, LARGURA_TELA - personagem2.rect.width)
        personagem2.rect.y = limitar_valor(personagem2.rect.y, 0, ALTURA_TELA - personagem2.rect.height)

        # Caption da tela do jogo
        pygame.display.set_caption(TITULO_JOGO)

        tela.blit(cenario, (0, 0))

        # Desenha a barra de vida e de ultimate e vai atualizando enquanto o jogo roda
        desenhar_barra_vida(tela, 90, 30, personagem1.vida, personagem1.vida_maxima)
        desenhar_barra_vida(tela, 1000, 30, personagem2.vida, personagem2.vida_maxima)
        desenhar_barra_ultimate(tela, 90, 60, personagem1.ultimate, personagem1.ultimate_maximo)
        desenhar_barra_ultimate(tela, 1000, 60, personagem2.ultimate, personagem2.ultimate_maximo)

        """ Renderiza o tempo formatado na tela """
        if tempo_restante > 10:
            texto = fonte.render(
                tempo_formatado,
                True,
                (255, 255, 255)
            )
        else:
            texto = fonte.render(
                tempo_formatado,
                True,
                (255, 0, 0) # Define que a partir dos 10 segundos finais, a cor do tempo é alterada para vermelho
            )

        """ Coloca o tempo na tela do jogo """
        tela.blit(texto, (630, 20))

        todas_sprites.update()
        for sprite in todas_sprites:
            sprite.draw(tela)
        pygame.display.flip()

    if vencedor:
        if personagem1.vida > 0:
            campeao = "Jogador 1"
        else:
            campeao = "Jogador 2"

        fim_partida = datetime.now()
        duracao = fim_partida - inicio_partida
        segundos = int(duracao.total_seconds())
        minutos = segundos // 60
        segundos = segundos % 60

        nova_partida = (
            f"{fim_partida.strftime('%d/%m/%Y %H:%M:%S')} | " 
            f"Campeão: {campeao} | " 
            f"{minutos:02}:{segundos:02}\n"
        )

        try:
            with open(CAMINHO_ARQ_HISTORICO, "r", encoding="utf-8") as arquivo:
                conteudo_antigo = arquivo.read()

        except FileNotFoundError:
            conteudo_antigo = ""

        with open(CAMINHO_ARQ_HISTORICO, "w", encoding="utf-8") as arquivo:
            arquivo.write(nova_partida)
            arquivo.write(conteudo_antigo)
        pygame.quit()