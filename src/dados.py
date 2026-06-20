from src.config import CAMINHO_ARQ_HISTORICO

def carregar_historico():
    """
    Lê o arquivo de histórico e armazena os registros encontrados. Caso o arquivo não exista, retorna uma lista vazia.o.

    Parâmetros:
        Nenhum parâmetro.

    Retorna:
        list[str]: Lista contendo até as 5 partidas mais recentes registradas no histórico.
    """
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
    """
    Atualiza o histórico de partidas do jogo.

    Parâmetros:
        nova_partida (str): Registro da nova partida que será adicionado ao histórico.

    Retorna:
        Insere a nova partida no início do arquivo de histórico, mantendo os registros anteriores.
    """
    try:
        with open(CAMINHO_ARQ_HISTORICO, "r", encoding="utf-8") as arquivo:
            conteudo_antigo = arquivo.read()

    except FileNotFoundError:
        conteudo_antigo = ""

    with open(CAMINHO_ARQ_HISTORICO, "w", encoding="utf-8") as arquivo:
        arquivo.write(nova_partida)
        arquivo.write(conteudo_antigo)  