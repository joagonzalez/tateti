from player import Player
from board import Board
import random

class Game():
    def __init__(
        self, name_p1, name_p2, type_p1, type_p2, \
        difficulty_p1, difficulty_p2, symbol_p1, symbol_p2
        ):
        self.board = Board(dimension)
        self.plater_1 = Player(name_p1, type_p1, difficulty_p1, symbol_p1)
        self.plater_2 = Player(name_p2, type_p2, difficulty_p2, symbol_p2)

    def __str__(self):
        result = 'Tablero: ' + str(self.board.get_id()) + '\n'
        result += str(self.plater_1) + '\n'
        result += str(self.plater_2)
        return result

    def is_winner(self):
        if self.board.is_tateti():
            return [self.board.is_tateti(), self.board.get_last_play()]
        return 
            self.board.is_tateti()

    def player_begin(self):
        """
        Choose randomly a player in order to start the game
        """

    def movement(self):
        pass


if __name__ == "__main__":
    pass