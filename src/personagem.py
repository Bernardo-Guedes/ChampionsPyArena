import pygame
from src.config import (ALTURA_TELA, CAMINHOS, FRAMES)
from src.sprites import ( carregar_animacao )

# Configuração das animações do primeiro personagem.
# Cada ação contém: caminho da spritesheet, coordenadas dos recortes dos frames e escala.
personagem1_sprites = {
    "idle": (CAMINHOS["idle"][0], FRAMES["idle"][0], 0.2),
    "ataque": (CAMINHOS["ataque"][0], FRAMES["ataque"][0], 0.5),
    "chute": (CAMINHOS["chute"][0], FRAMES["chute"][0], 0.5),
    "corrida": (CAMINHOS["corrida"][0], FRAMES["corrida"][0], 0.4),
    "especial": (CAMINHOS["especial"][0], FRAMES["especial"][0], 0.4),
    "defesa": (CAMINHOS["defesa"][0], FRAMES["defesa"][0], 0.3)
}

# Configuração das animações do segundo personagem.
# Cada ação contém: caminho da spritesheet, coordenadas dos recortes dos frames e escala.
personagem2_sprites = {
    "idle": (CAMINHOS["idle"][1], FRAMES["idle"][1], 0.16),
    "ataque": (CAMINHOS["ataque"][1], FRAMES["ataque"][1], 0.3),
    "chute": (CAMINHOS["chute"][1], FRAMES["chute"][1], 0.3),
    "corrida": (CAMINHOS["corrida"][1], FRAMES["corrida"][1], 0.4),
    "especial": (CAMINHOS["especial"][1], FRAMES["especial"][1], 0.3),
    "defesa": (CAMINHOS["defesa"][1], FRAMES["defesa"][1], 0.18)
}

class Personagem(pygame.sprite.Sprite):
    """
    Representa um personagem controlável durante a partida.

    A classe gerencia as animações, os atributos de combate (vida, dano e ultimate), os estados do personagem (parado, correndo, atacando, defendendo e utilizando golpe especial) e os métodos responsáveis por atualizar e desenhar o personagem na tela.
    """
    def __init__(self, rect_x, sprite_config):
        """
        Inicializa um personagem, carrega todas as animações, configura os atributos de combate e define
        a posição inicial na tela.

        Parâmetros:
            rect_x (int): Posição horizontal inicial do personagem.
            sprite_config (dict): Configuração contendo os caminhos das animações, coordenadas dos frames e escala de cada ação.

        Retorno:
            Inicializa um objeto da classe
        """
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
        """
        Inicia a animação e o estado de ataque do personagem.

        Parâmetros:
            Nenhum (apenas o self).

        Retorno:
            Modifica os estados do personagem.
        """
        if not self.atacando:
            self.atacando = True
            self.acertou_ataque = False
            self.frame = 0

    def chutar(self):
        """
        Inicia a animação e o estado de chute, caso o personagem não esteja atacando ou usando o ultimate.

        Parâmetros:
            Nenhum (apenas o self).
        
        Retorno:
            Modifica os estados do personagem.
        """
        if not self.chutando and not self.atacando and not self.usando_ultimate:
            self.chutando = True
            self.acertou_chute = False
            self.frame = 0

    def atacar_especial(self):
        """
        Executa o golpe especial caso a barra de ultimate esteja completamente carregada e o personagem não esteja atacando.

        Parâmetros:
            Nenhum (apenas o self).
        
        Retorno:
            Modifica os estados do personagem.
        """
        if self.ultimate >= self.ultimate_maximo and not self.atacando and not self.usando_ultimate:
            self.usando_ultimate = True
            self.acertou_ultimate = False
            self.frame = 0
            self.ultimate = 0

    def receber_dano(self, dano):
        """
        Aplica dano ao personagem que sofreu o ataque, mas caso o personagem esteja defendendo, o dano é bloqueado. Se a vida cair abaixo de 20% pela primeira vez, a barra de ultimate é preenchida.

        Parâmetros:
            dano (int): Quantidade de dano recebida.

        Retorno:
            bool:
                True se o dano foi aplicado.
                False se o ataque foi defendido.
        """
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
        """
        Aplica o dano causado pelo golpe especial no personagem que sofreu o golpe, mas caso o personagem esteja defendendo, o dano é bloqueado. Se a vida cair abaixo de 20% pela primeira vez, a barra de ultimate é preenchida.

        Parâmetros:
            dano_ultimate (int): Dano causado pelo golpe especial.

        Retorno:
            bool:
                True se o dano foi aplicado.
                False se o golpe foi defendido.
        """
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
        """
        Aumenta a barra de ultimate do personagem.

        Parâmetros:
            progresso_ultimate (int): Quantidade adicionada à barra de ultimate.

        Retorno:
            Modifica os estados do personagem.
        """
        self.ultimate += progresso_ultimate
        if self.ultimate > self.ultimate_maximo:
            self.ultimate = self.ultimate_maximo

    def update(self):
        """
        Atualiza o estado do personagem, controla a execução das animações e realiza a transição entre os estados do personagem conforme a ação que está sendo executada.

        Parâmetros:
            Nenhum (apenas o self).

        Retorno:
            Modifica os estados do personagem.
        """
        if self.usando_ultimate:
            self.frame += 0.08
            if self.frame >= len(self.animacoes["especial"]):
                self.frame = 0
                self.usando_ultimate = False
        elif self.atacando:
            self.frame += 0.15
            if self.frame >= len(self.animacoes["ataque"]):
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
                "corrida": 0.2
            }
            self.frame += velocidade_animacao[self.estado]
            if self.frame >= len(self.animacoes[self.estado]):
                self.frame = 0

    def draw(self, surface):
        """
        Desenha o personagem na tela, seleciona a animação correspondente ao estado atual do personagem e renderiza na superfície informada.

        Parâmetros:
            surface (pygame.Surface): Superfície onde o personagem será desenhado.

        Retorno:
            Modifica os estados do personagem e desenha na tela.
        """
        indice = int(self.frame)
        if self.usando_ultimate:
            animacao = "especial"
        elif self.atacando:
            animacao = "ataque"
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