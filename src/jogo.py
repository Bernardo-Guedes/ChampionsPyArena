import pygame
from src.config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, CINZA, PRETO)
from src.funcoes import ( desenhar_barra_vida, desenhar_barra_ultimate, verificar_ataque, limitar_valor )
from src.personagem import Personagem

def tela_inicio(tela):
    fonte_titulo = pygame.font.SysFont(None, 80)
    fonte_texto = pygame.font.SysFont(None, 40)
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False
            if evento.type == pygame.KEYDOWN:
                return True
        tela.fill((CINZA))
        titulo = fonte_titulo.render(TITULO_JOGO, True, (PRETO))
        texto = fonte_texto.render("Pressione qualquer tecla para começar", True, (PRETO))
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 200))
        tela.blit(texto, (LARGURA_TELA // 2 - texto.get_width() // 2, 350))
        pygame.display.flip()

    return True

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
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
    velocidade = 5

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
            
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

        tela.fill(CINZA)

        # Desenha a barra de vida e de ultimate e vai atualizando enquanto o jogo roda
        desenhar_barra_vida(tela, 90, 30, personagem1.vida, personagem1.vida_maxima)
        desenhar_barra_vida(tela, 1000, 30, personagem2.vida, personagem2.vida_maxima)
        desenhar_barra_ultimate(tela, 90, 60, personagem1.ultimate, personagem1.ultimate_maximo)
        desenhar_barra_ultimate(tela, 1000, 60, personagem2.ultimate, personagem2.ultimate_maximo)

        todas_sprites.update()
        for sprite in todas_sprites:
            sprite.draw(tela)
        pygame.display.flip()
    pygame.quit()