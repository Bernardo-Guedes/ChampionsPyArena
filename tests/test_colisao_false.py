from src.funcoes import verificar_colisao
import pygame

def test_verificar_colisao_falsa():
    r1 = pygame.Rect(0, 0, 100, 100)
    r2 = pygame.Rect(200, 200, 100, 100)

    assert verificar_colisao(r1, r2) is False