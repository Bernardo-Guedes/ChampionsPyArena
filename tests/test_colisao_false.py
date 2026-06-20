from src.funcoes import verificar_colisao
import pygame

def test_verificar_colisao_falsa():
    """
    Testa se a função verificar_colisao retorna False quando
    dois retângulos estão completamente separados e não possuem
    nenhuma área de interseção.
    """
    r1 = pygame.Rect(0, 0, 100, 100)
    r2 = pygame.Rect(200, 200, 100, 100)

    assert verificar_colisao(r1, r2) is False