from src.personagem import Personagem, personagem1_sprites
import pygame
pygame.display.set_mode((1,1))

def test_receber_dano_reduz_vida():
    """
    Dado que o Personagem precisa reduzir a vida ao receber um dano.

    Quando a função receber_dano() é chamada com o parâmetro 20, o assert deve retornar True
    para a vida do personagem igual a 80, pois a vida total (100) é subtraída pelo dano (20)
    """
    p = Personagem(100, personagem1_sprites)

    p.receber_dano(20)

    assert p.vida == 80

def test_bloquear_dano_mantem_vida():
    """
    Dado que o Personagem, ao realizar a ação de bloqueio, não pode sofrer dano.
    
    Quando a função receber_dano() é chamada com parâmetro 20 e ao mesmo tempo o 
    atributo defendendo é declarado como True, então o assert deve retornar True para a vida do 
    Personagem igual a 100, pois a vida do personagem (100) não é subtraída pelo dano (20)
    """
    p = Personagem(100, personagem1_sprites)
    p.defendendo = True
    p.receber_dano(20)

    assert p.vida == 100