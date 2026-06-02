# PJBL_BATALHA-NAVAL
Algoritmo python para o jogo batalha naval

Tema : Batalha Naval em Python

Introdução
O objetivo deste trabalho é desenvolver uma versão funcional do jogo Batalha Naval utilizando a linguagem Python. O foco da atividade é praticar conceitos fundamentais de programação, incluindo:

variáveis;
estruturas condicionais;
laços de repetição;
listas e matrizes;
funções;
organização de código;
validação de entradas.
O jogo deverá funcionar em modo texto (terminal/console).

Objetivos do Projeto
O sistema deverá:

implementar as regras básicas do jogo Batalha Naval;
permitir uma partida entre dois jogadores;
controlar turnos;
validar jogadas;
exibir o estado do tabuleiro;
detectar vitória automaticamente.
Requisitos Obrigatórios
Tabuleiro
O jogo deverá possuir:
um tabuleiro para cada jogador;
tamanho mínimo 10 x 10;
As posições devem ser identificadas utilizando coordenadas, por exemplo:
A1, B5, C8, J10
Embarcações
O sistema deverá possuir pelo menos os seguintes navios:
Embarcação	Tamanho
Porta-aviões	5
Encouraçado	4
Cruzador	3
Submarino	3
Destroyer	2
Posicionamento dos Navios
O programa deverá permitir que cada jogador:
escolha a posição inicial do navio;
escolha a orientação:
horizontal;
vertical.
O sistema deve validar:
posições fora do tabuleiro;
sobreposição de navios;
entradas inválidas.
Mecânica do Jogo
Durante a partida:

os jogadores jogam alternadamente;
cada jogador informa uma coordenada de ataque;
o sistema informa:
água;
acerto;
navio destruído.
O sistema também deve impedir:

ataques repetidos;
coordenadas inválidas.
Condição de Vitória
O jogo termina quando todos os navios de um jogador forem destruídos.

Ao final, o sistema deve informar:

jogador vencedor;
quantidade de jogadas realizadas.
Interface
O jogo será executado no terminal.

O tabuleiro deve ser exibido de forma organizada, por exemplo:

  1 2 3 4 5 6 7 8  
A ~ ~ ~ * ~ ~ ~ ~  
B ~ O O O X ~ * ~  
C ~ ~ ~ ~ ~ ~ ~ ~  
Legenda sugerida:

Símbolo	Significado
~	Água
O	Navio
X	Acerto
*	Tiro na água
Estrutura do Código
O projeto deve utilizar funções para organizar o sistema.

Sugestão:

criarTabuleiro()
posicionarNavios()
validarJogada()
realizarAtaque()
verificarVitoria()
imprimirTabuleiro()
 

Funcionalidades Extras (Opcional)
Pontuação adicional poderá ser atribuída para:

interface gráfica;
cores no terminal;
posicionamento automático;
efeitos sonoros;
salvar/carregar partidas;
diferentes tamanhos de tabuleiro.
