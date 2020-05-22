import sys
import uuid
class Board():
    def __init__(self, dimension):
        self.id = uuid.uuid4()
        self.dimension = dimension
        self.board = [[" " for i in range(dimension)] for i in range(dimension)]
        self.last_play = ''

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
        """
        Returns True if tateti position or False if it is not
        """
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ' or \
           self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ' or \
           self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ' or \
           self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ' or \
           self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ' or \
           self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ' or \
           self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ' or \
           self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True
        else:
            return False

    def update_board(self, position, symbol):
        """
        Interface with player class in order to make a movement.
        last_play is updated so winner player can be identified
        """
        _ok = False
        y = position[0]
        x = position[1]
        if self.board[x][y] != 'X' and self.board[x][y] != 'O':
            self.board[x][y] = symbol
            self.last_play = symbol 
            _ok = True
        
        return _ok

    def reset_board(self):
        self.board = [[" " for i in range(self.get_dimension())] for i in range(self.get_dimension())]

    def get_board(self):
        """
        Returns board object
        """
        return self.board

    def get_id(self):
        """
        Returns board id
        """
        return self.id

    def get_last_play(self):
        """
        Returns board last_play
        """
        return self.last_play

    def update_last_play(self, new_last_play):
        """
        Update last_play attribute with a new value
        """
        self.last_play = new_last_play

    def get_dimension(self):
        """
        Returns board dimension
        """
        return self.dimension

if __name__ == "__main__":
    print("Board class!")
    