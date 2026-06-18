from src.personagem import Personagem, personagem1_sprites
from src.funcoes import limitar_valor

def test_ultimate_nao_ultrapassa_maximo():
    p = Personagem(100, personagem1_sprites)

    p.carregar_ultimate(200)

    assert p.ultimate == p.ultimate_maximo