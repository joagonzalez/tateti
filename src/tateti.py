from game import Game
from library import banner as banner, instructions as instructions

if __name__ == "__main__":
    banner()
    instructions()

    app = Game()
    app.run()