from player import Player
from board import Board
from library import new_player as new_player, play_again as play_again
import random

class Game():
    def __init__(
        self, name_p1='', name_p2='', type_p1=0, type_p2=0, \
        difficulty_p1=0, difficulty_p2=0, symbol_p1=0, symbol_p2=1, dimension=3
        ):
        self.board = Board(dimension)
        self.player_1 = Player(name_p1, type_p1, difficulty_p1, symbol_p1)
        self.player_2 = Player(name_p2, type_p2, difficulty_p2, symbol_p2)

    def __str__(self):
        result = 'Tablero: ' + str(self.board.get_id()) + '\n'
        result += str(self.player_1) + ' - Id: 1' + '\n'
        result += str(self.player_2) + ' - Id: 2'
        return result

    def is_winner(self):
        """
        Interface with board class to check if last movement made tateti
        """
        if self.board.is_tateti():
            return [self.board.is_tateti(), self.board.get_last_play()]
        else: 
            return [self.board.is_tateti()]

    def player_begin(self):
        """
        Choose randomly a player in order to start the game
        """
        players = [self.player_1.get_name(), self.player_2.get_name()]
        return random.choice(players)

    def next_player_to_move(self):
        if self.board.last_play() == 'X':
            return 'O'
        else:
            return 'X'

    def movement(self, player_name):
        """
        Interface with player class to make a movement within the board
        """
        if self.player_1.get_name() == player_name:
            current_player = self.player_1
        else:
            current_player = self.player_2

        current_player.movement(self.board)

    def get_board(self):
        """
        Returns board object used in current game
        """
        return self.board

    def get_player(self, player_name):
        """
        Returns player object used in current game
        filtered by name
        """
        if self.player_1.get_name() == player_name:
            current_player = self.player_1
        else:
            current_player = self.player_2
        return current_player

    def winner_message(self):
        if self.player_1.get_symbol() == self.board.get_last_play():
            print("\nCongratulations " + self.player_1.get_name() + "!!! You have won this game.\n")
        else:
            print("\nCongratulations " + self.player_2.get_name() + "!!! You have won this game.\n")

    def run(self):
        PLAY_AGAIN = True
        PLAYERS = []
        while PLAY_AGAIN:
            # initial game setup
            PLAYERS.append(new_player(PLAYERS))
            # print(PLAYERS)
            PLAYERS.append(new_player(PLAYERS))
            # print(PLAYERS)
            # load player 1 information
            self.player_1.name = PLAYERS[0][0]
            self.player_1.type = PLAYERS[0][1]
            self.player_1.symbol = PLAYERS[0][2]
            if len(PLAYERS[0]) == 4:
                self.player_1.difficulty = PLAYERS[0][3]
            # load player 2 information
            self.player_2.name = PLAYERS[1][0]
            self.player_2.type = PLAYERS[1][1]
            self.player_2.symbol = PLAYERS[1][2]
            if len(PLAYERS[1]) == 4:
                self.player_2.difficulty = PLAYERS[1][3]

            # game
            begin = self.player_begin()
            if self.player_1.get_name() == begin:
                self.board.update_last_play(self.player_1.get_symbol())
            else:
                self.board.update_last_play(self.player_2.get_symbol())

            while not self.is_winner()[0]: 
                print(self.get_board())
                if self.player_1.get_symbol() == self.board.get_last_play():
                    print(self.player_2.get_name() + ', you move now!')
                    self.player_2.movement(self.board)
                else:
                    print(self.player_1.get_name() + ', you move now!')
                    self.player_1.movement(self.board)

            print(self.board)
            self.winner_message()
            self.board.reset_board()

            PLAYERS = []
            PLAY_AGAIN = play_again()
        
        print("\nBye bye!\n")

if __name__ == "__main__":
    # tests
    game_1 = Game('Joaquin', 'Morita', 0, 1, 0, 1, 0, 1)
    game_2 = Game('Julia', 'Ramiro', 0, 1, 0, 1, 0, 1)
    print(game_1)
    print
    print(game_2)
    print
    print(game_1.get_player('Morita'))
    print
    print(game_1.get_board())
    game_1.movement('Joaquin')
    print(game_1.get_board())
    board = game_1.get_board()
    print(board.get_id())
    print(game_1.is_winner())
    