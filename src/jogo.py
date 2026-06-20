import pygame
from src.config import (LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO)
from src.funcoes import ( desenhar_barra_vida, desenhar_barra_ultimate, desenhar_elementos_tela, verificar_ataque, verificar_chute, verificar_especial, limitar_valor)
from src.telas import (tela_inicio, tela_pause, tela_fim, tela_historico)
from src.sons import sons
from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.dados import atualizar_historico
from datetime import datetime

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA)) 
elementos_tela = desenhar_elementos_tela()

def executar_jogo():

    pygame.init()
    pygame.display.set_caption(TITULO_JOGO)
    pygame.mixer.init()

    relogio = pygame.time.Clock()

    while True:
        # Processa a ação escolhida no menu inicial (sair, ver histórico ou iniciar a partida)
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
        
        # Inicio da trilha sonora de combate ao iniciar a partida
        pygame.mixer.music.load("assets/sons/Combate.wav")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1) # -1 faz a trilha sonora repetir indefinidamente

        # Cria os personagens, ajusta a direção inicial do segundo jogador e os adiciona ao grupo de sprites
        todas_sprites = pygame.sprite.Group()
        personagem1 = Personagem(100, personagem1_sprites)
        personagem2 = Personagem(1100, personagem2_sprites)
        personagem2.direcao = -1 # Personagem 2 começa virado para a esquerda
        todas_sprites.add(personagem1)
        todas_sprites.add(personagem2)

        
        rodando = True
        vencedor = False
        velocidade = 4
        correndo_p1 = False       
        correndo_p2 = False        

        inicio_partida = datetime.now()
        inicio_luta = pygame.time.get_ticks() # Define o início do tempo de luta quando as animações são carregadas
        tempo_luta = 120 # Define o tempo de luta em segundos
        tempo_pausado = 0 # Acumula o tempo total que o jogo ficou pausado para descontar do cronômetro
        fonte_time = pygame.font.Font("assets/fontes/PressStart2P-Regular.ttf", 16) # Define o estilo da fonte do cronômetro
        mensagem_fim = ""
        voltar_menu = False

        # Loop principal: processa entrada, atualiza estado e renderiza a cena.
        while rodando:

            tempo_atual = pygame.time.get_ticks() # Define o tempo atual o mesmo do início da luta
            tempo_restante = tempo_luta - ((tempo_atual - inicio_luta - tempo_pausado) / 1000) # Defino o tempo_restante como o tempo de luta menos o tempo percorrido
            tempo_restante = max(0, tempo_restante) # Define o máximo do tempo restante (que só vai até 0)

            #Trecho de código que formata o tempo para minutos e segundos
            segundos = int(tempo_restante)
            minutos = segundos // 60
            segundos = segundos % 60
            tempo_formatado = f"{minutos:02}:{segundos:02}"

            #Condição que define que se o tempo restante for menor ou igual a 0, o loop principal se encerra
            if tempo_restante <= 0:
                # Ao fim do tempo, vence quem tiver mais vida ou empate se as vidas estão iguais
                if personagem1.vida > personagem2.vida:
                    mensagem_fim = "Jogador 1"
                elif personagem2.vida > personagem1.vida:
                    mensagem_fim = "Jogador 2"
                else:
                    mensagem_fim = "Empate!"
                rodando = False
                
            verificar_ataque(personagem1, personagem2, 1, sons["ataques"], sons["defesas"][0]) 
            verificar_ataque(personagem2, personagem1, 2, sons["socos"], sons["defesas"][0])
            verificar_chute(personagem1, personagem2, 1, sons["chutes"], sons["defesas"][0])
            verificar_chute(personagem2, personagem1, 2, sons["chutes"], sons["defesas"][0])
            verificar_especial(personagem1, personagem2, 1, sons["especiais"], sons["defesas"][0])
            verificar_especial(personagem2, personagem1, 2, sons["especiais"], sons["defesas"][0])

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    return

                # Ataques dos personagens e menu de pause
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        tempo_antes_pause = pygame.time.get_ticks()
                        resultado = tela_pause(tela)
                        if resultado == "exit":
                            pygame.quit()
                            return
                        if resultado == "menu":
                            pygame.mixer.music.stop()
                            voltar_menu = True
                            rodando = False
                            mensagem_fim = ""
                            break
                        if resultado == "continuar":
                            # Registra quanto tempo o jogo ficou pausado para manter o cronômetro correto
                            tempo_pausado += pygame.time.get_ticks() - tempo_antes_pause
                    
                    # Controles do jogador 1: W ataca, S chuta, E usa especial
                    if evento.key == pygame.K_w:
                        personagem1.atacar()
                    if evento.key == pygame.K_s:
                        personagem1.chutar()
                    if evento.key == pygame.K_e:
                        personagem1.atacar_especial()

                    # Controles do jogador 2: seta cima ataca, seta baixo chuta, Enter usa especial
                    if evento.key == pygame.K_UP:
                        personagem2.atacar()
                        
                    if evento.key == pygame.K_DOWN:
                        personagem2.chutar()

                    if evento.key == pygame.K_RETURN:
                        personagem2.atacar_especial()               

            teclas = pygame.key.get_pressed()
            personagem1.estado = "idle"
            personagem2.estado = "idle"

            # Shift mantido bloqueia dano enquanto a tecla estiver pressionada
            if teclas[pygame.K_LSHIFT]:      
                personagem1.defendendo = True
            else:
                personagem1.defendendo = False
            if teclas[pygame.K_RSHIFT]:
                personagem2.defendendo = True
            else:
                personagem2.defendendo = False

            if teclas[pygame.K_LEFT]:
                personagem2.rect.x -= velocidade
                personagem2.estado = "corrida"
                personagem2.direcao = -1
            if teclas[pygame.K_RIGHT]:
                personagem2.rect.x += velocidade
                personagem2.estado = "corrida"
                personagem2.direcao = 1
            if teclas[pygame.K_a]:
                personagem1.rect.x -= velocidade
                personagem1.estado = "corrida"
                personagem1.direcao = -1
            if teclas[pygame.K_d]:
                personagem1.rect.x += velocidade
                personagem1.estado = "corrida"
                personagem1.direcao = 1

            p1_correndo_agora = personagem1.estado == "corrida"
            p2_correndo_agora = personagem2.estado == "corrida"

            # Inicia o som de corrida quando qualquer jogador começa a se mover
            if (p1_correndo_agora or p2_correndo_agora) and not (correndo_p1 or correndo_p2):
                sons["corridas"][0].play(loops=-1)

            # Para o som de corrida somente quando os dois jogadores param
            if not p1_correndo_agora and not p2_correndo_agora and (correndo_p1 or correndo_p2):
                sons["corridas"][0].stop()
            
            correndo_p1 = p1_correndo_agora
            correndo_p2 = p2_correndo_agora

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
            
            # Desenha os elementos visuais na tela
            tela.blit(elementos_tela["cenario"], (0, 0))
            tela.blit(elementos_tela["avatar1"], (80, 20))
            tela.blit(elementos_tela["avatar2"], (1235, 20))
            tela.blit(elementos_tela["moldura_tempo"], elementos_tela["rect_moldura_tempo"])
            tela.blit(elementos_tela["moldura_vida"], (170, 40))
            tela.blit(elementos_tela["moldura_vida2"], (985, 40))
            tela.blit(elementos_tela["moldura_ultimate"], (170, 80))
            tela.blit(elementos_tela["moldura_ultimate2"], (985, 80))

            # Desenha a barra de vida e de ultimate e vai atualizando enquanto o jogo roda
            desenhar_barra_vida(tela, 218, 48, personagem1.vida, personagem1.vida_maxima)
            desenhar_barra_ultimate(tela, 217, 88, personagem1.ultimate, personagem1.ultimate_maximo)

            desenhar_barra_vida(tela, 1010, 48, personagem2.vida, personagem2.vida_maxima)
            desenhar_barra_ultimate(tela, 1009, 88, personagem2.ultimate, personagem2.ultimate_maximo)

            #Renderiza o tempo formatado na tela
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

            #Coloca o tempo na tela do jogo
            texto_rect = texto.get_rect(center=(LARGURA_TELA // 2, 57))
            tela.blit(texto, texto_rect)

            todas_sprites.update()
            for sprite in todas_sprites:
                sprite.draw(tela)

            pygame.display.flip()
            relogio.tick(FPS)
        if voltar_menu:
            continue
        pygame.mixer.music.stop()
        resultado = tela_fim(tela, mensagem_fim)
        if resultado == "exit":
            pygame.quit()
            return

        # Determina o campeão final considerando derrota ou vantagem de vida ao fim do tempo
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
