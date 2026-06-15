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
CAMINHO_IDLE_1 = "assets/imagens/sprites/sprite_idle.bmp"
CAMINHO_IDLE_2 = "assets/imagens/sprites/sprite_idle2.bmp"
CAMINHO_ATTACK_1 = "assets/imagens/sprites/sprite_attack.bmp"
CAMINHO_ATTACK_2 = "assets/imagens/sprites/sprite_attack2.bmp"
CAMINHO_CHUTE_1 = "assets/imagens/sprites/sprite_chute.bmp"
CAMINHO_CHUTE_2 = "assets/imagens/sprites/sprite_chute2.bmp"
CAMINHO_RUN_1 = "assets/imagens/sprites/sprite_run.bmp"
CAMINHO_RUN_2 = "assets/imagens/sprites/sprite_run2.bmp"
CAMINHO_ESPECIAL_1 = "assets/imagens/sprites/sprite_especial.bmp"
CAMINHO_ESPECIAL_2 = "assets/imagens/sprites/sprite_especial2.bmp"

FRAMES_IDLE_1 = [
    (100, 66, 447, 636),
    (838, 109, 435, 594)
]

FRAMES_IDLE_2 = [
    (66,  149, 636, 697),   # Frame 1 — postura ereta
    (849,  88, 626, 758),   # Frame 2 — postura abaixada (respiração)
]

FRAMES_ATTACK_1 = [
    (2,    6, 361, 391),
    (368,  6, 356, 391),
    (729,  6, 354, 391),
    (1088, 6, 354, 391),
    (1447, 6, 356, 391),
    (1808, 6, 361, 391)
]

FRAMES_ATTACK_2 = [
    (48,   66, 396, 385),   # Frame 1 — postura inicial
    (573,  68, 475, 383),   # Frame 2 — recuo / preparação
    (1176, 80, 390, 370),   # Frame 3 — impacto
    (1679, 64, 390, 387),   # Frame 4 — retorno à guarda
]

FRAMES_CHUTE_1 = [
    (6,    6, 306, 343),
    (320,  6, 309, 343),
    (637,  6, 305, 343),
    (951,  6, 325, 343),
    (1284, 6, 315, 343),
    (1607, 6, 287, 343),
    (1902, 6, 284, 343)
]

FRAMES_CHUTE_2 = [
    (10,   16, 485, 464),
    (511,  16, 485, 464),
    (1013, 16, 484, 464),
    (1513, 16, 486, 464)
]

FRAMES_RUN_1 = [
    (9,    6, 399, 421), 
    (420,  6, 409, 420),
    (841,  6, 413, 421),
    (1266, 6, 419, 421),
    (1697, 6, 413, 420)
]

FRAMES_RUN_2 = [
    (52,   58, 199, 266),
    (331,  58, 223, 265),
    (643,  65, 201, 258),
    (932,  63, 202, 260),
    (1205, 59, 219, 258),
    (1504, 59, 202, 265)
]

FRAMES_ESPECIAL_1 = [
    (8,    8, 606, 559),
    (614,  8, 615, 559),
    (1229, 8, 610, 559)
]

FRAMES_ESPECIAL_2 = [
    (10,   17, 436, 432),
    (466,  17, 453, 432),
    (937,  17, 453, 432),
    (1409, 17, 435, 432)
]