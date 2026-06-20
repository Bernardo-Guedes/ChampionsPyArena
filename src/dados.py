from src.config import CAMINHO_ARQ_HISTORICO

def carregar_historico():
    partidas = []
    contador = 0
    try:
        with open(CAMINHO_ARQ_HISTORICO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if contador < 5:
                    partidas.append(linha.strip())
                    contador += 1
                else:
                    break
    except FileNotFoundError:
        pass
    return partidas

def atualizar_historico(nova_partida):
    try:
        with open(CAMINHO_ARQ_HISTORICO, "r", encoding="utf-8") as arquivo:
            conteudo_antigo = arquivo.read()

    except FileNotFoundError:
        conteudo_antigo = ""

    with open(CAMINHO_ARQ_HISTORICO, "w", encoding="utf-8") as arquivo:
        arquivo.write(nova_partida)
        arquivo.write(conteudo_antigo)  