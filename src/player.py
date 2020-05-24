from board import Board
import random
import time

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

    def select_random_position(self):
        """
        Computer type players will use this method to
        randomly choose a position to play. Difficulty type 0
        """
        x = random.randint(0,2)
        y = random.randint(0,2)
        return [x, y]

    def movement(self, board):
        """
        Insert symbol in the possition chosen by player
        """
        _ok = False
        while not _ok:
            try:
                if self.type == 0:
                    x = int(input("Select a column for your move: "))
                    y = int(input("Select a row for your move: "))
                else:
                    x,y = self.select_random_position()
                    if board.is_position_available(y,x):
                        # human experience coefficient
                        print("espero!")
                        time.sleep(random.uniform(0.3,2))  
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
    print("Player class!")