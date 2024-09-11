# Jogo da Forca

Este é um simples jogo da forca que roda no terminal, onde o jogador tenta adivinhar uma palavra secreta, letra por letra. O jogo utiliza as entradas do jogador e verifica a validade das tentativas.

## Funcionalidades
- O jogo permite que o jogador insira letras para adivinhar uma palavra.
- A palavra secreta é inserida de forma oculta para evitar que outros jogadores vejam.
- A cada erro, o número de tentativas restantes é reduzido.
- O jogo exibe a palavra com as letras já adivinhadas e placeholders `_` para as letras ainda não reveladas.
- O jogador tem 6 tentativas para adivinhar a palavra corretamente antes de perder o jogo.

## Requisitos
- O módulo `getpass` é usado para inserir a palavra secreta de forma segura.
- A entrada do jogador deve ser uma única letra alfabética.

## Fluxo do Jogo
1. A palavra secreta é inserida pelo jogador que não participa das tentativas.
2. O jogador começa com 6 tentativas e tenta adivinhar a palavra secreta.
3. O jogo revela as letras corretas e oculta as não adivinhadas.
4. Se o jogador errar, perde uma tentativa. Caso acerte, a letra é revelada.
5. O jogo termina quando a palavra é completamente adivinhada ou quando o número de tentativas chega a 0.
