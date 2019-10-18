import os
import class_sudoku as cs

game = cs.Sudoku_game()


def inserir(linha,coluna):
    try:
        numero = int(input("Posição [%d,%d]: " % (linha + 1,coluna + 1)))
        if numero < 0 or numero > 9:
            raise Exception
        else:
            tabuleiro[linha][coluna] = numero
    except Exception as e:
        print("Insira um valor inteiro entre 1 e 9")
        inserir(linha,coluna)

tabuleiro =  [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]

print("Solucionador de Sudoku 3000")
while True:
    print("O que deseja fazer:")
    print("1. Inserir um novo tabuleiro")
    print("2. Usar um tabuleiro previamente definido")
    print("3. Solucionar!")
    print("4. Sair")

    chose = int(input())

    if chose == 1:
        print("Insira o tabuleiro que deseja solucionar, colocando 0 onde não souber:")

        for linha in range(0,9):
            for coluna in range(0,9):
                game._print_tabuleiro(tabuleiro)
                inserir(linha,coluna)
                os.system("clear")
        #Envia o tabuleiro atual para game
        game._tabuleiro = tabuleiro

    elif chose == 2:
        #Tabuleiros testados e já definidos em arquivos de texto
        print("Qual tabuleiro deseja utilizar (escolha entre 1 e 3): ")
        chose_tabuleiro = int(input())
        if chose_tabuleiro == 1:
            tabuleiro = game.novo_tabuleiro("tabuleiro")
            game._print_tabuleiro(tabuleiro)
        elif chose_tabuleiro == 2:
            tabuleiro = game.novo_tabuleiro("tabuleiro2")
            game._print_tabuleiro(tabuleiro)
        elif chose_tabuleiro == 3:
            tabuleiro = game.novo_tabuleiro("tabuleiro3")
            game._print_tabuleiro(tabuleiro)
        else:
            print("Insira um valor válido!")

    elif chose == 3:
        try:
            game.main()
        except IndexError:
            print("Selecione primeiramente um tabuleiro válido de sudoku")

    elif chose == 4:
        break
    else:
        print("Insira um valor válido")
