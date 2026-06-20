from src.personagem import Personagem, personagem1_sprites
import pygame
pygame.display.set_mode((1,1))

def test_receber_dano_reduz_vida():
    p = Personagem(100, personagem1_sprites)
    p.receber_dano(20)

    assert p.vida == 80

def test_bloquear_dano_mantem_vida():
    p = Personagem(100, personagem1_sprites)
    p.defendendo = True
    p.receber_dano(20)

    assert p.vida == 100