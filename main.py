# Importar Classe
from sudokusolver import SudokuSolver

# Array com a tabela do Sudoku
board = [[8, 0, 0, 2, 0, 6, 0, 7, 3],
         [0, 0, 6, 0, 4, 0, 0, 0, 0],
         [0, 0, 5, 0, 0, 0, 9, 0, 0],
         [0, 1, 0, 4, 0, 0, 0, 6, 0],
         [0, 0, 7, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 1, 0, 7],
         [4, 7, 9, 0, 3, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 8, 7, 0, 0, 2, 1, 0]]

# Inicializar classe
game = SudokuSolver(board)

# Mostrar o resultado final
isSolved = game.solve(0, 0)

if isSolved:
    game.print_board()
else:
    print("Não foi possível resolver este Sudoku")

