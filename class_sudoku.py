class Sudoku_game:
    """Capaz de determinar a solução para tabuleiros de sudoku

    COMO UTILIZAR:
    1. Crie um arquivo .csv com o seu tabuleiro sudoku, colocando 0 nas posições desconhecidas
    2. Abra o arquivo usando novo_tabuleiro("NOME_DO_ARQUIVO.csv")
    3. Execute main()
    4. O resultado é escrito em solução.txt"""

    def __init__(self):
        self._tabuleiro = [[],[],[],[],[],[],[],[],[]]
        self._valores_fixos = [[],[],[],[],[],[],[],[],[]]

    def novo_tabuleiro(self,nome):
        """Lê um arquivo de texto que contém o tabuleiro de sudoku com os valores
        separados por vírgula"""

        if type(nome) not in [str]:
            raise ValueError("Insira um nome de arquivo válido")
        try:
            arquivo = open(nome,"r")
            for linha in range(0,9):
                self._tabuleiro[linha] = arquivo.readline().split(",")
                for i in range(0,9):
                    self._tabuleiro[linha][i] = int(self._tabuleiro[linha][i])

            arquivo.close()
            return self._tabuleiro

        except FileNotFoundError:
            print("O arquivo %s não existe" % nome)

    def _print_tabuleiro(self,tabuleiro):
        """Recebe uma lista contendo o tabuleiro e exibe na tela em uma forma mais agradável, usando
         caracteres para formar o tabuleiro"""
        for linha in range(0,9):
            if linha % 3 == 0:
                print("===========##=========##===========")
            print("## %d| %d |%d ## %d| %d |%d ## %d| %d |%d ##" % (tabuleiro[linha][0],tabuleiro[linha][1],tabuleiro[linha][2],tabuleiro[linha][3],tabuleiro[linha][4],tabuleiro[linha][5],tabuleiro[linha][6],tabuleiro[linha][7],tabuleiro[linha][8]))
        print("===========##=========##===========")

    def _verifica(self, lin_Numero_Verificar,col_Numero_Verificar,verificando):
        """Realiza a verificação se um número 'verificando' pode ser colocado em uma posição 'lin_Numero_Verificar' e 'col_Numero_Verificar'"""

        # Verifica se encontra um número igual na linha
        for lin in range(0,9):
            if self._tabuleiro[lin][col_Numero_Verificar] == verificando and lin != lin_Numero_Verificar:
                return False
        # Verifica se encontra um número igual na coluna
        for col in range(0,9):
            if self._tabuleiro[lin_Numero_Verificar][col] == verificando and col != col_Numero_Verificar:
                return False

        # Verifica se encontra um número igual no bloco
        fixLin = lin_Numero_Verificar % 3; # Estas correções são necessárias para que seja possível determinar o bloco que aquele valor pertence
        fixCol = col_Numero_Verificar % 3;
        # O bloco começa na posição dada no argumento da função menos a correção e termina 3 posições seguintes
        for lin_Bloco in range(lin_Numero_Verificar - fixLin, (lin_Numero_Verificar - fixLin) + 3):
            for col_Bloco in range(col_Numero_Verificar - fixCol, (col_Numero_Verificar - fixCol) + 3):
                if self._tabuleiro[lin_Bloco][col_Bloco] == verificando and lin_Bloco != lin_Numero_Verificar and col_Bloco != col_Numero_Verificar:
                    return False
        return True


    def _define_valores_fixos(self):
        """Determina com base no tabuleiro quais valores podem ser alterados
        e quais são fixos"""

        for linha in range(0,9):
            self._valores_fixos[linha].clear()
            for coluna in range(0,9):
                self._valores_fixos[linha].append(True if self._tabuleiro[linha][coluna] != 0 else False)

    def _escreve_tabuleiro_resolvido(self):
        """Cria um arquivo 'solucao.txt' que contém uma lista com a solução para
        o tabuleiro de sudoku"""

        print("Gravando solução...")
        with open("solucao.txt","w") as fileOut:
            for linha in range(0,9):
                for coluna in range(0,9):
                    fileOut.write("%d" % self._tabuleiro[linha][coluna])
                    if coluna != 8:
                        fileOut.write(",")
                fileOut.write("\n")

    def _resolve(self, linha=0, coluna=0):
        """Realiza a solução do tabuleiro de sudoku.
        Recebe um valor para linha e coluna, sendo por padrão 0"""
    #    print("Resolvendo linha %d coluna %d" % (linha,coluna))
        if linha == 9:
            self._escreve_tabuleiro_resolvido()
            self._print_tabuleiro(self._tabuleiro)
            return True
        elif not self._valores_fixos[linha][coluna]:
            for numeroTentativa in range(1,10):
                if self._verifica(linha,coluna,numeroTentativa):
                    numeroAnterior = self._tabuleiro[linha][coluna]
                    self._tabuleiro[linha][coluna] = numeroTentativa
                    if coluna == 8:
                        # Troca de linha ao chegar ao final da coluna
                        self._resolve(linha+1,0)
                    else:
                        # Troca de coluna se ainda não chegou no final da linha
                        self._resolve(linha,coluna+1)
                    self._tabuleiro[linha][coluna] = numeroAnterior
        elif coluna == 8:
            # Troca de linha ao chegar ao final da coluna
            self._resolve(linha+1,0)
        else:
            # Troca de coluna se ainda não chegou no final da linha
            self._resolve(linha,coluna+1)

    def __debug(self):
        print("Exibindo tabuleiro:")
        for linha in self._tabuleiro:
            print(linha)

        print("Exibindo valores fixos:")
        for linha in self._valores_fixos:
            print(linha)

    def main(self):
        """Realiza os procedimentos necessários para resolver o sudoku. É necessário
        definir um tabuleiro anteriormente"""
        self._define_valores_fixos()
        self._resolve(0,0)
