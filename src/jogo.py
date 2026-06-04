import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
    CAMINHO_SPRITE_1,
    CAMINHO_SPRITE_ATAQUE,
    CAMINHO_SPRITE_CORRIDA
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)
from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

class personagem(pygame.sprite.Sprite):
    def __init__(self, rect_x):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=59, y=107, width=105, height=87, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=303, y=104, width=105, height=90, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=547, y=104, width=105, height=90, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=793, y=107, width=105, height=87, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=1030, y=110, width=111, height=84, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=1279, y=113, width=105, height=81, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=1523, y=110, width=105, height=84, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=1767, y=110, width=105, height=84, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_1, x=2011, y=110, width=105, height=84, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=55, y=124, width=107, height=59, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=305, y=121, width=101, height=65, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=570, y=52, width=80, height=143, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=814, y=52, width=80, height=134, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=1049, y=52, width=86, height=131, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=1290, y=49, width=89, height=134, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=1534, y=52, width=89, height=131, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=1780, y=25, width=170, height=191, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_ATAQUE, x=2013, y=121, width=107, height=65, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=55, y=100, width=140, height=100, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=305, y=100, width=140, height=100, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=570, y=100, width=140, height=100, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=814, y=100, width=140, height=100, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=1049, y=100, width=140, height=100, scale=2))
        self.sprites.append(pegar_sprite(CAMINHO_SPRITE_CORRIDA, x=1290, y=100, width=140, height=100, scale=2))
        self.sprites_esquerda = [
            pygame.transform.flip(sprite, True, False)
            for sprite in self.sprites
        ]
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = pygame.Rect(0, 0, 222, 180)
        self.rect.topleft = (rect_x, ALTURA_TELA-300)
        self.ataque = False
        self.correndo = False
        self.direcao = 1

    def atacar(self):
        self.ataque = True
        self.atual = 10

    def update(self, inicio = 0):
        if self.ataque:
            self.atual +=0.15
            if self.atual >= 18:
                self.atual = 0
                self.ataque = False

        elif self.correndo:
            if self.atual < 19 or self.atual >=24:
                self.atual = 19
            self.atual += 0.15
            if self.atual >= 24:
                self.atual = 19

        else:
            self.atual += 0.1
            if self.atual >= 9:
                self.atual = 0

    def draw(self, surface):
        if self.direcao == 1:
            imagem = self.sprites[int(self.atual)]
        else:
            imagem = self.sprites_esquerda[int(self.atual)]
        img_rect = imagem.get_rect(center=self.rect.center)
        surface.blit(imagem, img_rect)

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    todas_sprites = pygame.sprite.Group()
    personagem1 = personagem(100)
    personagem2 = personagem(300)
    todas_sprites.add(personagem1)
    todas_sprites.add(personagem2)
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    rodando = True

    # 1. Carregando as imagens recortadas do Spritesheet


    # Jogador: usando tamanho 110x110 para capturar o quadrado perfeitamente
    #player_image = pegar_sprite(CAMINHO_SPRITE_1, x=59, y=107, width=105, height=87, scale=2)

    # Gema pequena: usando tamanho 64x64
    #gem_image    = pegar_sprite(CAMINHO_SPRITES, x=900, y=690, width=200, height=200, scale=0.5)

    # Morcego: usando tamanho 180x120 por causa das asas abertas
    #bat_image    = pegar_sprite(CAMINHO_SPRITES, x=905, y=1060, width=200, height=130, scale=0.0)
    
    # 2. Criando a estrutura de Sprites usando Dicionários
    """
    jogador = {
        "imagem": player_image,
        "rect": player_image.get_rect(topleft=(100, 100))
    }
    gema = {
        "imagem": gem_image,
        "rect": gem_image.get_rect(topleft=(500, 300))
    }
    
    inimigo = {
        "imagem": bat_image,
        "rect": bat_image.get_rect(topleft=(200, 500))
    }
    """
    velocidade = 5
    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)

    # Loop principal: processa entrada, atualiza estado e renderiza a cena.
    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    personagem1.atacar()
                if evento.key == pygame.K_DOWN:
                    personagem2.atacar()

        teclas = pygame.key.get_pressed()

        # Movimentação alterando direto os eixos X e Y do retângulo do jogador
        personagem1.correndo = False
        personagem2.correndo = False
        if teclas[pygame.K_LEFT]:
            personagem2.rect.x -= velocidade
            personagem2.correndo = True
            personagem2.direcao = -1
        if teclas[pygame.K_RIGHT]:
            personagem2.rect.x += velocidade
            personagem2.correndo = True
            personagem2.direcao = 1
        if teclas[pygame.K_a]:
            personagem1.rect.x -= velocidade
            personagem1.correndo = True
            personagem1.direcao = -1
        if teclas[pygame.K_d]:
            personagem1.rect.x += velocidade
            personagem1.correndo = True
            personagem1.direcao = 1

        # Limitando o jogador dentro das bordas da tela usando as propriedades do Rect
        #jogador["rect"].x = limitar_valor(jogador["rect"].x, 0, LARGURA_TELA - jogador["rect"].width)
        #jogador["rect"].y = limitar_valor(jogador["rect"].y, 0, ALTURA_TELA - jogador["rect"].height)

        """
        # Verificação de colisão com a Gema (antigo 'item')
        if verificar_colisao(jogador["rect"], gema["rect"]):
            pontos = calcular_pontos(pontos, 10)

            # Move a gema de lugar ao coletar
            gema["rect"].x += 80
            gema["rect"].y += 50

            # Se a gema sair da tela, volta para uma posição segura
            if gema["rect"].x > LARGURA_TELA - gema["rect"].width:
                gema["rect"].x = 50
            if gema["rect"].y > ALTURA_TELA - gema["rect"].height:
                gema["rect"].y = 50

        # Verificação de colisão com o Inimigo
        if verificar_colisao(jogador["rect"], inimigo["rect"]):
            vidas = tomar_dano(vidas, 1)

            # Afasta o inimigo ao colidir
            inimigo["rect"].x += 80
            inimigo["rect"].y += 50

            if inimigo["rect"].x > LARGURA_TELA - inimigo["rect"].width:
                inimigo["rect"].x = 50
            if inimigo["rect"].y > ALTURA_TELA - inimigo["rect"].height:
                inimigo["rect"].y = 50
        """
        # Regras de fim de jogo e recorde
        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {pontos} | Recorde: {recorde} | Vidas: {vidas}"
        )

        tela.fill(CINZA)

        # Desenhando os elementos na tela passando a imagem e o rect de cada dicionário
        """
        tela.blit(gema["imagem"], gema["rect"])
        tela.blit(inimigo["imagem"], inimigo["rect"])
        """
        #tela.blit(jogador["imagem"], jogador["rect"])
        todas_sprites.update()
        for sprite in todas_sprites:
            sprite.draw(tela)
        pygame.display.flip()

    pygame.quit()