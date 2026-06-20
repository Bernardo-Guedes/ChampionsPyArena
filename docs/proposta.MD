# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Champions of the Py Arena


## 2. Integrantes do grupo

- Nome 1: Bernardo Guedes da Silveira
- Nome 2: Kaique Rodrigues do Vale
- Nome 3: Paulo César Monteiro


## 3. Tipo de jogo

> Jogo de luta entre dois jogadores locais

## 4. Descrição geral do jogo

Descrição:

> Champions of the Py Arena é um jogo de luta local para dois jogadores em que cada participante controla um personagem dentro de uma arena. O objetivo é derrotar o adversário reduzindo sua barra de vida a zero por meio de ataques e movimentação estratégica. 
> Durante a partida, os jogadores devem desviar dos golpes inimigos e encontrar oportunidades para atacar. Os jogadores podem utilizar uma habilidade especial chamada "Ultimate" que é desbloqueada quando sua barra é totalmente preenchida. Quando a vida de um personagem chega a 20%, ele desbloqueia automaticamente o "Ultimate", capaz de causar grande dano e mudar o rumo da luta.


## 5. Objetivo do jogador

Objetivo:

> Evitar os golpes desferidos pelo adversário;
> Encontrar momentos oportunos para desferir  e acertar golpes;
> Se perto da derrota, utilizar o Ultimate para tentar virar o jogo.
> Reduzir os pontos de vida do oponente a zero, vencendo a disputa;


## 6. Regras principais

Liste as principais regras do jogo.

Regras do grupo:

- Regra 1: O jogador começa com 100 pontos de vida.
- Regra 2: Cada golpe aplicado tira 5 pontos de vida do adversário.
- Regra 3: Cada golpe aplicado no adversário aumenta o preenchimento da barra do Ultimate.
- Regra 4: Ao atingir 20 pontos de vida, o jogador libera automaticamente o Ultimate.
- Regra 5: O jogador vence e o combate termina se o adversário chegar a 0 pontos de vida.


## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Condição de vitória:

> O jogador vence e conclui o jogo quando consegue fazer com que seu adversário chegue a 0 pontos de vida.


## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Condição de derrota ou encerramento:

> O jogador perde e finaliza a partida quando tem seus pontos de vida reduzidos a 0 pelo adversário.


## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Dois personagens que serão controlados pelas setas do teclado.

Descrição:

> Cada competidor controlará um personagem na disputa, sendo que um será controlado pelas teclas WASD e o outro pelas setas do teclado. Cada personagem poderá ser movimentado para os lados e poderão desferir golpes.


## Obstáculos, inimigos ou desafios

Exemplo:

> A habilidade "Ultimate" poderá ser utilizada pelo adversário em algum momento da disputa e deve ser evitada.

Descrição:

> Os jogadores podem utilizar uma habilidade especial chamada "Ultimate" que é desbloqueada quando sua barra é totalmente preenchida. Quando a vida de um personagem chega a 20%, ele desbloqueia automaticamente o "Ultimate", capaz de causar grande dano e mudar o rumo da luta.


## Itens, alvos ou objetos de interação

Exemplo:

> O alvo para cada jogador sempre será seu oponente, no qual deve acertar seus golpes.

Descrição:

> Cada jogador deve acertar seus golpes no oponente (alvo) afim de reduzir seus pontos de vida e aumentar o progresso da barra de utilização do "Ultimate" e garantir a vitória.


## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 100 pontos de vida e perde 5 pontos a cada golpe sofrido.
> A barra de progresso do "Ultimate" do jogador começa com 0% e é preenchida a medida em que os golpes são aplicados no oponente.

Descrição:

> Cada jogador inicia o combate com 100 pontos de vida e 0% de progresso para utilização do "Ultimate". A cada golpe aplicado no oponente, o progresso do "Ultimate" aumenta, e a cada golpe sofrido, são perdidos 5 pontos de vida.
> Obs.: Ao atingir 20% da vida de seu personagem, o jogador libera a habilidade "Ultimate".


## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Controles do grupo:

- Tecla A: mover para esquerda (jogador 1)
- Tecla D: mover para direita (jogador 1)
- Tecla W: soco (jogador 1)
- Tecla S: chute (jogador 1)
- Tecla F: Ultimate (jogador 1)
- Seta para esquerda: mover para esquerda (jogador 2)
- Seta para direita: mover para direita (jogador 2)
- Seta para cima: soco (jogador 2)
- Seta para baixo: chute (jogador 2)
- Enter: Ultimate (jogador 2)
- ESC: Menu de Pause


## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Organização planejada:

- `main.py`: responsável por iniciar o jogo e carregar os recursos principais;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/player.py`: implementa a lógica dos personagens, incluindo movimentação, barra de vida e "Ultimate";
- `src/combat.py`: gerencia o sistema de combate, detecção de acertos, aplicação de dano e lista de golpes;
- `src/screens.py`: contém as telas do jogo, como menu inicial, partida e tela de vitória;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.
- `assets/images/`: armazena sprites, cenários e elementos da interface;
- `assets/sounds/`: contém efeitos sonoros e músicas do jogo.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Recursos previstos:

- imagens e designs gratuitos;
- sons gratuitos;
- tutoriais e documentações de referência;


## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Dificuldades previstas:

- Dificuldade 1: design dos personagens, seus movimentos e habilidades;
- Dificuldade 2: organização do código, arquivos e funções;
- Dificuldade 3: testes;
- Dificuldade 4: conflito em validação de ideias;
- Dificuldade 5: gerenciamento de tempo para desenvolvimento.


## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Escopo mínimo:

> A versão mínima do jogo terá dois personagens que serão controlados simultâneamente por dois jogadores utilizando o teclado, sistema de vida, sistema de progresso para habilidade "Ultimate", tela de menu/pause e fim de jogo.


## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Melhorias possíveis (em ordem de prioridade):

- Melhoria 1: Efeitos sonoros e trilha sonora - CONCLUIDO;
- Melhoria 2: Movimentação extra: Defesa/bloqueio - CONCLUIDO;
- Melhoria 3: Movimentação extra: Pular e agachar;
- Melhoria 4: Movimentação extra: Combos de golpes;
- Melhoria 5: Menu de seleção de personagem;
- Melhoria 6: Menu de seleção de mapa;
