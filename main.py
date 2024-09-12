# import getpass
# # def clear():
# #     # Detecta o sistema operacional e executa o comando correto
# #     if os.name == 'nt':  # Se for Windows
# #         os.system('cls')
# #     else:  # Se for Linux ou macOS
# #         os.system('clear')
#
# palavra_secreta = getpass.getpass('Digite a palavra para a forca ') # Palavra a ser adivinhada
# palavra_secreta = palavra_secreta.lower() # Convertendo a palavra para minusculo pelo case sensitive.
# def jogar_forca():
#     letras_adivinhadas = ["_" for _ in palavra_secreta] # Array com for para placeholder das letras
#     tentativas = 6  # Número de tentativas
#     letras_erradas = [] # Array das letras erradas
#
#     print("Bem-vindo ao Jogo da Forca")
#
#     while tentativas > 0 and "_" in letras_adivinhadas:
#         print("-----------------------------")
#         print(f"Palavra secreta: " + " ".join(letras_adivinhadas))
#         print(f"\nTentativas restantes: {tentativas}")
#         print(f"Letras erradas: {', '.join(letras_erradas)}")
#
#         # Entrada do jogador
#         letra = input("Digite uma letra: ").lower()
#
#         # Checagem da entrada para evitar mais de uma letra por ver e caractéres não alfanuméricos
#         if len(letra) != 1 or not letra.isalpha():
#             print("Por favor, digite apenas uma letra.")
#             continue
#
#         # Checagem da entrada para evitar letras repetidas
#         if letra in letras_adivinhadas or letra in letras_erradas:
#             print("Você já tentou essa letra.")
#             continue
#
#         # Atualização do display com a letra
#         print("\n"*100)
#         if letra in palavra_secreta:
#             for i, l in enumerate(palavra_secreta):
#                 if l == letra:
#                     letras_adivinhadas[i] = letra
#         else:
#             # Se errar ele tira uma das tentativas e coloca mostra na tela
#             tentativas -= 1
#             letras_erradas.append(letra)
#
#         # Checa se não tem mais lugares vazios no display.
#         if "_" not in letras_adivinhadas:
#             print("\nParabéns! Você adivinhou a palavra!")
#         else:
#             print(f"\nVocê perdeu! A palavra era {palavra_secreta}.")
#
# jogar_forca()


import getpass

# Função para receber a palavra secreta
def palavra_secreta():
    palavra = getpass.getpass('Digite a palavra para a forca: ').lower()
    return palavra

# Função para criar o estado inicial do jogo (palavra oculta)
def iniciar_jogo(palavra):
    letras_adivinhadas = ["_" for _ in palavra]
    return letras_adivinhadas

# Função para exibir o estado atual do jogo
def exibir_estado(letras_adivinhadas, tentativas, letras_erradas):
    print("-----------------------------")
    print(f"Palavra secreta: " + " ".join(letras_adivinhadas))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")

# Função para validar a entrada do jogador
def validar_letra(letra, letras_adivinhadas, letras_erradas):
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.")
        return False
    if letra in letras_adivinhadas or letra in letras_erradas:
        print("Você já tentou essa letra.")
        return False
    return True

# Função para atualizar o estado do jogo
def atualizar_jogo(letra, palavra_secreta, letras_adivinhadas, letras_erradas, tentativas):
    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_adivinhadas[i] = letra
    else:
        tentativas -= 1
        letras_erradas.append(letra)
    return tentativas

# Função main do programa
def jogar_forca():
    palavra = palavra_secreta()
    letras_adivinhadas = iniciar_jogo(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca")

    while tentativas > 0 and "_" in letras_adivinhadas:
        exibir_estado(letras_adivinhadas, tentativas, letras_erradas)

        letra = input("Digite uma letra: ").lower()

        if not validar_letra(letra, letras_adivinhadas, letras_erradas):
            continue

        tentativas = atualizar_jogo(letra, palavra, letras_adivinhadas, letras_erradas, tentativas)

    if "_" not in letras_adivinhadas:
        print("\nParabéns! Você adivinhou a palavra!")
    else:
        print(f"\nVocê perdeu! A palavra era {palavra}.")

jogar_forca()
