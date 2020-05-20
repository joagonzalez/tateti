import sys
import uuid
class Board():
    def __init__(self, dimension):
        self.id = uuid.uuid4()
        self.dimension = dimension
        self.board = [[" " for i in range(dimension)] for i in range(dimension)]

    def __str__(self):
        result = ''
        i = 0
        j = 0
        for row in self.board:
            for column in row:
                if i == len(column) - 1 or i == 0 :
                    result += ' ' + column
                else: 
                    result += ' | ' + column
                i += 1
            j += 1
            if j != len(row):
                result += '\n-----------\n'
            else:
                result += '\n'
            i = 0
        return result

    def is_tateti(self):
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ' or \
           self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ' or \
           self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ' or \
           self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ' or \
           self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][0] != ' ' or \
           self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ' or \
           self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ' or \
           self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True
        else:
            return False

    def update_board(self, position, symbol):
        y = position[0]
        x = position[1]
        self.board[x][y] = symbol 

    def get_board(self):
        return self.board

    def get_id(self):
        return self.id

    def get_dimension(self):
        return self.dimension

if __name__ == "__main__":
    dimension = int(sys.argv[1])
    board = Board(dimension)
    print("Imprimimos tablero vacio: ")
    print(board)
    board.update_board([0, 2], 'X')
    board.update_board([0, 0], 'O')
    board.update_board([1, 2], 'X')
    board.update_board([2, 2], 'X')
    board.update_board([1, 0], 'X')
    board.update_board([2, 0], 'O')
    board.update_board([0, 1], 'O')
    board.update_board([1, 1], 'X')
    board.update_board([2, 1], 'X')
    if dimension == 4:
        board.update_board([3, 3], 'X')
    print("Imprimimos tablero con contenido: ")
    print(board)
    print(board.is_tateti())
    print(board.get_board())
    print(board.get_id())
    print(board.get_dimension())