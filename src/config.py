# ==========================================================
# Configurações gerais do jogo
# ==========================================================

LARGURA_TELA = 1400
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "Champions of the Py Arena"
CAMINHO_ARQ_HISTORICO = "data/historico.txt"


# ================================================================================
# Configuração dos elementos gráficos da tela principal (utilizando dicionários)
#
# Cada elemento define:
# - caminho: localização da imagem;
# - convert_alpha: indica se será utilizado confert_alpha() ou convert();
# - scale: escala a ser aplicada na renderização.
# =================================================================================

ELEMENTOS_TELA_PRINCIPAL_CONFIG = {
    "cenario": {
        "caminho": "assets/imagens/tela/cenario.png",
        "convert_alpha": False,
        "scale": (LARGURA_TELA, ALTURA_TELA)
    },
    "avatar1": {
        "caminho": "assets/imagens/tela/avatar1.png",
        "convert_alpha": True,
        "scale": (90, 120)
    },
    "avatar2": {
        "caminho": "assets/imagens/tela/avatar2.png",
        "convert_alpha": True,
        "scale": (90, 120)
    },
    "moldura_tempo": {
        "caminho": "assets/imagens/tela/moldura_tempo.png",
        "convert_alpha": True,
        "scale": (300, 77)
    },
    "moldura_vida": {
        "caminho": "assets/imagens/tela/moldura_vida.png",
        "convert_alpha": True,
        "scale": (250, 37)
    },
    "moldura_ultimate": {
        "caminho": "assets/imagens/tela/moldura_ultimate.png",
        "convert_alpha": True,
        "scale": (250, 37)
    }
}


# ==========================================================
# Configuração dos elementos gráficos das telas secundárias
# (menu inicial, pausa, histórico e fim de partida).
# ==========================================================

ELEMENTOS_TELAS_SEC_CONFIG = {
    "logo": {
        "caminho": "assets/imagens/tela/logo.png",
        "convert_alpha": True,
        "scale": (700, 350)
    },
    "titulo_pause": {
        "caminho": "assets/imagens/tela/titulo_pause.png",
        "convert_alpha": True,
        "scale": (600, 171)
    },
    "btn_start": {
        "caminho": "assets/imagens/tela/btn_start.png",
        "convert_alpha": True
    },
    "btn_resume": {
        "caminho": "assets/imagens/tela/btn_resume.png",
        "convert_alpha": True
    },
    "btn_exit": {
        "caminho": "assets/imagens/tela/btn_exit.png",
        "convert_alpha": True
    },
    "btn_back": {
        "caminho": "assets/imagens/tela/btn_voltar.png",
        "convert_alpha": True
    },
    "btn_historico": {
        "caminho": "assets/imagens/tela/btn_historico.png",
        "convert_alpha": True
    },
    "fundo_inicial": {
        "caminho": "assets/imagens/tela/fundo_inicial.png",
        "convert_alpha": True,
        "scale": (LARGURA_TELA, ALTURA_TELA)
    },
    "fundo_historico": {
        "caminho": "assets/imagens/tela/fundo_historico.png",
        "convert_alpha": True,
        "scale": (LARGURA_TELA, ALTURA_TELA)
    },
    "fundo_fim": {
        "caminho": "assets/imagens/tela/fundo_fim.png",
        "convert_alpha": True,
        "scale": (LARGURA_TELA, ALTURA_TELA)
    }
}


# ===============================================================
# Caminhos das spritesheets de cada animação de cada personagem.
# ===============================================================

CAMINHO_IDLE_1 = "assets/imagens/sprites/sprite_idle.bmp"
CAMINHO_IDLE_2 = "assets/imagens/sprites/sprite_idle2.bmp"
CAMINHO_ATAQUE_1 = "assets/imagens/sprites/sprite_attack.bmp"
CAMINHO_ATAQUE_2 = "assets/imagens/sprites/sprite_attack2.bmp"
CAMINHO_CHUTE_1 = "assets/imagens/sprites/sprite_chute.bmp"
CAMINHO_CHUTE_2 = "assets/imagens/sprites/sprite_chute2.bmp"
CAMINHO_CORRIDA_1 = "assets/imagens/sprites/sprite_run.bmp"
CAMINHO_CORRIDA_2 = "assets/imagens/sprites/sprite_run2.bmp"
CAMINHO_ESPECIAL_1 = "assets/imagens/sprites/sprite_especial.bmp"
CAMINHO_ESPECIAL_2 = "assets/imagens/sprites/sprite_especial2.bmp"
CAMINHO_DEFESA_1 = "assets/imagens/sprites/sprite_defesa.bmp"
CAMINHO_DEFESA_2 = "assets/imagens/sprites/sprite_defesa2.bmp"



