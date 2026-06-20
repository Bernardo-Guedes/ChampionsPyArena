from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.funcoes import verificar_especial
import pygame
pygame.display.set_mode((1,1))

def test_ultimate_nao_ultrapassa_maximo():
    p = Personagem(100, personagem1_sprites)

    p.carregar_ultimate(200)

    assert p.ultimate == p.ultimate_maximo

def test_ultimate_bem_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.usando_ultimate = True
    p1.frame = 2

    verificar_especial(p1, p2, 1)

    assert p2.vida == 80
    assert p1.acertou_ultimate is True

def test_ultimate_mal_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(500, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.usando_ultimate = True
    p1.frame = 2

    verificar_especial(p1, p2, 1)

    assert p2.vida == 100
    assert p1.acertou_ultimate is False

def test_ultimate_bloqueado():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.usando_ultimate = True
    p1.frame = 2
    p2.defendendo = True

    verificar_especial(p1, p2, 1)

    assert p2.vida == 100
    assert p1.acertou_ultimate is True



