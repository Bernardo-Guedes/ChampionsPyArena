# Testes

Esta pasta contem testes automatizados do projeto.

## Arquivos

- `test_logica.py`: Testes de ataque e chute: início da ação, acerto, erro e bloqueio.
- `test_dano.py`: Testes de recebimento de dano e bloqueio de dano.
- `test_vida_negativa.py`: Garante que a vida do personagem não fica negativa.
- `test_ultimate.py`: Testes do ultimate: limite máximo, acerto, erro e bloqueio.
- `test_colisao.py`: Verifica colisão verdadeira entre dois objetos.
- `test_colisao_false.py`: Verifica colisão falsa entre objetos distantes.

## Como executar

```bash
python -m pytest
```


