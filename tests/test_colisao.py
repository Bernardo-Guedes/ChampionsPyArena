from src.funcoes import verificar_colisao
import pygame

def test_verificar_colisao():
    r1 = pygame.Rect(0, 0, 100, 100)
    r2 = pygame.Rect(50, 50, 100, 100)

    assert verificar_colisao(r1, r2) is True