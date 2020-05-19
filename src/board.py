import uuid
class Board():
    def __init__(self, dimension):
        self.id = uuid.uuid4()
        self.dimension = dimension
        self.board = [[" " for i in range(dimension)] for i in range(dimension)]

    def __str__(self):
        pass

    def is_tateti(self):
        pass

    def update_board(self, position, symbol):
        x = position[0]
        y = position[1]
        self.board[x][y] = symbol 

    def get_board(self):
        return self.board

    def get_id(self):
        return self.id

    def get_dimension(self):
        return self.dimension

if __name__ == "__main__":
    pass