# Nome do Jogo

> Champions of the Py Arena

## Integrantes do grupo

- Bernardo Guedes da Silveira
- Kaique Rodrigues do Vale
- Paulo César Monteiro

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites, dados, telas, personagens).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (histórico).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> Champions of the Py Arena é um jogo de luta local para dois jogadores em que cada participante controla um personagem dentro de uma arena. O objetivo é derrotar o adversário reduzindo sua barra de vida a zero por meio de ataques e movimentação estratégica. 
> Durante a partida, os jogadores devem escapar dos golpes inimigos e encontrar oportunidades para atacar. Os jogadores podem utilizar uma habilidade especial chamada "Ultimate" que é desbloqueada quando sua barra é totalmente preenchida.


## Objetivo do jogador

> O objetivo é evitar os golpes desferidos pelo adversário, encontrar momentos oportunos para desferir e acertar golpes, para entãoreduzir os pontos de vida do oponente a zero, vencendo a disputa.

## Regras do jogo

- Regra 1: O jogador se movimenta usando as setas do teclado ou WASD.
- Regra 2: O jogador começa com 100 pontos de vida.
- Regra 3: Cada golpe aplicado tira 5 pontos de vida do adversário.
- Regra 4: Cada golpe aplicado no adversário aumenta o preenchimento da barra do Ultimate.
- Regra 5: Ao atingir 20 pontos de vida, o jogador libera automaticamente o Ultimate - Ainda não implementado
- Regra 6: O jogador vence e o combate termina se o adversário chegar a 0 pontos de vida.


## Controles

- Tecla A: mover para esquerda (jogador 1)
- Tecla D: mover para direita (jogador 1)
- Tecla W: soco (jogador 1)
- Tecla S: chute (jogador 1)
- Tecla E: Ultimate (jogador 1)
- Seta para esquerda: mover para esquerda (jogador 2)
- Seta para direita: mover para direita (jogador 2)
- Seta para cima: soco (jogador 2)
- Seta para baixo: chute (jogador 2)
- Enter: Ultimate (jogador 2)
- ESC: Menu de Pause - Ainda não implementado


## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Bernardo-Guedes/ChampionsPyArena
cd ChampionsPyArena
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
