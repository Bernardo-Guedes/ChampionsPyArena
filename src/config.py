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
CAMINHO_FUNDO_FIM = "assets/imagens/tela/fundo_fim.png"
CAMINHO_LOGO = "assets/imagens/tela/logo.png"
CAMINO_START = "assets/imagens/tela/btn_start.png"
CAMINHO_EXIT = "assets/imagens/tela/btn_exit.png"
CAMINHO_BACK = "assets/imagens/tela/btn_voltar.png"
CAMINHO_BTN_HISTORICO = "assets/imagens/tela/btn_historico.png"
CAMINHO_ARQ_HISTORICO = "data/historico.txt"
CAMINHO_SPRITE_IDLE = "assets/imagens/sprites/sprite_idle.bmp"
CAMINHO_SPRITE_ATTACK = "assets/imagens/sprites/teste_sprite.bmp"
CAMINHO_SPRITE_CHUTE = "assets/imagens/sprites/sprite_chute.bmp"
CAMINHO_SPRITE_RUN = "assets/imagens/sprites/sprite_movimentacao.bmp"

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
    (2,    6, 361, 391),   # Frame 1
    (368,  6, 356, 391),   # Frame 2
    (729,  6, 354, 391),   # Frame 3
    (1088, 6, 354, 391),   # Frame 4
    (1447, 6, 356, 391),   # Frame 5
    (1808, 6, 361, 391),   # Frame 6
]

FRAMES_CHUTE = [
    (6,    6, 306, 343),   # Frame 1
    (320,  6, 309, 343),   # Frame 2
    (637,  6, 305, 343),   # Frame 3
    (951,  6, 325, 343),   # Frame 4
    (1284, 6, 315, 343),   # Frame 5
    (1607, 6, 287, 343),   # Frame 6
    (1902, 6, 284, 343),   # Frame 7
]

FRAMES_RUN = [
    (9,    6, 399, 421),   # Frame 1
    (420,  6, 409, 420),   # Frame 2
    (841,  6, 413, 421),   # Frame 3
    (1266, 6, 419, 421),   # Frame 4
    (1697, 6, 413, 420),   # Frame 5
]