import pygame
import random
from src.config import ELEMENTOS_TELA_PRINCIPAL_CONFIG, ELEMENTOS_TELAS_SEC_CONFIG, LARGURA_TELA

def desenhar_barra_vida(tela, x, y, vida, vida_maxima):
    """
    Desenha a barra de vida do personagem na tela.

    Parâmetros:
        tela (pygame.Surface): Superfície onde a barra será desenhada.
        x (int): Posição horizontal da barra.
        y (int): Posição vertical da barra.
        ultimate (int): Valor atual da vida do personagem.
        ultimate_maximo (int): Valor máximo da vida do personagem.

    Retorna:
        Desenha/atualiza visualmente a barra de vida de acordo com a porcentagem preenchida com base no valor máximo.
    """
    largura_total = 178
    altura = 20
    porcentagem = vida / vida_maxima
    largura_atual = largura_total * porcentagem

    pygame.draw.rect(
        tela,
        (0, 255, 0),
        (x, y, largura_atual, altura)
    )

def desenhar_barra_ultimate(tela, x, y, ultimate, ultimate_maximo):
    """
    Desenha a barra de ultimate do personagem na tela.

    Parâmetros:
        tela (pygame.Surface): Superfície onde a barra será desenhada.
        x (int): Posição horizontal da barra.
        y (int): Posição vertical da barra.
        ultimate (int): Valor atual da ultimate do personagem.
        ultimate_maximo (int): Valor máximo da ultimate do personagem.

    Retorna:
        Desenha/atualiza visualmente a barra de ultimate de acordo com a porcentagem preenchida com base no valor máximo.
    """
    largura_total = 178
    altura = 20
    porcentagem = ultimate / ultimate_maximo
    largura_atual = largura_total * porcentagem

    pygame.draw.rect(
        tela,
        (0, 0, 255),
        (x, y, largura_atual, altura)
    )

