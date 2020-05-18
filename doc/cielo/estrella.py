import sys
import random

class Estrella():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forma = random.choice(['*', '.', '.', '.'])

    def __str__(self):
        return self.forma