
import pygame
from src.config import SONS_CONFIG


# Inicialização do sistema de áudio do Pygame.
pygame.mixer.init()

# Carrega os efeitos sonoros dos ataques de espada.
sons_ataque = [
    pygame.mixer.Sound(SONS_CONFIG["ataque1"]["caminho"]),
    pygame.mixer.Sound(SONS_CONFIG["ataque2"]["caminho"])
]

# Carrega os efeitos sonoros dos golpes de soco.
sons_soco = [
    pygame.mixer.Sound(SONS_CONFIG["soco1"]["caminho"]),
    pygame.mixer.Sound(SONS_CONFIG["soco2"]["caminho"])
]

# Carrega o efeito sonoro do chute.
sons_chute = [
    pygame.mixer.Sound(SONS_CONFIG["chute1"]["caminho"])
]

# Carrega o efeito sonoro da defesa.
sons_defesa = [
    pygame.mixer.Sound(SONS_CONFIG["defesa1"]["caminho"])
]

# Carrega os efeitos sonoros dos golpes especiais.
sons_especial = [
    pygame.mixer.Sound(SONS_CONFIG["especial1"]["caminho"]),
    pygame.mixer.Sound(SONS_CONFIG["especial2"]["caminho"])
]

# Carrega o efeito sonoro da corrida.
sons_corrida = [
    pygame.mixer.Sound(SONS_CONFIG["corrida1"]["caminho"])
]

# Agrupa todos os efeitos sonoros em um dicionário para facilitar o acesso pelos outros módulos do jogo.
sons = {
    "ataques": sons_ataque,
    "socos": sons_soco,
    "chutes": sons_chute,
    "defesas": sons_defesa,
    "especiais": sons_especial,
    "corridas": sons_corrida
}