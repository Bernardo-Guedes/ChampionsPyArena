from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.funcoes import verificar_ataque, verificar_chute
import pygame
pygame.display.set_mode((1,1))

# =================== TESTES DO ATAQUE ======================

def test_personagem_inicia_ataque():
    p = Personagem(100, personagem1_sprites)
    p.atacar()

    assert p.atacando is True
    assert p.estado == "idle"
    assert p.frame == 0

def test_ataque_bem_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.atacando = True
    p1.frame = 4

    verificar_ataque(p1, p2, 1)

    assert p2.vida == 95
    assert p1.ultimate == 10
    assert p1.acertou_ataque is True

def test_ataque_mal_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(500, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.atacando = True
    p1.frame = 4

    verificar_ataque(p1, p2, 1)

    assert p2.vida == 100
    assert p1.ultimate == 0
    assert p1.acertou_ataque is False

def test_ataque_bloqueado():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.atacando = True
    p1.frame = 4
    p2.defendendo = True

    verificar_ataque(p1, p2, 1)

    assert p2.vida == 100
    assert p1.ultimate == 0
    assert p1.acertou_ataque is True


# ================= TESTES DO CHUTE ====================

def test_personagem_inicia_chute():
    p = Personagem(100, personagem1_sprites)
    p.chutar()

    assert p.chutando is True
    assert p.estado == "idle"
    assert p.frame == 0

def test_chute_bem_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.chutando = True
    p1.frame = 4

    verificar_chute(p1, p2, 1)

    assert p2.vida == 95
    assert p1.ultimate == 10
    assert p1.acertou_chute is True

def test_chute_mal_sucedido():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(500, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.chutando = True
    p1.frame = 4

    verificar_chute(p1, p2, 1)

    assert p2.vida == 100
    assert p1.ultimate == 0
    assert p1.acertou_chute is False

def test_chute_bloqueado():
    p1 = Personagem(100, personagem1_sprites)
    p2 = Personagem(200, personagem2_sprites)

    p1.direcao = 1
    p2.direcao = -1
    p1.ultimate = 0
    p1.chutando = True
    p1.frame = 4
    p2.defendendo = True

    verificar_chute(p1, p2, 1)

    assert p2.vida == 100
    assert p1.ultimate == 0
    assert p1.acertou_chute is True




