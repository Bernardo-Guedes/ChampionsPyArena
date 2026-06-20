import pygame
import random

def desenhar_barra_vida(tela, x, y, vida, vida_maxima):
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
    largura_total = 178
    altura = 20
    porcentagem = ultimate / ultimate_maximo
    largura_atual = largura_total * porcentagem

    pygame.draw.rect(
        tela,
        (0, 0, 255),
        (x, y, largura_atual, altura)
    )

def verificar_ataque(atacante, defensor, personagem, sons=None, som_defesa = None):
    if not atacante.atacando: # Se o atacante não realiza o ataque a função não é realizada
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

def verificar_chute(atacante, defensor, personagem, sons =None, som_defesa = None):
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
    y = 255
    for partida in partidas:
        campeao, data, duracao = partida.split("|")
        tela.blit(fonte.render(campeao, True, (255, 255, 255)),(300, y))
        tela.blit(fonte.render(data, True, (255, 255, 255)),(600, y))
        tela.blit(fonte.render(duracao, True, (255, 255, 255)),(1000, y))
        y += 50

def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor

def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)