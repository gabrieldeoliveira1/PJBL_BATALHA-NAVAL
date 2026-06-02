#nota: instale o rich caso você não tenha (usei para uns frufruzinho já que no primeiro PJBL não tinha nada e perdemos nota kkkkk)
import os
from time import sleep 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_tabuleiro():
    tabuleiro = []

    for numero_linha in range(10):
        linha = ["~", "~", "~", "~", "~", "~", "~", "~", "~", "~"] 
        tabuleiro.append(linha)
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    
    tabela = Table(title="[bold yellow]RADAR NAVAL[/bold yellow]", show_header=True, header_style="cyan")
    tabela.add_column(" ")

    for i in range(1,11):
        tabela.add_column(str(i), justify="center")
    
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for i in range(10):
        linha_atual = tabuleiro[i]
        linha_formatada = []
        
        for item in linha_atual:
            if item == "~":
                linha_formatada.append("[blue]~[/blue]")
            elif item == "X":
                linha_formatada.append("[bold red]X[/bold red]")
            else:
                linha_formatada.append(item)

        tabela.add_row(f"[bold yellow]{letras[i]}[/bold yellow]", *linha_formatada)
    
    painel = Panel(tabela, expand=False, border_style="cyan")
    console.print(painel)

def converter_coordernada(jogada):
    letra = jogada[0].upper() #pega a letra estando maísculo ou minúsculo
    numero = jogada[1:] #pega os números após a letra

    letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    linha_escolhida = letras_validas.index(letra)
    coluna_escolhida = int(numero) - 1

    return linha_escolhida, coluna_escolhida

#Validação caso o usuário clique alguma letra além de J ou número maior que 10, ou apenas letras e apenas números (como pode o usuário ser tão burro!)
def validar_jogada(alvo):
    
    if len(alvo) < 2 or len(alvo) > 3:
        console.print("\n[bold red][ERROR][/bold red] Coordenada incompleta! Digite uma letra e um número (Exemplo: A1, B2, C3...)")
        input("Pressione ENTER para inserir coordenada novamente...")
        return False

    letra_digitada = alvo[0].upper()
    numero_digitado = alvo[1:]
    letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    if letra_digitada not in letras_validas:
        console.print(f"\n[bold red][ERROR][/bold red] Não é uma posição válida! Use letras de A até J.")
        input("Pressione ENTER para inserir coordenada novamente...")
        return False

    if not numero_digitado.isdigit():
        console.print(f"\n[bold red][ERROR][/bold red] Não é uma posição válida! Use apenas números.")
        input("Pressione ENTER para inserir coordenada novamente...")
        return False

    if int(numero_digitado) < 1 or int(numero_digitado) > 10:
        console.print(f"\n[bold red][ERROR][/bold red] Não é uma posição válida! Use apenas números de 1 a 10.")
        input("Pressione ENTER para inserir coordenada novamente...")
        return False

    return True


print("------- BATALHA NAVAL -------")
print("\n");

tabuleiro = criar_tabuleiro()

while True:
    limpar_tela()
    imprimir_tabuleiro(tabuleiro)
    console.print("\nDigite [bold yellow]SAIR[/bold yellow] para encerrar os sistemas.")

    alvo = input("\nCapitão, digite a coordenada de ataque: ")

    if alvo.lower() == "sair":
        console.print("[bold yellow]Encerrando os sistemas... Até a próxima, Capitão![/bold yellow]")
        break;
    
    if not validar_jogada(alvo):
        continue

    linha_alvo, coluna_alvo = converter_coordernada(alvo)

    if tabuleiro[linha_alvo][coluna_alvo] == "X":
        console.print("\n[bold yellow][WARNING][/bold yellow] Capitão, nós já atiramos nesta coordenada! Desperdício de munição. (perdeu malandro kkkkkk)\n")
        sleep(3) #deixar a mensagem de fogo aparecendo por um tempinho a mais antes de limpar a tela
    else:
        tabuleiro[linha_alvo][coluna_alvo] = "X"
        console.print("\n[bold green] ---- Fogo! Atualizando o radar... ----[/bold green]\n")
        sleep(1.5) 
#fazer uma espécie de switch que pergunte onde e qual orientação da embarcação