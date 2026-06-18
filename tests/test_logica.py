from src.personagem import Personagem, personagem1_sprites

def test_personagem_inicia_ataque():
    p = Personagem(100, personagem1_sprites)
    p.atacar()

    assert p.atacando is True
    assert p.estado == "attack"
    assert p.frame == 0