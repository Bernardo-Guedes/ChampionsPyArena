# Configurações centrais do jogo (tela, cores e caminhos de arquivos).
LARGURA_TELA = 1400
ALTURA_TELA = 600
FPS = 60

TITULO_JOGO = "Champions of the Py Arena"
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212,212,212)

CAMINHO_CENARIO = "assets/imagens/tela/cenario.png"
CAMINHO_FUNDO_INICIAL = "assets/imagens/tela/fundo_inicial.png"
CAMINHO_FUNDO_HISTORICO = "assets/imagens/tela/fundo_historico.png"
CAMINHO_LOGO = "assets/imagens/tela/logo.png"
CAMINO_START = "assets/imagens/tela/btn_start.png"
CAMINHO_EXIT = "assets/imagens/tela/btn_exit.png"
CAMINHO_BACK = "assets/imagens/tela/btn_voltar.png"
CAMINHO_BTN_HISTORICO = "assets/imagens/tela/btn_historico.png"
CAMINHO_ARQ_HISTORICO = "data/historico.txt"
CAMINHO_SPRITE_IDLE = "assets/imagens/sprites/sprite_idle.bmp"
CAMINHO_SPRITE_ATTACK = "assets/imagens/sprites/sprite_attack.bmp"
CAMINHO_SPRITE_RUN = "assets/imagens/sprites/sprite_run.bmp"

FRAMES_IDLE = [
        (59, 107, 105, 87),
        (303, 104, 105, 90),
        (547, 104, 105, 90),
        (793, 107, 105, 87),
        (1030, 110, 111, 84),
        (1279, 113, 105, 81),
        (1523, 110, 105, 84),
        (1767, 110, 105, 84),
        (2011, 110, 105, 84)
]

FRAMES_ATTACK = [
    (55, 124, 107, 59),
    (305, 121, 101, 65),
    (570, 52, 80, 143),
    (814, 52, 80, 134),
    (1049, 52, 86, 131),
    (1290, 49, 89, 134),
    (1534, 52, 89, 131),
    (1780, 25, 170, 191),
    (2013, 121, 107, 65)
]

FRAMES_RUN = [
    (55, 100, 140, 100),
    (305, 100, 140, 100),
    (570, 100, 140, 100),
    (814, 100, 140, 100),
    (1049, 100, 140, 100),
    (1290, 100, 140, 100)
]