
class Side:

    def __init__(self, types=[None] * 4):
        self.sides = types


class Piece:

    def __init__(self, edges=[None] * 4):
        self.rotation = 0
        self.edges = edges

    def rotateLeft(self):
        self.rotation -= 1
        self.rotation %= 4
    
    def rotateRight(self):
        self.rotation += 1
        self.rotation %= 4

    def matchingPieces(self, other, otherRotation):
        return self.edges[self.rotation] == other.edges[other.rotation + other.rotation + otherRotation]


class Puzzle:

    def __init__(self, width, height):
        self.grid = [[Piece() for x in height] for y in width]

    def solve(self):
        # Iterate through the grid
        # If a piece is a corner piece or edge, rotate accordingly
        # Work outside in, doing corners and edges first
        # Otherwise, rotate pieces internally based on their rotation
        # Check if one piece matches another in its current orientation
        print(self.grid)


def main():
    print("\nHello World\n")


if __name__ == "__main__":
    main()
