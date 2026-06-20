from src.personagem import Personagem, personagem1_sprites
<<<<<<< HEAD
=======
from src.funcoes import limitar_valor
>>>>>>> c5d5bfd8d8bf2e4594fbe5fa5917d6536e7cdf48

def test_ultimate_nao_ultrapassa_maximo():
    p = Personagem(100, personagem1_sprites)

    p.carregar_ultimate(200)

    assert p.ultimate == p.ultimate_maximo