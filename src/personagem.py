import pygame
from src.config import (
    ALTURA_TELA,
    CAMINHO_SPRITE_IDLE,
    CAMINHO_SPRITE_ATTACK,
    CAMINHO_SPRITE_RUN,
    FRAMES_IDLE,
    FRAMES_ATTACK,
    FRAMES_RUN
)
from src.sprites import ( carregar_animacao )

class Personagem(pygame.sprite.Sprite):
    def __init__(self, rect_x):
        super().__init__()
        self.animacoes = {
            "idle": carregar_animacao(CAMINHO_SPRITE_IDLE, FRAMES_IDLE),
            "attack": carregar_animacao(CAMINHO_SPRITE_ATTACK, FRAMES_ATTACK),
            "run": carregar_animacao(CAMINHO_SPRITE_RUN, FRAMES_RUN)
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
        self.acertou_ataque = False

    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.acertou_ataque = False
            self.frame = 0

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

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