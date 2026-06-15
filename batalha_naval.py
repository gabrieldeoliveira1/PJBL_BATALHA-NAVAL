#nota: instale o rich caso você não tenha (usei para uns frufruzinho já que no primeiro PJBL não tinha nada e perdemos nota kkkkk)
import os
import random
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

def imprimir_tabuleiro(tabuleiro, ocultar_navios=False):
    
    tabela = Table(title="[bold yellow]RADAR NAVAL[/bold yellow]", show_header=True, header_style="cyan")
    tabela.add_column(" ")

    for i in range(1,11):
        tabela.add_column(str(i), justify="center")
    
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for i in range(10):
        linha_atual = tabuleiro[i]
        linha_formatada = []
        
        for item in linha_atual:

            #oculta pro adversario
            if ocultar_navios and item == "O":
                item = "~"

            if item == "~":
                linha_formatada.append("[blue]~[/blue]")
            elif item == "X":
                linha_formatada.append("[bold red]X[/bold red]")
            elif item == "O":
                linha_formatada.append("[green]O[/green]")
            elif item == "*":
                linha_formatada.append("[bold cyan]*[/bold cyan]")
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

navios = [
    {"nome": "Porta-aviões", "tamanho": 5},
    {"nome": "Encouraçado",  "tamanho": 4},
    {"nome": "Cruzador",     "tamanho": 3},
    {"nome": "Submarino",    "tamanho": 3},
    {"nome": "Destroyer",    "tamanho": 2},
]

#FALTA MUDAR A LOGICA PARA NAO SER RANDOMICO E VER SE DA PRA COLOCAR TODOS OS NAVIOS
def posicionar_navios(tabuleiro, nome_jogador):
    mapa_navios = {}

    for navio in navios:
        tamanho = navio["tamanho"]
        nome = navio["nome"]
        posicionado = False

        while not posicionado:
            console.print(f"\n[bold cyan]Almirante {nome_jogador}, prepare a sua frota![/bold cyan]")
            console.print(f"\nPosicionando: [bold yellow]{nome}[/bold yellow] que ocupa [bold red]{tamanho}[/bold red] espaços.")

            imprimir_tabuleiro(tabuleiro, ocultar_navios=False)

            orientacao = input("Digite a orientação H para Horizontal e V para Vertical: ")
            if orientacao not in ["H", "V"]:
                console.print("[bold red]ERROR[/bold red], digite apenas H ou V")
                sleep(2)
                continue

            alvo = input(f"Digite a coordenada inicial para o {nome} (Ex: A1): ").strip()
            
            #aproveitar a funcao da coordenada pra jogada do usuario

            if not validar_jogada(alvo):
                continue
            
            linha, coluna = converter_coordernada(alvo)

            if orientacao == "H" and (coluna + tamanho) > 10:
                console.print(f"[bold red]ERROR[/bold red] O {nome} não pode ficar nesta posição!")
                sleep(3)
                continue
            elif orientacao == "V" and (linha + tamanho) > 10:
                console.print(f"[bold red]ERROR[/bold red] O {nome} não pode ficar nesta posição!")
                sleep(3)
                continue
                
            celulas = []

            for k in range(tamanho):
                if orientacao == "H":
                    celulas.append((linha, coluna + k))
                else:
                    celulas.append((linha + k, coluna))

            
            todas_livres = True
            for l, c in celulas:
                if tabuleiro[l][c] != "~":
                    todas_livres = False
                    break
            
            if not todas_livres:
                console.print("\n[bold red][ERROR][/bold red] Já existe um navio nessa localização. Escolha outra coordenada.")
                sleep(3)
                continue

            for l, c in celulas:
                tabuleiro[l][c] = "O" 
            mapa_navios[navio["nome"]] = celulas 
            posicionado = True 

    return mapa_navios





def verificar_vitoria(tabuleiro_alvo):
    
    for linha in tabuleiro_alvo:
        if "O" in linha:
            return False
    return True


def realizar_ataque(tabuleiro_alvo, mapa_navios_alvo, linha, coluna):
    celula = tabuleiro_alvo[linha][coluna]

    if celula == "~":
        tabuleiro_alvo[linha][coluna] = "*"
        return "agua"

    if celula == "O":
        tabuleiro_alvo[linha][coluna] = "X"

    for nome_navio, celulas in mapa_navios_alvo.items():
            if (linha, coluna) in celulas:
                todas_acertadas = True
                for l, c in celulas:
                    if tabuleiro_alvo[l][c] != "X":
                        todas_acertadas = False
                        break
                if todas_acertadas:
                    return "destruido:" + nome_navio
                return "acerto"
 
    return "repetido" 


