import pygame
from src.config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, CAMINHO_CENARIO, CAMINHO_ARQ_HISTORICO)
from src.funcoes import ( desenhar_barra_vida, desenhar_barra_ultimate, verificar_ataque, verificar_chute, verificar_especial, limitar_valor)
from src.telas import (tela_inicio, tela_pause, tela_fim, tela_historico)
from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.dados import atualizar_historico
from datetime import datetime

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    pygame.display.set_caption(TITULO_JOGO)

    cenario = pygame.image.load(CAMINHO_CENARIO).convert()
    cenario = pygame.transform.scale(cenario, (1400, 600))
    avatar1 = pygame.image.load("assets/imagens/tela/avatar1.png").convert_alpha()
    avatar2 = pygame.image.load("assets/imagens/tela/avatar2.png").convert_alpha()
    avatar1 = pygame.transform.smoothscale(avatar1, (90, 120))
    avatar2 = pygame.transform.smoothscale(avatar2, (90, 120))
    moldura_tempo = pygame.image.load("assets/imagens/tela/moldura_tempo.png").convert_alpha()
    moldura_tempo = pygame.transform.smoothscale(moldura_tempo, (300, 77))
    moldura_vida = pygame.image.load("assets/imagens/tela/moldura_vida.png").convert_alpha()
    moldura_vida = pygame.transform.smoothscale(moldura_vida, (250, 37))
    moldura_vida2 = pygame.transform.flip(moldura_vida, True, False)
    moldura_ultimate = pygame.image.load("assets/imagens/tela/moldura_ultimate.png").convert_alpha()
    moldura_ultimate = pygame.transform.smoothscale(moldura_ultimate, (250, 37))
    moldura_ultimate2 = pygame.transform.flip(moldura_ultimate, True, False)
    rect_moldura_tempo = moldura_tempo.get_rect(center=(LARGURA_TELA//2, 55))

    relogio = pygame.time.Clock()

    while True:
        acao = tela_inicio(tela)

        if acao == "exit":
            pygame.quit()
            return
        
        if acao == "historico":
            resultado = tela_historico(tela)
            if resultado == "exit":
                pygame.quit()
                return
            continue

        if acao != "start":
            continue

        todas_sprites = pygame.sprite.Group()
        personagem1 = Personagem(100, personagem1_sprites)
        personagem2 = Personagem(1100, personagem2_sprites)
        personagem2.direcao = -1
        todas_sprites.add(personagem1)
        todas_sprites.add(personagem2)

        
        rodando = True
        vencedor = False
        velocidade = 4

        inicio_partida = datetime.now()
        inicio_luta = pygame.time.get_ticks() # Define o início do tempo de luta quando as animações são carregadas
        tempo_luta = 120 # Define o tempo de luta em segundos
        tempo_pausado = 0
        fonte_time = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 16) # Define o estilo da fonte do cronômetro
        mensagem_fim = ""
        voltar_menu = False

        # Loop principal: processa entrada, atualiza estado e renderiza a cena.
        while rodando:

            tempo_atual = pygame.time.get_ticks() # Define o tempo atual o mesmo do início da luta
            tempo_restante = tempo_luta - ((tempo_atual - inicio_luta - tempo_pausado) / 1000) # Defino o tempo_restante como o tempo de luta menos o tempo percorrido
            tempo_restante = max(0, tempo_restante) # Define o máximo do tempo restante (que só vai até 0)

            """ Trecho de código que formata o tempo para minutos e segundos """
            segundos = int(tempo_restante)
            minutos = segundos // 60
            segundos = segundos % 60
            tempo_formatado = f"{minutos:02}:{segundos:02}"

            """ Condição que define que se o tempo restante for menor ou igual a 0, o loop principal se encerra """
            if tempo_restante <= 0:
                if personagem1.vida > personagem2.vida:
                    mensagem_fim = "Jogador 1"
                elif personagem2.vida > personagem1.vida:
                    mensagem_fim = "Jogador 2"
                else:
                    mensagem_fim = "Empate!"
                rodando = False
                
            verificar_ataque(personagem1, personagem2, 1) 
            verificar_ataque(personagem2, personagem1, 2)
            verificar_chute(personagem1, personagem2, 1)
            verificar_chute(personagem2, personagem1, 2)
            verificar_especial(personagem1, personagem2, 1)
            verificar_especial(personagem2, personagem1, 2)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                # Ataques dos personagens
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        tempo_antes_pause = pygame.time.get_ticks()
                        resultado = tela_pause(tela)
                        if resultado == "exit":
                            pygame.quit()
                            return
                        if resultado == "menu":
                            voltar_menu = True
                            rodando = False
                            mensagem_fim = ""
                            break
                        if resultado == "continuar":
                            tempo_pausado += pygame.time.get_ticks() - tempo_antes_pause
                    if evento.key == pygame.K_w:
                        personagem1.atacar()
                    if evento.key == pygame.K_s:
                        personagem1.chutar()
                    if evento.key == pygame.K_e:
                        personagem1.atacar_especial()
                    if evento.key == pygame.K_UP:
                        personagem2.atacar()
                    if evento.key == pygame.K_DOWN:
                        personagem2.chutar()
                    if evento.key == pygame.K_RETURN:
                        personagem2.atacar_especial()               

            teclas = pygame.key.get_pressed()
            personagem1.estado = "idle"
            personagem2.estado = "idle"
            # Movimentação alterando direto o eixo X do retângulo do jogador
            if teclas[pygame.K_LSHIFT]:      
                personagem1.defendendo = True
            else:
                personagem1.defendendo = False
            if teclas[pygame.K_KP0]:
                personagem2.defendendo = True
            else:
                personagem2.defendendo = False
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
            personagem2.rect.x = limitar_valor(personagem2.rect.x, 0, LARGURA_TELA - personagem2.rect.width)

            # Se alguum dos personagens atingir 0 de pontos de vida, o jogo acaba
            if personagem1.vida <= 0:
                mensagem_fim = "Jogador 2"
                vencedor = True
                rodando = False

            elif personagem2.vida <= 0:
                mensagem_fim = "Jogador 1"
                vencedor = True
                rodando = False

            tela.blit(cenario, (0, 0))
            tela.blit(moldura_tempo, rect_moldura_tempo)
            tela.blit(moldura_vida, (170,40))
            tela.blit(moldura_ultimate, (170,80))
            tela.blit(moldura_vida2, (985,40))
            tela.blit(moldura_ultimate2, (985,80))
            # Jogador 1
            tela.blit(avatar1, (80, 20))
            # Jogador 2
            tela.blit(avatar2, (1235, 20))

            # Desenha a barra de vida e de ultimate e vai atualizando enquanto o jogo roda
            desenhar_barra_vida(tela, 218, 48, personagem1.vida, personagem1.vida_maxima)
            desenhar_barra_ultimate(tela, 217, 88, personagem1.ultimate, personagem1.ultimate_maximo)

            desenhar_barra_vida(tela, 1010, 48, personagem2.vida, personagem2.vida_maxima)
            desenhar_barra_ultimate(tela, 1009, 88, personagem2.ultimate, personagem2.ultimate_maximo)

            """ Renderiza o tempo formatado na tela """
            if tempo_restante > 10:
                texto = fonte_time.render(
                    tempo_formatado,
                    True,
                    (255, 255, 255)
                )
            else:
                texto = fonte_time.render(
                    tempo_formatado,
                    True,
                    (255, 0, 0) # Define que a partir dos 10 segundos finais, a cor do tempo é alterada para vermelho
                )

            """ Coloca o tempo na tela do jogo """
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 57))
            tela.blit(texto, texto_rect)

            todas_sprites.update()
            for sprite in todas_sprites:
                sprite.draw(tela)

            pygame.display.flip()
            relogio.tick(FPS)
        if voltar_menu:
            continue
        resultado = tela_fim(tela, mensagem_fim)
        if resultado == "exit":
            pygame.quit()
            return

        if personagem1.vida <= 0:
            campeao = "Jogador 2"
        elif personagem2.vida <= 0:
            campeao = "Jogador 1"
        elif personagem1.vida > personagem2.vida:
            campeao = "Jogador 1"
        elif personagem2.vida > personagem1.vida:
            campeao = "Jogador 2"
        else:
            campeao = "Empate"

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

        atualizar_historico(nova_partida)