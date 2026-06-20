from src.personagem import Personagem, personagem1_sprites
from src.funcoes import limitar_valor

def test_vida_nao_fica_negativa():
    p = Personagem(100, personagem1_sprites)

    p.receber_dano(999)

    assert p.vida == 0