limpar_tela()
console.print(
    Panel(
        "[bold cyan]⚓  BATALHA NAVAL  ⚓[/bold cyan]\n\n"
        "Os navios serão posicionados automaticamente.\n"
        "Quem afundar todos os navios adversários primeiro vence.",
        border_style="cyan",
        expand=False,
    )
)
sleep(1)

nome1 = input("Nome do jogador 1: ").strip() or "Jogador 1" #caso o usuario nao digite nada
nome2 = input("Nome do jogador 2: ").strip() or "Jogador 2"



limpar_tela()
input(f"\n[AVISO] É a vez de {nome1} posicionar a frota. {nome2}, não olhe a tela! (Pressione ENTER)")
tabuleiro1 = criar_tabuleiro()
mapa_navios1 = posicionar_navios(tabuleiro1, nome1) 


limpar_tela()
console.print(f"\n[bold green]Frota de {nome1} posicionada com sucesso![/bold green]")
input(f"Passando o comando... Chame {nome2} e pressione ENTER para continuar.")


limpar_tela()
input(f"\n[AVISO] É a vez de {nome2} posicionar a frota. {nome1}, vire de costas! (Pressione ENTER)")
tabuleiro2 = criar_tabuleiro()
mapa_navios2 = posicionar_navios(tabuleiro2, nome2)


limpar_tela()
console.print("\n[bold red] TODAS AS FROTAS A POSTOS! PREPARAR PARA O COMBATE! [/bold red]")
sleep(2)

turno_atual = 1
jogadas1 = 0
jogadas2 = 0


while True:
    limpar_tela()


    if turno_atual == 1:
        nome_atual = nome1
        tabuleiro_proprio = tabuleiro1
        tabuleiro_alvo = tabuleiro2
        mapa_alvo = mapa_navios2
    else: 
        nome_atual = nome2
        tabuleiro_proprio = tabuleiro2
        tabuleiro_alvo = tabuleiro1
        mapa_alvo = mapa_navios1

    
    print(f"\n----- Turno do Jogador {nome_atual} -----")
    console.print("\n[bold cyan]Seu tabuleiro: [/bold cyan]")
    imprimir_tabuleiro(tabuleiro_proprio, ocultar_navios=False)
    console.print("\n[bold red]Tabuleiro adversário: [/bold red]")
    imprimir_tabuleiro(tabuleiro_alvo, ocultar_navios=True)

    alvo = input(f"\nCapitão {nome_atual}, digite a coordenada de ataque: ")
    
    console.print("\nDigite [bold yellow]SAIR[/bold yellow] para encerrar os sistemas.")

    if alvo.lower() == "sair":
        console.print("[bold yellow]Encerrando os sistemas... Até a próxima, Capitão![/bold yellow]")
        break;

    if not validar_jogada(alvo):
        continue

    linha_alvo, coluna_alvo = converter_coordernada(alvo)


    if tabuleiro_alvo[linha_alvo][coluna_alvo] == "X" or tabuleiro_alvo[linha_alvo][coluna_alvo] == "*":
        console.print("\n[bold yellow][WARNING][/bold yellow] Capitão, nós já atiramos nesta coordenada! Desperdício de munição. (perdeu malandro kkkkkk)\n")
        sleep(3)
        continue

    resultado = realizar_ataque(tabuleiro_alvo, mapa_alvo, linha_alvo, coluna_alvo)

    if turno_atual == 1:
        jogadas1 += 1
    else:
        jogadas2 += 1


    if resultado == "agua":
        print("\n ---- Água! O tiro caiu no mar. ----\n")
    elif resultado == "acerto":
        print("\n ---- Acerto! Você atingiu um navio inimigo! ----\n")
    elif resultado.startswith("destruido:"):
        nome_navio = resultado.split(":")[1]
        print(f"\n ---- NAVIO DESTRUÍDO! O {nome_navio} adversário afundou! ----\n")

    sleep(2)
    

    if verificar_vitoria(tabuleiro_alvo):
        limpar_tela()

        if turno_atual == 1:
            perdedor = nome2
        else:
            perdedor = nome1

        console.print(f"\n🏆 [bold yellow]VITÓRIA DE {nome_atual.upper()}![/bold yellow] 🏆")
        print(f"\n{nome_atual} afundou todos os navios de {perdedor}!")
        console.print(f"\nJogadas de {nome1}: [bold red]{jogadas1}[/bold red]")
        console.print(f"Jogadas de {nome2}: [bold red]{jogadas2}[/bold red]\n")
        break

    limpar_tela()
    console.print(f"\n[bold cyan]Fim do turno do Capitão {nome_atual}![/bold cyan]")

    # Alterna o turno
    if turno_atual == 1:
        turno_atual = 2
        proximo_jogador = nome2
    else:
        turno_atual = 1
        proximo_jogador = nome1

    input(f"\nPassando o comando... Chame o Almirante {proximo_jogador} e pressione ENTER para iniciar o próximo turno!")
    

