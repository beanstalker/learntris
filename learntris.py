#!/usr/bin/env python3

import os, sys

class Board:
    """A simple class defining the tetris game board."""
    def __init__(self):
        """Initialises an empty game board."""
        self.score = 0
        self.lines = 0
        self.width = 10
        self.depth = 22
        self.activeTetramino = None
        self.tetraminoCoords = {"x":None, "y":None}
        self.rotated = False
        self.matrix = [["."] * self.width] * self.depth
    
    def printMatrix(self):
        """Print the game matrix."""
        for i in self.matrix:
            print(*i, sep=" ", end="\n")
    
    def clearMatrix(self):
        """Reset the game matrix."""
        self.matrix = [["."] * self.width] * self.depth
    
    def setMatrix(self):
        """Gets user input (stdin) to set the matrix."""
        i = 0
        while i < self.depth:
            self.matrix[i] = input().split()
            i += 1
    
    def lineClear(self):
        """If a single line in the matrix is full, it is reset."""
        i = 0
        while i < self.depth:
            clear = True
            for j in self.matrix[i]:
                if j is ".":
                    clear = False
            if clear:
                self.matrix[i] = ["."] * self.width
                self.score += 100
                self.lines += 1
            i += 1


class Tetramino:
    """A simple class to define the different tetraminos."""
    tetraminos = {
        "I":[
            [".", ".", ".", "."],
            ["c", "c", "c", "c"],
            [".", ".", ".", "."],
            [".", ".", ".", "."]
        ],
        "O":[ 
            ["y", "y"],
            ["y", "y"]
        ],
        "Z":[
            ["r", "r", "."],
            [".", "r", "r"],
            [".", ".", "."]
        ],
        "S":[
            [".", "g", "g"],
            ["g", "g", "."],
            [".", ".", "."]
        ],
        "J":[
            ["b", ".", "."],
            ["b", "b", "b"],
            [".", ".", "."]
        ],
        "L":[
            [".", ".", "o"],
            ["o", "o", "o"],
            [".", ".", "."]
        ],
        "T":[
            [".", "m", "."],
            ["m", "m", "m"],
            [".", ".", "."]
        ]
    }
    
    def __init__(self, selector):
        """Initialises a single tetramino with a specific shape"""
        self.tetramino = self.tetraminos[selector]
    
    def printTetramino(self):
        """Prints the initialised tetramino."""
        for i in self.tetramino:
            print(*i, sep=" ", end="\n")
    
    def rotateTetramino(self):
        self.tetramino = list(zip(*self.tetramino[::-1]))

game = Board()
while True:
    commands = input().replace(" ", "")
    #commands = input().split()
    query = False
    for i in commands:
        if i == "q":
            sys.exit(0)
        elif i == "p":
            game.printMatrix()
        elif i == "c":
            game.clearMatrix()
        elif i == "g":
            game.setMatrix()
        elif i == "s" and (not query):
            game.lineClear()
        elif i == "t":
            game.activeTetramino.printTetramino()
        elif i == "?":
                query = True
                continue
        elif i == "s" and query:
            print(game.score)
            query = False
        elif i == "n" and query:
            print(game.lines)
            query = False
        elif (i == "I") or (i == "O") or (i == "Z") or (i == "S") or
             (i == "J") or (i == "L") or (i == "T"):
            game.activeTetramino = Tetramino(i)
        elif i == ")":
            game.activeTetramino.rotateTetramino()
        elif i == ";":
            print()
        else:
            print("Bad input.")
            sys.exit(0)

        