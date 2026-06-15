import pygame
from src.config import (
    ALTURA_TELA,
    CAMINHO_IDLE_1,
    CAMINHO_IDLE_2,
    CAMINHO_ATTACK_1,
    CAMINHO_ATTACK_2,
    CAMINHO_CHUTE_1,
    CAMINHO_CHUTE_2,
    CAMINHO_RUN_1,
    CAMINHO_RUN_2,
    CAMINHO_ESPECIAL_1,
    CAMINHO_ESPECIAL_2,
    FRAMES_IDLE_1,
    FRAMES_IDLE_2,
    FRAMES_ATTACK_1,
    FRAMES_ATTACK_2,
    FRAMES_CHUTE_1,
    FRAMES_CHUTE_2,
    FRAMES_RUN_1,
    FRAMES_RUN_2,
    FRAMES_ESPECIAL_1, 
    FRAMES_ESPECIAL_2 

)
from src.sprites import ( carregar_animacao )

personagem1_sprites = {
    "idle": (CAMINHO_IDLE_1, FRAMES_IDLE_1, 0.2),
    "attack": (CAMINHO_ATTACK_1, FRAMES_ATTACK_1, 0.5),
    "chute": (CAMINHO_CHUTE_1, FRAMES_CHUTE_1, 0.5),
    "run": (CAMINHO_RUN_1, FRAMES_RUN_1, 0.4),
    "especial": (CAMINHO_ESPECIAL_1, FRAMES_ESPECIAL_1, 0.4),
}

personagem2_sprites = {
    "idle": (CAMINHO_IDLE_2, FRAMES_IDLE_2, 0.16),
    "attack": (CAMINHO_ATTACK_2, FRAMES_ATTACK_2, 0.3),
    "chute": (CAMINHO_CHUTE_2, FRAMES_CHUTE_2, 0.5),
    "run": (CAMINHO_RUN_2, FRAMES_RUN_2, 0.4),
    "especial": (CAMINHO_ESPECIAL_2, FRAMES_ESPECIAL_2, 0.4),
}

class Personagem(pygame.sprite.Sprite):
    def __init__(self, rect_x, sprite_config):
        super().__init__()
        self.som_ataque = pygame.mixer.Sound("assets/sons/ataque1.wav") #Necessário para que cada personagem guarde o som de ataque.
        self.animacoes = {
            nome: carregar_animacao(caminho, frames, speed)
            for nome, (caminho, frames, speed) in sprite_config.items()
        }
        self.animacoes_inverso = {
            nome: [
                pygame.transform.flip(sprite, True, False)
                for sprite in frames
            ]
            for nome, frames in self.animacoes.items()
        }
        self.estado = "idle"
        self.atacando = False
        self.frame = 0
        self.direcao = 1
        self.rect = pygame.Rect(0, 0, 222, 180)
        self.rect.topleft = (rect_x, ALTURA_TELA-300)
        self.vida_maxima = 100
        self.vida = self.vida_maxima
        self.dano = 5
        self.ultimate = 0
        self.ultimate_maximo = 100
        self.acertou_ataque = False

    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.acertou_ataque = False
            self.frame = 0

            self.som_ataque.play() #Som de ataque.

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def carregar_ultimate(self, progresso_ultimate):
        self.ultimate += progresso_ultimate
        if self.ultimate > self.ultimate_maximo:
            self.ultimate = self.ultimate_maximo

    def update(self):
        if self.atacando:
            self.frame += 0.15
            if self.frame >= len(self.animacoes["attack"]):
                self.frame = 0
                self.atacando = False
        else:
            velocidade_animacao = {
                "idle": 0.1,
                "run": 0.2
            }
            self.frame += velocidade_animacao[self.estado]
            if self.frame >= len(self.animacoes[self.estado]):
                self.frame = 0

    def draw(self, surface):
        indice = int(self.frame)
        if self.atacando:
            animacao = "attack"
        else:
            animacao = self.estado
        if self.direcao == 1:
            imagem = self.animacoes[animacao][indice]
        else:
            imagem = self.animacoes_inverso[animacao][indice]
        img_rect = imagem.get_rect(center=self.rect.center)
        surface.blit(imagem, img_rect)