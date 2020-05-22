from game import Game, Player, Board
import sys
def test_player():
    print("Player() class tests")
    dimension = 3
    board_player = Board(dimension)
    print("Imprimimos tablero vacio: ")
    print(board_player)
    board_player.update_board([0, 2], 'X')
    board_player.update_board([0, 0], 'O')
    board_player.update_board([1, 2], 'X')
    board_player.update_board([2, 2], 'X')
    board_player.update_board([1, 0], 'X')
    board_player.update_board([2, 0], 'O')
    board_player.update_board([0, 1], 'O')
    board_player.update_board([1, 1], 'X')
    #board_player.update_board([2, 1], 'X')
    print(board_player)
    player_1 = Player('Joaquin', 0, 0, 0)
    player_2 = Player('Xano', 1, 1, 1)
    print(player_1)
    print(player_2)
    player_1.movement(board_player)
    print(board_player)
    print(board_player.is_tateti())

def test_board():
    print("Board() class tests")
    dimension = int(sys.argv[1])
    board = Board(dimension)
    board_2 = Board(dimension)
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
    # board_2
    print(board_2)
    print(board_2.is_tateti())
    board_2.update_board([0, 0], 'X')
    print(board_2)
    print(board_2.is_tateti())

def test_game():
    print("Game() class tests")
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
    
if __name__ == "__main__":
    test_board()
    test_player()
    test_game()