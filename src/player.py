from board import Board

class Player():
    types = ['human', 'computer']
    difficulties = [0, 1, 2]
    symbols = ["X", "O"]

    def __init__(self, name, type, difficulty, symbol):
        self.name = name
        self.type = type
        self.difficulty = difficulty
        self.symbol = symbol
    
    def __str__(self):
        type = self.types[self.type]
        difficulty = self.difficulties[self.difficulty]
        symbol = self.symbols[self.symbol]
        if self.type == 0:
            result = "Player: {} - Type: {} - Symbol: {}".format(self.name, type, symbol)
        else:
            result = "Player: {} - Difficulty: {} - Type: {} - Symbol: {}".format(self.name, difficulty, type, symbol)
        return result

    def movement(self, board):
        """
        Insert symbol in the possition chosen by player
        """
        _ok = False
        while not _ok:
            x = input("Ingrese columna de su jugada: ")
            y = input("Ingrese fila de su jugada: ")
            if x < 0 or x > 2 or y < 0 or y > 2:
                print('Ingrese un casillero valido!\n')
            else:
                _ok = True
        
        movement = [int(y), int(x)]
        board.update_board(movement, self.symbols[self.symbol])

    def get_symbol(self):
        """
        Returns player symbol
        """
        return self.symbols[self.symbol]

    def get_name(self):
        """
        Returns player name
        """
        return self.name

    def change_name(self, name):
        """
        Allows player name modification
        """
        self.name = name

if __name__ == "__main__":
    dimension = 3
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
    print(board)
    player_1 = Player('Joaquin', 0, 0, 0)
    player_2 = Player('Xano', 1, 1, 1)
    print(player_1)
    print(player_2)
    player_1.movement(board)
    print(board)
    print(board.is_tateti())