def desenhar_elementos_tela():
    """
    Carrega, configura e armazena os elementos gráficos da tela principal.

    Parâmetros:
        Nenhum parâmetro

    Retorna:
        dict: Dicionário contendo as imagens carregadas, redimensionadas e os elementos auxiliares da interface, como molduras e retângulos.
    """
    elementos = {}

    for nome, config in ELEMENTOS_TELA_PRINCIPAL_CONFIG.items():
        elemento = pygame.image.load(config["caminho"])
        if config["convert_alpha"]:
            elemento = elemento.convert_alpha()
        else:
            elemento = elemento.convert()

        if "scale" in config:
            elemento = pygame.transform.smoothscale(elemento, config["scale"])

        elementos[nome] = elemento

    elementos["moldura_vida2"] = pygame.transform.flip(elementos["moldura_vida"], True, False)
    elementos["moldura_ultimate2"] = pygame.transform.flip(elementos["moldura_ultimate"], True, False)
    elementos["rect_moldura_tempo"] = elementos["moldura_tempo"].get_rect(center=(LARGURA_TELA // 2, 55))

    return elementos


def desenhar_elementos_telas_sec():
    """
    Carrega, configura e armazena os elementos gráficos das telas secundárias.

    Parâmetros:
        Nenhum parâmetro

    Retorna:
        dict: Dicionário contendo as imagens carregadas e configuradas para utilização nas telas secundárias do jogo.
    """
    elementos = {}

    for nome, config in ELEMENTOS_TELAS_SEC_CONFIG.items():
        elemento = pygame.image.load(config["caminho"])
        if config["convert_alpha"]:
            elemento = elemento.convert_alpha()
        else:
            elemento = elemento.convert()

        if "scale" in config:
            elemento = pygame.transform.smoothscale(elemento, config["scale"])

        elementos[nome] = elemento
    return elementos


def verificar_ataque(atacante, defensor, personagem, sons=None, som_defesa = None):
    """
    Verifica se um ataque atingiu o defensor e aplica seus efeitos.

    Parâmetros:
        atacante (Personagem): Personagem que está realizando o ataque.
        defensor (Personagem): Personagem que pode receber o dano.
        personagem (int): Identificação do personagem utilizado para determinar em qual frame o golpe deve atingir.
        sons (pygame.mixer.Sound, opcional): Som reproduzido quando o ataque acerta.
        som_defesa (pygame.mixer.Sound, opcional): Som reproduzido quando o ataque é defendido.

    Retorno:
        A função verifica a colisão do ataque e, quando bem sucedido, aplica dano ao defensor, aumenta a barra de ultimate do atacante e reproduz os efeitos sonoros.     
    """
    if not atacante.atacando:
        return
        
    if personagem == 1 and int(atacante.frame) != 4:
        return
    if personagem == 2 and int(atacante.frame) != 2:
        return

    if atacante.direcao == 1: # Se o atacante estiver olhando para direita
        hitbox_ataque = pygame.Rect( # Define a hitbox de ataque
            atacante.rect.right, 
            atacante.rect.y + 30, # A hitbox é posicionada a frente, para verificar se é o golpe que pega no adversário
            70, # Largura
            60 # Altura
        )
    else: # caso o atacante esteja olhando pra esquerda
        hitbox_ataque = pygame.Rect( 
            atacante.rect.left - 70,
            atacante.rect.y + 30,
            70,
            60
        )

    # Se o programa detecta a colisão da hitbox com o adversário e o ataque acertado está False
    if (hitbox_ataque.colliderect(defensor.rect) and not atacante.acertou_ataque):
        dano_aplicado = defensor.receber_dano(atacante.dano) # Define o dano para o defensor
        if dano_aplicado:
            atacante.carregar_ultimate(10) # Define o aumento do ultimate para o atacante
            if sons:
                random.choice(sons).play()
        elif som_defesa:
            som_defesa.play()
        atacante.acertou_ataque = True

def verificar_chute(atacante, defensor, personagem, sons = None, som_defesa = None):
    """
    Verifica se o chute atingiu o defensor e aplica seus efeitos.

    Parâmetros:
        atacante (Personagem): Personagem que está realizando o chute.
        defensor (Personagem): Personagem que pode receber o dano.
        personagem (int): Identificação do personagem utilizado para determinar em qual frame o chute deve atingir.
        sons (pygame.mixer.Sound, opcional): Som reproduzido quando o chute acerta.
        som_defesa (pygame.mixer.Sound, opcional): Som reproduzido quando o chute é defendido.

    Retorna:
        A função verifica a colisão do chute e, quando bem sucedido, aplica dano ao defensor, aumenta a barra de ultimate do atacante e reproduz os efeitos sonoros.
    """

    if not atacante.chutando:
        return
    
    if personagem == 1 and int(atacante.frame) != 4:
        return
    if personagem == 2 and int(atacante.frame) != 2:
        return
 
    if atacante.direcao == 1:
        hitbox_ataque = pygame.Rect(
            atacante.rect.right, 
            atacante.rect.y + 30, 
            70, 
            60)
    else:
        hitbox_ataque = pygame.Rect(
            atacante.rect.left - 70, 
            atacante.rect.y + 30, 
            70, 
            60)
 
    if hitbox_ataque.colliderect(defensor.rect) and not atacante.acertou_chute:
        dano_aplicado = defensor.receber_dano(atacante.dano_chute)
        if dano_aplicado:
            atacante.carregar_ultimate(10)
            if sons:
                random.choice(sons).play()
        elif som_defesa:
            som_defesa.play()
        atacante.acertou_chute = True
        

def verificar_especial(atacante, defensor, personagem, sons = None, som_defesa = None):
    """
    Verifica se o ataque especial atingiu o defensor e aplica seus efeitos.

    Parâmetros:
        atacante (Personagem): Personagem que está realizando o ataque especial.
        defensor (Personagem): Personagem que pode receber o dano.
        personagem (int): Identificação do personagem utilizado para determinar em qual frame o ataque especial deve atingir.
        sons (pygame.mixer.Sound, opcional): Som reproduzido quando o ataque especial acerta.
        som_defesa (pygame.mixer.Sound, opcional): Som reproduzido quando o ataque especial é defendido.

    Retorna:
        A função verifica a colisão do ultimate e, quando bem sucedido, aplica dano ao defensor, aumenta a barra de ultimate do atacante e reproduz os efeitos sonoros.
    """
    if not atacante.usando_ultimate:
        return

    if personagem == 1 and int(atacante.frame) != 2:
        return
    if personagem == 2 and int(atacante.frame) != 1:
        return

    if atacante.direcao == 1:
        hitbox_ataque = pygame.Rect(
            atacante.rect.right,
            atacante.rect.y + 50,
            70,   
            60
        )
    else:
        hitbox_ataque = pygame.Rect(
            atacante.rect.left - 70,
            atacante.rect.y + 40,
            70,
            60
        )
    if hitbox_ataque.colliderect(defensor.rect) and not atacante.acertou_ultimate:
        dano_aplicado = defensor.receber_dano_ultimate(atacante.dano_ultimate)
        atacante.acertou_ultimate = True
        if dano_aplicado:
            if sons:
                random.choice(sons).play()
        elif som_defesa:
            som_defesa.play()


def desenhar_historico(tela, partidas, fonte):
    """
    Desenha o histórico das partidas na tela.

    Parâmetros:
        tela (pygame.Surface): Superfície onde o histórico será desenhado.
        partidas (list): lista contendo o registro das partidas na tela.
        fonte (pygame.font.Font): Fonte utilizada para renderizar os textos.

    Retorna:
        Exibe na tela o campeão, a data e a duração de cada partida registrada no histórico.
    """
    y = 255
    for partida in partidas:
        campeao, data, duracao = partida.split("|")
        tela.blit(fonte.render(campeao, True, (255, 255, 255)),(300, y))
        tela.blit(fonte.render(data, True, (255, 255, 255)),(600, y))
        tela.blit(fonte.render(duracao, True, (255, 255, 255)),(1000, y))
        y += 50

def limitar_valor(valor, minimo, maximo):
    """
    Limita um valor entre um mínimo e um máximo.

    Parâmetros:
        valor (int): Valor que será verificado.
        minimo (int): Menor valor permitido.
        maximo (int): Maior valor permitido.

    Retorna:
        int: O valor ajustado dentro dos limites especificados. Retorna o mínimo se o valor for menor que o limite inferior, o máximo se o valor exceder o limite superior, ou o próprio valor caso esteja dentro dos limites.
    """
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor

def verificar_colisao(retangulo_1, retangulo_2):
    """
    Verifica se há colisão entre dois retângulos.

    Parâmetros:
        retangulo_1 (pygame.Rect): 1° retângulo a ser verificado.
        retangulo_2 (pygame.Rect): 2° retângulo a ser verificado.

    Retorna:
        True se os retângulos estiverem colidindo e False caso contrário.
    """
    return retangulo_1.colliderect(retangulo_2)