from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.funcoes import verificar_especial
import pygame
pygame.display.set_mode((1,1))

def test_ultimate_nao_ultrapassa_maximo():
    """
    Dado que ao chegar no máximo do ultimate o valor não deve ser aumentado.

    Quando a função carregar_ultimate é chamada com o parâmetro 200, o assert deve
    retornar True para o ultimate do personagem igual ao ultimate máximo, visto que o
    valor do ultimate não deve passar do valor máximo
    """
    p = Personagem(100, personagem1_sprites)

    p.carregar_ultimate(200)

    assert p.ultimate == p.ultimate_maximo

def test_ultimate_bem_sucedido():
    """
    Dado que ao usar o ultimate e acertar o adversário, o adversário precisa sofrer o dano do ultimate.

    Quando a função verificar_especial é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo usando_ultimate é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 80,
    pois é a vida (100) menos o dano do ultimate (20) e deve retornar True para o atributo acertou_ultimate igual a True, 
    pois o ultimate foi bem sucedido
    """
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
    """
    Dado que ao usar o ultimate e não acertar o adversário, o adversário não sofre o dano.

    Quando a função verificar_ultimate é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo usando_especial é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 100,
    pois não ocorre o dano, e deve retornar True para o atributo acertou_ultimate igual a False, pois o ultimate não foi bem sucedido
    """
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
    """
    Dado que ao usar o ultimate, acertar o adversário e o adversário estiver bloqueando, o adversário não sofre o dano.
    
    Quando a função verificar_especial é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima, o atributo usando_ultimate é verdadeiro e o atributo defendendo é verdadeiro também, 
    o assert deve retornar True para a vida do personagem 2 igual a 100, pois não ocorre o dano e deve retornar True 
    para o atributo acertou_ultimate igual a True, pois o ultimate foi bem sucedido, mas foi defendido
    """
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



