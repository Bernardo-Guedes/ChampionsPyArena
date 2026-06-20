from src.personagem import Personagem, personagem1_sprites, personagem2_sprites
from src.funcoes import verificar_ataque, verificar_chute
import pygame
pygame.display.set_mode((1,1))

# =================== TESTES DO ATAQUE ======================

def test_personagem_inicia_ataque():
    """
    Dado que ao apertar a tecla de ataque o personagem precisa iniciar a ação de ataque.
    
    Quando a função atacar é chamada, o assert deve retornar True para o atributo atacando, 
    para o estado igual a "idle", pois é o estado que antecede o estado de "attack" e deve retornar 
    True para o frame de "attack" igual a 0, que significa o início da renderização da animacão de ataque
    """
    p = Personagem(100, personagem1_sprites)
    p.atacar()

    assert p.atacando is True
    assert p.estado == "idle"
    assert p.frame == 0

def test_ataque_bem_sucedido():
    """
    Dado que ao atacar e assertar o adversário o adversário precisa sofrer o dano e a barra de ultimate deve ser atualizada.

    Quando a função verificar ataque é chamada, os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo atacando é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 95,
    pois é a vida (100) menos o dano (20), para o ultimate do personagem 1 igual a 10, que é o valor atualizado
    e deve retornar True para o atributo acertou_ataque igual a True, pois o ataque foi bem sucedido
    """
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
    """
    Dado que ao atacar e não acertar o adversário, o adversário não sofre o dano e a barra de ultimate não deve ser atualizada.

    Quando a função verificar ataque é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo atacando é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 100,
    pois não ocorre o dano, para o ultimate do personagem 1 igual a 0, que é o valor inicial já que não ocorre atualização
    e deve retornar True para o atributo acertou_ataque igual a False, pois o ataque não foi bem sucedido
    """
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
    """
    Dado que ao atacar, acertar o adversário e o adversário estiver bloqueando, o adversário não sofre o dano e a barra de ultimate não deve ser atualizada.

    Quando a função verificar ataque é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima, o atributo atacando é verdadeiro e o atributo defendendo é verdadeiro também, 
    o assert deve retornar True para a vida do personagem 2 igual a 100,
    pois não ocorre o dano, para o ultimate do personagem 1 igual a 0, que é o valor inicial já que não há atualização
    e deve retornar True para o atributo acertou_ataque igual a True, pois o ataque foi bem sucedido, mas foi defendido
    """
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
    """
    Dado que ao apertar a tecla de chute o personagem precisa iniciar a ação de ataque.

    Quando a função chutar é chamada, o assert deve retornar True para o atributo chutando, 
    para o estado igual a "idle", pois é o estado que antecede o estado de "chute" e deve retornar 
    True para o frame de "chute" igual a 0, que significa o início da renderização da animacão de chute
    """
    p = Personagem(100, personagem1_sprites)
    p.chutar()

    assert p.chutando is True
    assert p.estado == "idle"
    assert p.frame == 0

def test_chute_bem_sucedido():
    """
    Dado que ao chutar e acertar o adversário, o adversário precisa sofrer o dano e a barra de ultimate deve ser atualizada.

    Quando a função verificar_chute é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo chutando é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 95,
    pois é a vida (100) menos o dano (20), para o ultimate do personagem 1 igual a 10, que é o valor atualizado
    e deve retornar True para o atributo acertou_chute igual a True, pois o chute foi bem sucedido
    """
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
    """
    Dado que ao chutar e não acertar o adversário, o adversário não sofre o dano e a barra de ultimate não deve ser atualizada.

    Quando a função verificar_chute é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima e o atributo chutando é verdadeiro, o assert deve retornar True para a vida do personagem 2 igual a 100,
    pois não ocorre o dano, para o ultimate do personagem 1 igual a 0, que é o valor inicial já que não ocorre atualização
    e deve retornar True para o atributo acertou_chute igual a False, pois o chute não foi bem sucedido
    """
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
    """
    Dado que ao chutar, acertar o adversário e o adversário estiver bloqueando, 
    o adversário não sofre o dano e a barra de ultimate não deve ser atualizada.

    Quando a função verificar_chute é chamada, e os personagens estão de frente um para o outro e em uma distância
    próxima, o atributo chutando é verdadeiro e o atributo defendendo é verdadeiro também, o assert deve retornar True para a vida do personagem 2 igual a 100, pois não ocorre o dano, para o ultimate do personagem 1 igual a 0, que é o valor inicial já que não há atualização
    e deve retornar True para o atributo acertou_chute igual a True, pois o chute foi bem sucedido, mas foi defendido.
    """
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




