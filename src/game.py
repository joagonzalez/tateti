from player import Player
from board import Board
import random

class Game():
    def __init__(
        self, name_p1, name_p2, type_p1, type_p2, \
        difficulty_p1, difficulty_p2, symbol_p1, symbol_p2, dimension=3
        ):
        self.board = Board(dimension)
        self.player_1 = Player(name_p1, type_p1, difficulty_p1, symbol_p1)
        self.player_2 = Player(name_p2, type_p2, difficulty_p2, symbol_p2)

    def __str__(self):
        result = 'Tablero: ' + str(self.board.get_id()) + '\n'
        result += str(self.player_1) + '\n'
        result += str(self.player_2)
        return result

    def is_winner(self):
        """
        Interface with board class to check if last movement made tateti
        """
        if self.board.is_tateti():
            return [self.board.is_tateti(), self.board.get_last_play()]
        else: 
            return self.board.is_tateti()

    def player_begin(self):
        """
        Choose randomly a player in order to start the game
        """
        players = [self.player_1.get_name(), self.player_2.get_name()]
        return random.choice(players)

    def movement(self, player_name):
        """
        Interface with player class to make a movement within the board
        """
        if self.player_1.get_name() == player_name:
            current_player = self.player_1
        else:
            current_player = self.player_2

        current_player.movement(self.board)

if __name__ == "__main__":
    game = Game('Joaquin', 'Morita', 0, 1, 0, 1, 0, 1)

    print(game)