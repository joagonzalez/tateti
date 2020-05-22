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
        type = self.get_type()
        difficulty = self.get_difficulty()
        symbol = self.get_symbol()
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
            try:
                x = int(input("Select a column for your move: "))
                y = int(input("Select a row for your move: "))
                if x < 0 or x > 2 or y < 0 or y > 2:
                    print('Select a valid position!\n')
                else:
                    movement = [x, y]
                    _ok = board.update_board(movement, self.get_symbol())
                    if not _ok:
                        print("Position selected was already chosen.\nTry again!")    
            except Exception as e:
                print('You have entered an invalid option, try again!')    

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

    def get_difficulty(self):
        """
        Returns player difficulty if computer type
        """
        return self.difficulties[self.difficulty]

    def get_type(self):
        """
        Returns player type
        """
        return self.types[self.type]

    def change_name(self, name):
        """
        Allows player name modification
        """
        self.name = name

if __name__ == "__main__":
    # tests
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