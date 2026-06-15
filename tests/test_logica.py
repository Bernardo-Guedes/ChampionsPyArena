from src.personagem import Personagem, personagem1_sprites

def test_personagem_inicia_ataque():
    p = Personagem(100, personagem1_sprites)
    p.atacar()

    assert p.atacando is True
    assert p.estado == "attack"
    assert p.frame == 0

def test_receber_dano_reduz_vida():
    p = Personagem(100, personagem1_sprites)

    p.receber_dano(20)

    assert p.vida == 80