# ======================================================================
# Coordenadas dos frames das animações a serem utilizanas em sprites.py.
#
# Cada tupla possui o formato:
# (x, y, largura, altura)
# - x e y representam a posição inicial do frame na spritesheet;
# - largura e altura representam suas dimensões.
# ======================================================================
FRAMES_IDLE_1 = [
    (100, 66, 447, 636),
    (838, 109, 435, 594)
]

FRAMES_IDLE_2 = [

    (66, 149, 636, 697),
    (849, 88, 626, 758)
]

FRAMES_ATAQUE_1 = [
    (2, 6, 361, 391),
    (368, 6, 356, 391),
    (729, 6, 354, 391),
    (1088, 6, 354, 391),
    (1447, 6, 356, 391),
    (1808, 6, 361, 391)
]

FRAMES_ATAQUE_2 = [
    (48, 66, 396, 385),
    (573, 68, 475, 383),
    (1176, 80, 390, 370),
    (1679, 64, 390, 387)
]

FRAMES_CHUTE_1 = [
    (6, 6, 306, 343),
    (320, 6, 309, 343),
    (637, 6, 305, 343),
    (951, 6, 325, 343),
    (1284, 6, 315, 343),
    (1607, 6, 287, 343),
    (1902, 6, 284, 343)
]

FRAMES_CHUTE_2 = [
    (47, 65, 404, 391),
    (562, 54, 472, 411),
    (1207, 45, 357, 412),
    (1696, 65, 401, 388)
]

FRAMES_CORRIDA_1 = [
    (9, 6, 399, 421), 
    (420, 6, 409, 420),
    (841, 6, 413, 421),
    (1266, 6, 419, 421),
    (1697, 6, 413, 420)
]

FRAMES_CORRIDA_2 = [
    (52, 58, 199, 266),
    (331, 58, 223, 265),
    (643, 65, 201, 258),
    (932, 63, 202, 260),
    (1205, 59, 219, 258),
    (1504, 59, 202, 265)
]

FRAMES_ESPECIAL_1 = [
    (119,  136, 263, 354),
    (666,   46, 325, 442),
    (1204, 106, 591, 387)
]

FRAMES_ESPECIAL_2 = [
    (45, 85, 420, 379),
    (555, 68, 472, 396),
    (1153, 12, 422, 452),
    (1659, 12, 429, 455)
]

FRAMES_DEFESA_1 = [
    (58, 70, 284, 416),
    (544, 34, 256, 454)
]

FRAMES_DEFESA_2 = [
    (97, 72, 639, 667),
    (834, 80, 599, 659)
]


# Agrupa os frames de todas as animações por ação e personagem em um dicionário.
FRAMES = {
    "idle": [FRAMES_IDLE_1, FRAMES_IDLE_2],
    "ataque": [FRAMES_ATAQUE_1, FRAMES_ATAQUE_2],
    "chute": [FRAMES_CHUTE_1, FRAMES_CHUTE_2],
    "especial": [FRAMES_ESPECIAL_1, FRAMES_ESPECIAL_2],
    "defesa": [FRAMES_DEFESA_1, FRAMES_DEFESA_2],
    "corrida": [FRAMES_CORRIDA_1, FRAMES_CORRIDA_2]
}

# Associa cada ação aos respectivos caminhos dos arquivos de spritesheet utilizados pelos personagens.
CAMINHOS = {
    "idle": [CAMINHO_IDLE_1, CAMINHO_IDLE_2],
    "ataque": [CAMINHO_ATAQUE_1, CAMINHO_ATAQUE_2],
    "chute": [CAMINHO_CHUTE_1, CAMINHO_CHUTE_2],
    "especial": [CAMINHO_ESPECIAL_1, CAMINHO_ESPECIAL_2],
    "defesa": [CAMINHO_DEFESA_1, CAMINHO_DEFESA_2],
    "corrida": [CAMINHO_CORRIDA_1, CAMINHO_CORRIDA_2]
}


# ==========================================================
# Configuração dos efeitos sonoros do jogo.
#
# Cada elemento define:
# - caminho do arquivo de áudio;
# - volume utilizado durante a reprodução.
# ==========================================================
SONS_CONFIG = {
    "ataque1": {"caminho": "assets/sons/ataque1.wav", "volume": 0.6},
    "ataque2": {"caminho": "assets/sons/ataque2.wav", "volume": 0.9},
    "soco1": {"caminho": "assets/sons/soco1.wav", "volume": 0.6},
    "soco2": {"caminho": "assets/sons/soco2.wav", "volume": 0.6},
    "chute1": {"caminho": "assets/sons/chute.wav", "volume": 0.6},
    "especial1": {"caminho": "assets/sons/Especial1.wav", "volume": 0.6},
    "especial2": {"caminho": "assets/sons/Especial2.wav", "volume": 0.6},
    "defesa1": {"caminho": "assets/sons/Defesa.wav", "volume": 0.6},
    "corrida1": {"caminho": "assets/sons/Corrida.wav", "volume": 1.0},
}
