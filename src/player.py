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
        type = types[self.type]
        difficulty = difficulties[self.difficulty]
        symbol = symbols[self.symbol]
        if self.type == 0:
            result = "{} - {} - {}".format(self.name, type, symbol)
        else:
            result = "{} - {} - {} - {}".format(self.name, type, difficulty, symbol)
        return result

    def movement(self, board):
        position = input("Ingrese su jugada: ")
        board.update_board(position)

    def get_symbol(self):
        return symbols[self.symbol]

    def get_name(self):
        return self.name

    def change_name(self, name):
        self.name = name

if __name__ = "__main__":
    pass