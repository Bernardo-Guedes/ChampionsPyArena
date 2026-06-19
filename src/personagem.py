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
    CAMINHO_DEFESA_1,
    CAMINHO_DEFESA_2,
    FRAMES_IDLE_1,
    FRAMES_IDLE_2,
    FRAMES_ATTACK_1,
    FRAMES_ATTACK_2,
    FRAMES_CHUTE_1,
    FRAMES_CHUTE_2,
    FRAMES_RUN_1,
    FRAMES_RUN_2,
    FRAMES_ESPECIAL_1, 
    FRAMES_ESPECIAL_2,
    FRAMES_DEFESA_1,
    FRAMES_DEFESA_2

)
from src.sprites import ( carregar_animacao )

personagem1_sprites = {
    "idle": (CAMINHO_IDLE_1, FRAMES_IDLE_1, 0.2),
    "attack": (CAMINHO_ATTACK_1, FRAMES_ATTACK_1, 0.5),
    "chute": (CAMINHO_CHUTE_1, FRAMES_CHUTE_1, 0.5),
    "run": (CAMINHO_RUN_1, FRAMES_RUN_1, 0.4),
    "especial": (CAMINHO_ESPECIAL_1, FRAMES_ESPECIAL_1, 0.4),
    "defesa": (CAMINHO_DEFESA_1, FRAMES_DEFESA_1, 0.3)
}

personagem2_sprites = {
    "idle": (CAMINHO_IDLE_2, FRAMES_IDLE_2, 0.16),
    "attack": (CAMINHO_ATTACK_2, FRAMES_ATTACK_2, 0.3),
    "chute": (CAMINHO_CHUTE_2, FRAMES_CHUTE_2, 0.3),
    "run": (CAMINHO_RUN_2, FRAMES_RUN_2, 0.4),
    "especial": (CAMINHO_ESPECIAL_2, FRAMES_ESPECIAL_2, 0.3),
    "defesa": (CAMINHO_DEFESA_2, FRAMES_DEFESA_2, 0.18)
}

class Personagem(pygame.sprite.Sprite):
    def __init__(self, rect_x, sprite_config):
        super().__init__()
        self.animacoes = {
            nome: carregar_animacao(caminho, frames, scale)
            for nome, (caminho, frames, scale) in sprite_config.items()
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
        self.chutando = False
        self.defendendo = False
        self.frame = 0
        self.direcao = 1
        self.rect = pygame.Rect(0, 0, 50, 130)
        self.rect.topleft = (rect_x, ALTURA_TELA-300)
        self.vida_maxima = 100
        self.vida = self.vida_maxima
        self.dano = 5
        self.dano_chute = 5
        self.dano_ultimate = 20
        self.ultimate = 0
        self.ultimate_forcado = False
        self.ultimate_maximo = 100
        self.acertou_ataque = False
        self.acertou_chute = False
        self.usando_ultimate = False
        self.acertou_ultimate = False

    def atacar(self):
        if not self.atacando:
            self.atacando = True
            self.acertou_ataque = False
            self.frame = 0

    def chutar(self):
        if not self.chutando and not self.atacando and not self.usando_ultimate:
            self.chutando = True
            self.acertou_chute = False
            self.frame = 0

    def atacar_especial(self):
        if self.ultimate >= self.ultimate_maximo and not self.atacando and not self.usando_ultimate:
            self.usando_ultimate = True
            self.acertou_ultimate = False
            self.frame = 0
            self.ultimate = 0

    def receber_dano(self, dano):
        if self.defendendo:
            return False
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        if self.vida <= self.vida_maxima * 0.2 and not self.ultimate_forcado:
            self.ultimate = self.ultimate_maximo
            self.ultimate_forcado = True
        return True

    def receber_dano_ultimate(self, dano_ultimate):
        if self.defendendo:
            return False
        self.vida -= dano_ultimate
        if self.vida < 0:
            self.vida = 0
        if self.vida <= self.vida_maxima * 0.2 and not self.ultimate_forcado:
            self.ultimate = self.ultimate_maximo
            self.ultimate_forcado = True
        return True

    def carregar_ultimate(self, progresso_ultimate):
        self.ultimate += progresso_ultimate
        if self.ultimate > self.ultimate_maximo:
            self.ultimate = self.ultimate_maximo

    def update(self):
        if self.usando_ultimate:
            self.frame += 0.08
            if self.frame >= len(self.animacoes["especial"]):
                self.frame = 0
                self.usando_ultimate = False
        elif self.atacando:
            self.frame += 0.15
            if self.frame >= len(self.animacoes["attack"]):
                self.frame = 0
                self.atacando = False
        elif self.chutando:
            self.frame += 0.15
            if self.frame >= len(self.animacoes["chute"]):
                self.frame = 0
                self.chutando = False
        elif self.defendendo:
            ultimo_frame = len(self.animacoes["defesa"]) - 1
            if self.frame < ultimo_frame:
                self.frame += 0.3
                if self.frame > ultimo_frame:
                    self.frame = ultimo_frame
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
        if self.usando_ultimate:
            animacao = "especial"
        elif self.atacando:
            animacao = "attack"
        elif self.chutando:
            animacao = "chute"
        elif self.defendendo:
            animacao = "defesa"
        else:
            animacao = self.estado

        frames = self.animacoes[animacao] if self.direcao == 1 else self.animacoes_inverso[animacao]
        indice = min(indice, len(frames) - 1)
        
        imagem = frames[indice]
        img_rect = imagem.get_rect(center=self.rect.center)
        surface.blit(imagem, img_rect)