from src.personagem import Personagem, personagem1_sprites
import pygame
pygame.display.set_mode((1,1))

def test_vida_nao_fica_negativa():
    """
    Dado que a vida do personagem não pode ser menor que 0.
    
    Quando a função receber_dano() é chamada com parâmetro 999, o assert
    deve retornar True para a vida igual a 0, visto que a vida do personagem
    não pode ser negativa
    """
    p = Personagem(100, personagem1_sprites)

    p.receber_dano(999)

    assert p.vida == 0