from src.funcoes import verificar_colisao
import pygame

def test_verificar_colisao():
    r1 = pygame.Rect(0, 0, 100, 100)
    r2 = pygame.Rect(50, 50, 100, 100)

<<<<<<< HEAD
    assert verificar_colisao(r1, r2) is True

def test_verificar_colisao_falsa():
    r1 = pygame.Rect(0, 0, 100, 100)
    r2 = pygame.Rect(200, 200, 100, 100)

    assert verificar_colisao(r1, r2) is False
=======
    assert verificar_colisao(r1, r2) is True
>>>>>>> c5d5bfd8d8bf2e4594fbe5fa5917d6536e7cdf48
