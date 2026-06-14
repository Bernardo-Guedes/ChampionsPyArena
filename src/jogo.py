import pygame
from src.config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO, CAMINHO_CENARIO, CAMINHO_ARQ_HISTORICO)
from src.funcoes import ( desenhar_barra_vida, desenhar_barra_ultimate, verificar_ataque, limitar_valor)
from src.telas import (tela_inicio, tela_fim, tela_historico)
from src.personagem import Personagem
from datetime import datetime

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    pygame.display.set_caption(TITULO_JOGO)

    cenario = pygame.image.load(CAMINHO_CENARIO).convert()
    cenario = pygame.transform.scale(cenario, (1400, 600))

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
        personagem1 = Personagem(100)
        personagem2 = Personagem(1100)
        personagem2.direcao = -1
        todas_sprites.add(personagem1)
        todas_sprites.add(personagem2)

        
        rodando = True
        vencedor = False
        velocidade = 5

        inicio_partida = datetime.now()
        inicio_luta = pygame.time.get_ticks() # Define o início do tempo de luta quando as animações são carregadas
        tempo_luta = 20 # Define o tempo de luta em segundos
        fonte = pygame.font.SysFont("Arial", 40, True) # Define o estilo da fonte do cronômetro
        mensagem_fim = ""

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
                if personagem1.vida > personagem2.vida:
                    mensagem_fim = "Jogador 1 venceu!"
                elif personagem2.vida > personagem1.vida:
                    mensagem_fim = "Jogador 2 venceu!"
                else:
                    mensagem_fim = "Empate!"
                rodando = False
                
            verificar_ataque(personagem1, personagem2) 
            verificar_ataque(personagem2, personagem1)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                # Ataques dos personagens
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_w:
                        personagem1.atacar()
                    if evento.key == pygame.K_UP:
                        personagem2.atacar()                

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
            personagem2.rect.x = limitar_valor(personagem2.rect.x, 0, LARGURA_TELA - personagem2.rect.width)

            # Se alguum dos personagens atingir 0 de pontos de vida, o jogo acaba
            if personagem1.vida <= 0:
                mensagem_fim = "Jogador 2 venceu!"
                vencedor = True
                rodando = False

            elif personagem2.vida <= 0:
                mensagem_fim = "Jogador 1 venceu!"
                vencedor = True
                rodando = False

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
            relogio.tick(FPS)

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

        try:
            with open(CAMINHO_ARQ_HISTORICO, "r", encoding="utf-8") as arquivo:
                conteudo_antigo = arquivo.read()

        except FileNotFoundError:
            conteudo_antigo = ""

        with open(CAMINHO_ARQ_HISTORICO, "w", encoding="utf-8") as arquivo:
            arquivo.write(nova_partida)
            arquivo.write(conteudo_antigo)