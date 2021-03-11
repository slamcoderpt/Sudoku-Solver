class SudokuSolver:

    # Tamanho do tabuleiro
    BOARD_SIZE = 9
    SQUARE_SIZE = 3

    # Construtor da classe
    def __init__(self, board):
        self.board = board

    # Verificar se numero (num) existe na linha (line)
    def check_line(self, num, line):
        return num in self.board[line]

    # Verificar se numero (num) existe na coluna (column)
    def check_column(self, num, column):
        for y in range(self.BOARD_SIZE):
            if num == self.board[y][column]:
                return True

        return False

    # Verificar se numero (num) existe no quadrado (square)
    def check_square(self, num, square_x, square_y):
        for y in range(self.SQUARE_SIZE):
            for x in range(self.SQUARE_SIZE):
                if self.board[square_y * self.SQUARE_SIZE + y][square_x * self.SQUARE_SIZE + x] == num:
                    return True

        return False

    # Função principal que faz a resolução do sudoku
    def solve(self, line, column):
        # Se True finalizamos o tabuleiro
        if line == self.BOARD_SIZE - 1  and column == self.BOARD_SIZE:
            return True
        
        # Se chegamos à ultima coluna vamos para a próxima linha
        if column == self.BOARD_SIZE:
            column = 0
            line += 1

        # Verificar se posição atual já tem posição, caso tenha avança para a proxima posição
        if(self.board[line][column] > 0):
            return self.solve(line, column + 1)

        # Vamos lá testar números
        for number in range(10):
            # Verificar se podemos colocar o numero atual na posição do tabuleiro
            if not self.check_line(number, line) and not self.check_column(number, column) and not self.check_square(number, int(column / self.SQUARE_SIZE), int(line / self.SQUARE_SIZE)):
                self.board[line][column] = number
                if self.solve(line, column + 1):
                    return True

            self.board[line][column] = 0
        return False

    def print_board(self):
        for y in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                print(self.board[y][x], end = " ")
            print()

    def get_board(self):
        return self.board
        


                    

