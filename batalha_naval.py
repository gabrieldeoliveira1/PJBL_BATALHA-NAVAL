def criar_tabuleiro():
    tabuleiro = []

    for numero_linha in range(10):
        linha = ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"] 
        tabuleiro.append(linha)
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    print("  1 2 3 4 5 6 7 8 9 10")
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for i in range(10):
        letra = letras[i]
        linha_atual = tabuleiro[i]

        linha_texto = " ".join(linha_atual)
        print(letra + " " + linha_texto)

def converter_coordernada(jogada):
    letra = jogada[0].upper() #pega a letra estando maísculo ou minúsculo
    numero = jogada[1:] #pega os números após a letra

    letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    linha_escolhida = letras_validas.index(letra)
    coluna_escolhida = int(numero) - 1

    return linha_escolhida, coluna_escolhida


print("------- BATALHA NAVAL -------")
print("\n");

tabuleiro = criar_tabuleiro()
imprimir_tabuleiro(tabuleiro)

alvo = input("\nCapitão, digite a coordenada de ataque: ")
linha_alvo, coluna_alvo = converter_coordernada(alvo)
tabuleiro[linha_alvo][coluna_alvo] = X